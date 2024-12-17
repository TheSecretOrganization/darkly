# hidden

* Go to `/robots.txt`, we can see a reference to an `/.hidden`.
* At `/.hidden` we can observe an list of folder with a `README` file in each of them. We can assume the flag will be somewhere in here.

## Finding the flag

We can use a python script to check each folder and search for a `README` file with a `flag` word in it.

### Setup venv

```bash
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```

### Run script

```py
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

```

## Result

At the end of the script we can see it found the flag at `/.hidden/whtccjokayshttvxycsvykxcfm/igeemtxnvexvxezqwntmzjltkt/lmpanswobhwcozdqixbowvbrhw/`
