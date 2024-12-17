from bs4 import BeautifulSoup
import requests

print('outfile?')
file = open(input(), 'w')

def scrap(link):
	print(f'scrapping {link}')
	r = requests.get(f'{link}/README')
	content = r.text
	if 'flag' in content:
		print(f'flag found in {link}: {content}')
		exit(0)
	file.write(f'{link}: {content}')
	r.close()

	r = requests.get(link)
	content = BeautifulSoup(r.text, 'html.parser')
	r.close()
	for anchor in content.findAll('a')[1:-1]:
		scrap(f'{link}{anchor.get("href")}')

print('ip?')
ip = input()

scrap(f'http://{ip}/.hidden/')
file.close()
