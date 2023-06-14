import json
from datetime import datetime

class DateTimeDecoder(json.JSONDecoder):
    def __init__(self, *args, **kwargs):
        super(DateTimeDecoder, self).__init__(object_hook=self.object_hook, *args, **kwargs)

    def object_hook(self, dct):
        for k, v in dct.items():
            if isinstance(v, str):
                try:
                    dct[k] = datetime.fromisoformat(v)
                except ValueError:
                    pass
        return dct

apps = [
    'youtube',
    'whatsapp',
    'netflix',
    'amazon_shop',
    'paypal'
    ]

for app in apps:

    versions = []
    major_versions = []

    # Load the scraped data into a dictionary
    with open(f'./data/{app}_reviews_all.json', 'r', encoding='utf-8') as f:
        data = json.load(f, cls=DateTimeDecoder)

    # filter out any irrelevant app versions
    for entry in data:
        if entry['reviewCreatedVersion'] != None:
            if app == 'youtube':
                # filter out Dogfood/experimental versions
                # YouTube has only an E and a -DOGFOOD appendix
                if '-DOGFOOD' not in entry['reviewCreatedVersion'] and 'E' not in entry['reviewCreatedVersion']:
                    versions.append(entry['reviewCreatedVersion'])
            elif app == 'whatsapp':
                # no filtering required
                versions.append(entry['reviewCreatedVersion'])
            elif app == 'netflix':
                # filter out Dogfooding, D1 and 1.0 as experimental versions
                if 'Dogfooding' not in entry['reviewCreatedVersion'] and 'D1' not in entry['reviewCreatedVersion'] and '1.0' not in entry['reviewCreatedVersion']:
                    versions.append(entry['reviewCreatedVersion'])
            elif app == 'amazon_shop':
                # no filtering required
                versions.append(entry['reviewCreatedVersion'])
            elif app == 'paypal':
                # no filtering required
                versions.append(entry['reviewCreatedVersion'])

    # create a set
    versions = list(set(versions))

    # sort the versions based on numbers between the dot
    if app != 'netflix':
        versions.sort(key=lambda x: list(map(int, x.split('.'))))
    else:
        # custom sort function for netflix to keep the additional text ([...] build [...])
        versions.sort(key=lambda x: list(map(int, x.split(' ')[0].split('.'))))

    for version in versions:
        if app != 'whatsapp':
            major_version = version.split('.')[0]
            major_versions.append(major_version)
        else:
            major_version = '.'.join(version.split('.')[0:2])
            major_versions.append(major_version)

    major_versions = list(set(major_versions))
    major_versions.sort(key=lambda x: list(map(int, x.split('.'))))

    # calculate the average
    print(f'The number of versions for {app} are: ', len(versions))
    print(f'The oldest version for {app} is: ', versions[0])
    print(f'The newest version for {app} is: ', versions[-1])
    print(f'The oldest major version for {app} is: ', major_versions[0])
    print(f'The newest major version for {app} is: ', major_versions[-1])
    print(f'The number of major versions for {app} are: ', len(major_versions))