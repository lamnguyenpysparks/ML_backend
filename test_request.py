import requests
import os
import glob
from concurrent import futures
import time
from datetime import datetime, timedelta

URL = 'http://127.0.0.1:8000/prediction/prediction'

# fn = '/home/lam/repos/template_api/coco8/images/train/000000000025.jpg'

def send_request(fn):
    now = datetime.now()
    next_sec = now +  timedelta(seconds=1)
    headers = {
        'accept': 'application/json',
        # requests won't add a boundary if this header is set when you pass files=
        # 'Content-Type': 'multipart/form-data',
    }

    params = {
        'client_id': 'asd',
        'token': 'asdas',
    }

    files = {
        'file': (os.path.basename(fn), open(fn, 'rb'), 'image/jpeg'),
    }

    r = requests.post(URL, files=files, params=params, headers=headers)
    time.sleep(max((next_sec - datetime.now()).total_seconds(), 0.2))
    return r.text

files = glob.glob('/home/lam/repos/template_api/val2017/*.jpg')

with futures.ThreadPoolExecutor(max_workers=10) as executor:
    for i in executor.map(send_request, [fn for fn in files[:500]]):
        print(i)