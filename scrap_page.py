import requests
from bs4 import BeautifulSoup

response = requests.get('https://en.wikipedia.org/wiki/List_of_biblical_names_starting_with_A')

content = response.content

site = BeautifulSoup(content, 'html.parser')

# HTML da notícia
noticia = site.find('div', attrs={'class': 'mw-content-ltr mw-parser-output'})


# Título
titulo = noticia.find('ul')

#mw-content-text > div.mw-content-ltr.mw-parser-output

# Subtítulo: div class="feed-post-body-resumo"
for name in titulo:
    print(name.text)
#subtitulo = titulo.find('a')


#print(subtitulo.text)
