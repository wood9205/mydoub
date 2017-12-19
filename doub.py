import requests
import re

headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/62.0.3202.94 YaBrowser/17.11.0.2191 Yowser/2.5 Safari/537.36"}
html = requests.get('https://doub.bid/sszhfx/',headers=headers)
ssr_pool = re.findall('ssr://(.*?)([\s|"|<|,])', html.text, re.S)
ssr=[]
for a in ssr_pool:
	if len(a[0]) <=10:
		continue
		pass
	ssr.append(a[0].replace('!',''))
ssr=list(set(ssr))
print(ssr)