# This script gives us the percentage of all negative scores from all reviews
# A negative score is anything below 5 stars.

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

    scores_negative = []

    # Load the scraped data into memory
    with open(f'./data/{app}_reviews_all.json', 'r', encoding='utf-8') as f:
        data = json.load(f, cls=DateTimeDecoder)

    # filter out any positive reviews for the content meta data
    for entry in data:
        if int(entry['score']) < 5:
            scores_negative.append(entry['score'])

    # calculate the average
    print(f'The percentage of negative reviews for {app} is: ', len(scores_negative)/len(data))