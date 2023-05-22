from urllib.request import urlopen

with urlopen("https://www.baidu.com") as f:
    print(f.read())