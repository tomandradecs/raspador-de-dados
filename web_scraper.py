#Este projeto vai te introduzir ao mundo do web scraping com Python. Voce vai criar um programa Python que acessa uma pagina da internet, extrai informações expecificas e as exibe. Para começar, vamos focar em uma pagina simples e publica para aprender os fundamentos.

#Qque voce vai aprender: Requisicoes HTTP, parsing HTML, bibliotecas externas, extração de dados, tratamento de erros.

#Funcionalidades: URL de entrada, requisicao, analise html, extracao simples, exibicao, tratamento de erros.

import requests
from bs4 import BeautifulSoup
def fetch_page(url):
    try:
        response = requests.get(url)
        response.raise_for_status()  # Verifica se a requisição foi bem-sucedida
        return response.text
    except requests.exceptions.RequestException as e:
        print(f"Erro ao acessar a página: {e}")
        return None
def parse_html(html_content):
    soup = BeautifulSoup(html_content, 'html.parser')
    return soup
def extract_data(soup):
    # Exemplo: extrair todos os títulos de artigos (h2) e links (a)
    titles = soup.find_all('h2')
    links = soup.find_all('a')

    extracted_data = []
    for title in titles:
        extracted_data.append({
            'title': title.get_text(strip=True),
            'link': title.find('a')['href'] if title.find('a') else None
        })
    
    return extracted_data
def display_data(data):
    if not data:
        print("Nenhum dado encontrado.")
        return
    
    for item in data:
        print(f"Título: {item['title']}")
        if item['link']:
            print(f"Link: {item['link']}")
        print("-" * 40)
def main():
    url = input("Digite a URL da página que deseja acessar: ")
    html_content = fetch_page(url)
    
    if html_content:
        soup = parse_html(html_content)
        data = extract_data(soup)
        display_data(data)
if __name__ == "__main__":
    main()
# Este é um exemplo simples de web scraping. Você pode expandir este código para extrair mais informações ou lidar com páginas mais complexas.
# Lembre-se de sempre verificar os Termos de Serviço do site que você está acessando para garantir que o web scraping é permitido.
# Além disso, considere adicionar funcionalidades como paginação, autenticação ou manipulação de cookies, dependendo das necessidades do seu projeto.
# Certifique-se de ter as bibliotecas necessárias instaladas:
# pip install requests beautifulsoup4
# Boa sorte com seu projeto de web scraping! Se tiver dúvidas, sinta-se à vontade para perguntar.
