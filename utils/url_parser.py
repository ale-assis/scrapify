import os
from urllib.parse import urlparse, unquote

def generate_file_name(url_input):
    # Pega a parte final da URL
    caminho = urlparse(url_input).path
    ultimo_segmento = caminho.strip("/").split("/")[-1]

    # Decodifica caracteres tipo %20 e coloca tudo em minúsculas
    nome_base = unquote(ultimo_segmento).lower()

    # Garante que o nome seja seguro (só letras)
    nome_base = ''.join(c if c.isalnum() or c in ('-', '_') else '_' for c in nome_base)
    return f"{nome_base}.txt"

