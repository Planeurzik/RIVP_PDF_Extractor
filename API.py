import requests

NUM_ADEME = "2375E2231272D"

cookies = {
    'tarteaucitron': '!googletagmanager=true',
    '_ga': 'GA1.3.1182479622.1689592022',
    '_gid': 'GA1.3.1841884616.1689592022',
    '_gat_UA-12073385-31': '1',
    '_ga_PZRMHNSZP7': 'GS1.3.1689592022.1.1.1689592303.0.0.0',
}

headers = {
    'Accept': 'application/json, text/plain, */*',
    'Accept-Language': 'fr-FR,fr;q=0.9,en;q=0.8',
    'Connection': 'keep-alive',
    # 'Cookie': 'tarteaucitron=!googletagmanager=true; _ga=GA1.3.1182479622.1689592022; _gid=GA1.3.1841884616.1689592022; _gat_UA-12073385-31=1; _ga_PZRMHNSZP7=GS1.3.1689592022.1.1.1689592303.0.0.0',
    'Referer': f'https://observatoire-dpe-audit.ademe.fr/afficher-dpe/{NUM_ADEME}',
    'Sec-Fetch-Dest': 'empty',
    'Sec-Fetch-Mode': 'cors',
    'Sec-Fetch-Site': 'same-origin',
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36',
    'sec-ch-ua': '"Not.A/Brand";v="8", "Chromium";v="114", "Google Chrome";v="114"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"macOS"',
}

response = requests.get(f'https://observatoire-dpe-audit.ademe.fr/pub/dpe/{NUM_ADEME}', cookies=cookies, headers=headers)
data = response.json()
consommation , emission = data['consommation'],data['emission']
print(consommation , emission)