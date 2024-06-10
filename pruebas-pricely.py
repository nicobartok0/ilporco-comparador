import requests
from bs4 import BeautifulSoup

cookies = {
    'client': 'e2a890fd-c61a-4c25-aa36-690faee56336',
}

headers = {
    'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
    'accept-language': 'es-ES,es;q=0.9',
    # 'cookie': 'client=e2a890fd-c61a-4c25-aa36-690faee56336',
    'referer': 'https://pricely.ar/product/2000000451770',
    'sec-ch-ua': '"Opera GX";v="109", "Not:A-Brand";v="8", "Chromium";v="123"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
    'sec-fetch-dest': 'document',
    'sec-fetch-mode': 'navigate',
    'sec-fetch-site': 'same-origin',
    'sec-fetch-user': '?1',
    'upgrade-insecure-requests': '1',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/123.0.0.0 Safari/537.36 OPR/109.0.0.0',
}

response = requests.get('https://pricely.ar/product/2000000451770', cookies=cookies, headers=headers)
soup = BeautifulSoup(response.content, 'html.parser')
precio = soup.find('span', {'class': 'font-display text-zinc-700 text-2xl'})
print(precio.text)