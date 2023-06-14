import matplotlib.pyplot as plt
import nltk
import json
from datetime import datetime
import csv
import statistics
from tqdm import tqdm

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

days = set()

apps = [
    'youtube',
    'whatsapp',
    'netflix',
    'amazon_shop',
    'paypal'
    ]


for app in apps:
    # Dump the scraped data into a JSON file
    with open(f'./data/{app}_reviews_all.json', 'r', encoding='utf-8') as f:
        data = json.load(f, cls=DateTimeDecoder)

    ratings = []

    for entry in data:
        if entry['score'] != None:
            ratings.append(entry['score'])

    ratings = sorted([rating for rating in ratings])

    print(f'Largest number of ratings for {app}: ', ratings[-1])

    fdist = nltk.FreqDist(ratings)

    print(fdist.most_common())
