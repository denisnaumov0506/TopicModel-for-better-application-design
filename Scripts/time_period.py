import json
from datetime import datetime
import numpy as np

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

    dates = []

    # Dump the scraped data into a JSON file
    with open(f'./data/{app}_reviews_all.json', 'r', encoding='utf-8') as f:
        data = json.load(f, cls=DateTimeDecoder)

    # filter out any positive reviews for the content meta data
    for entry in data:
        dates.append(entry['at'].date())

    # create a set
    dates = list(set(dates))
    dates.sort()

    # calculate the average
    print(f'The start date for {app} is: ', dates[0])
    print(f'The end date for {app} is: ', dates[-1], '\n\n')
