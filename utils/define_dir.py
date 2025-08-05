import os
from utils.insert_url import url
from utils.url_parser import generate_file_name

# Caminho absoluto para pasta de output
project_root = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# Caminho para a pasta "output"
output_dir = os.path.join(project_root, "output")

# Cria a pasta se ela ainda não existir
os.makedirs(output_dir, exist_ok=True)

# Define o nome do arquivo
file_name = generate_file_name(url)

# Junta a pasta + nome do arquivo
file_path = os.path.join(output_dir, file_name)