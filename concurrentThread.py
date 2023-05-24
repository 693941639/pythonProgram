import concurrent.futures
import urllib.request

URLS = [
    'https://www.google.com',
    'https://wwww.baidu.com',
    'https://www.bilibili.com/',
    'https://www.youtube.com'
]

def load_url(url, timeout):
    with urllib.request.urlopen(url, timeout=timeout) as conn:
        return conn.read()
    
with concurrent.futures.ThreadPoolExecutor(max_workers=4) as executor:
    future_urls = {executor.submit(load_url, url, 60): url for url in URLS}
    for future_url in concurrent.futures.as_completed(future_urls):
        url = future_urls[future_url]

        try:
            data = future_url.result()
        except Exception as e:
            print(url, e)
        else:
            print(url, len(data))