import csv
import statistics

apps = [
    'youtube',
    'whatsapp',
    'netflix',
    'amazon_shop',
    'paypal'
    ]

for app in apps:

    data = []

    with open(f'fdist_{app}.csv', 'r', newline='\n') as f:
        reader = csv.reader(f, delimiter=',', quotechar='|')
        for row in reader:
            data.append(row)

    # calculate the average
    print(f'The average of {app} is: ', statistics.mean(int(x[0]) for x in data))