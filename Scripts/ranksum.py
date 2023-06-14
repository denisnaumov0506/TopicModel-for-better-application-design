import pandas as pd
from scipy.stats import ranksums
import nltk
import json
from datetime import datetime
import statistics
from tqdm import tqdm

import pandas as pd

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

    # Retrieve the scraped data from a JSON file
    with open(f'./data/{app}_reviews_all.json', 'r', encoding='utf-8') as f:
        data = json.load(f, cls=DateTimeDecoder)

    ratings = []

    df = pd.DataFrame() # empty dataframe
    feedback = []
    ratings = []

    for entry in data:
        if entry['score'] != None and entry['content'] != None:
            feedback.append(entry['content'])
            ratings.append(entry['score'])

    df['feedback'] = feedback
    df['rating'] = ratings

    df['feedback_length'] = df['feedback'].apply(lambda x: len(x))

    print(df)

    # Split feedback data into rating groups
    groups = df.groupby('rating')

    # Calculate median length of feedback for each group
    medians = groups['feedback_length'].median()

    # Initialize list to store pairs of groups to compare
    group_pairs = [
        (1, 2), (1, 3), (1, 4), (1, 5),
        (2, 3), (2, 4), (2, 5),
        (3, 4), (3, 5),
        (4, 5)
        ]

    print(f'\n\nApp: {app}\n')

    # Perform Wilcoxon rank sum tests for each pair of groups
    for pair in group_pairs:
        group1 = groups.get_group(pair[0])["feedback_length"]
        group2 = groups.get_group(pair[1])["feedback_length"]
        test_stat, p_value = ranksums(group1, group2)
        print(f"Pair: {pair}, Median diff: {medians[pair[0]] - medians[pair[1]]: .2f}, P-Value: {p_value: .3f}, Test: {test_stat}")

