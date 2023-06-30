
import csv

apps = [
    'youtube',
    'whatsapp',
    'netflix',
    'amazon_shop',
    'paypal'
    ]

for app in apps:

    data = []

    # read the frequency distribution
    with open(f'fdist_{app}.csv', 'r', newline='\n') as f:
        reader = csv.reader(f, delimiter=',', quotechar='|')
        for row in reader:
            data.append(row)

    # calculate and print the min and max doc length
    print(f'The max doc length of {app} is: ', max(int(x[0]) for x in data))
    print(f'The min doc length of {app} is: ', min(int(x[0]) for x in data), '\n\n')
