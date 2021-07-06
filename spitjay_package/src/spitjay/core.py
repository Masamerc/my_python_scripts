#!/usr/bin/env python

import datetime
import json
import random 


names = ['jp', 'sk', 'po', 'df']

def get_random_date() -> datetime.datetime:
    return datetime.datetime.now() - datetime.timedelta(days=random.randint(0, 100))


def spit_1000_json() -> None:
    mock_data = [
        {'name': random.choice(names), 'date': get_random_date().strftime('%Y-%m-%d'), 'score': random.randint(0, 100)}
        for _ in range(1000)
    ]

    json_string = json.dumps(mock_data, indent=2)

    print(json_string)
    

if __name__ == '__main__':
    spit_1000_json()
