# -*- coding: utf-8 -*-
"""The Transaction Pump continuously pumps money from one account to another"""

import json
import time
import random
import requests

USER = 'user099'
PASSWORD = 'TSuNHAWuHYwH'

URL = 'http://api.futurefinance.io/api'
FROM_ACCOUNT = '4574000007'
TO_ACCOUNT = '4574000008'

TXTS = ['Bilka, Skalborg',
        'Kvickly, Randers',
        'H&M, Lyngby',
        'Amazon.com',
        'SuperBrugsen, Hadsund',
        'Gistrup Bageri',
        'Netflix']

HEADERS = {'Content-Type': 'application/json'}


while True:
    PAYLOAD = {'destinationAccountNumber': TO_ACCOUNT,
               'amount': 1000 * random.random(),
               'postingText': random.choice(TXTS)}

    R = requests.post(URL + '/accounts/' + FROM_ACCOUNT + '/transactions',
                      headers=HEADERS,
                      auth=(USER, PASSWORD),
                      data=json.dumps(PAYLOAD))
    print('Response:', json.dumps(R.json(), sort_keys=True, indent=4))

    time.sleep(5)
