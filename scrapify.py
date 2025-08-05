import requests
from bs4 import BeautifulSoup
from utils.insert_url import url
from utils.define_dir import os, file_path

def extract_wiki_text(url, file_name='resultado.txt'):
    headers = {
        'User-Agent': 'Mozilla/5.0'
    }

    # Faz a requisição
    response = requests.get(url, headers=headers)
    if response.status_code != 200:
        print(f"Erro ao acessar a página: {url}")
        return

    soup = BeautifulSoup(response.text, 'html.parser')

    # Pega o título
    title = soup.find('h1')
    text_title = title.text.strip() if title else 'A página não possui título.'

    # Pega o conteúdo principal
    content_div = soup.find('div', class_='mw-parser-output')
    if not content_div:
        print("Conteúdo principal não encontrado.")
        return

    # Junta todo o texto dos parágrafos
    paragraphs = content_div.find_all(['p', 'h2', 'h3', 'li'])
    final_text = text_title + '\n\n'

    for element in paragraphs:
        text = element.get_text(strip=True)
        if text:
            final_text += text + '\n\n'

    with open(file_path, 'w', encoding='utf-8') as file:
        file.write(final_text)

    print(f"Texto salvo em: {os.path.abspath(file_path)}")