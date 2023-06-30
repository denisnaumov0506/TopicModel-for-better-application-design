import csv

apps = ['netflix', 'youtube', 'whatsapp', 'paypal', 'amazon_shop']

for app in apps:

    list_ = []

    # read the frequency distribution
    with open(f'fdist_{app}.csv', 'r', newline='\n') as f:
        reader = csv.reader(f, delimiter=',', quotechar='|')
        for row in reader:
            list_.append(row)

    # sort the list
    list_.sort(key=lambda x: int(x[0]))

    # now calculate the percentage of at and below 280
    print(f'Result for {app}: ', sum(int(x[1]) for x in list_ if int(x[0]) <= 280)/sum(int(x[1]) for x in list_))
