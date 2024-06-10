import requests

headers = {
    'accept': 'application/json, text/plain, */*',
    'accept-language': 'es-ES,es;q=0.9',
    'origin': 'https://www.preciosclaros.gob.ar',
    'referer': 'https://www.preciosclaros.gob.ar/',
    'sec-ch-ua': '"Opera GX";v="109", "Not:A-Brand";v="8", "Chromium";v="123"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'cross-site',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/123.0.0.0 Safari/537.36 OPR/109.0.0.0',
    'x-api-key': 'zIgFou7Gta7g87VFGL9dZ4BEEs19gNYS1SOQZt96',
}

response = requests.get(
    'https://d3e6htiiul5ek9.cloudfront.net/prod/productos?string=morcilla&array_sucursales=10-2-282,10-2-290,2002-1-80,2005-1-79,9-1-188,9-1-400,10-2-283,10-1-29,2002-1-34,2002-1-132,9-1-174,9-1-402,9-1-170,9-3-5222,9-1-196,10-2-287,9-1-181,9-1-857,12-1-209,9-1-180,9-1-175,10-2-288,9-1-855,9-1-173,9-1-546,2002-1-56,9-1-190,9-1-189,9-1-171,9-1-176&offset=0&limit=50&sort=-cant_sucursales_disponible',
    headers=headers,
)

print(response.json())