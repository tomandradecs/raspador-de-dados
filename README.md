Raspador de Dados (Web Scraper) Simples em Python

🕷️ Sobre o Projeto
Este projeto é um Web Scraper simples desenvolvido em Python, projetado para extrair informações básicas de páginas web. Utilizando as poderosas bibliotecas requests para fazer as requisições HTTP e BeautifulSoup para analisar o HTML, o programa consegue acessar uma URL fornecida pelo usuário e extrair elementos como títulos e links. É uma excelente introdução ao mundo da raspagem de dados, demonstrando como coletar informações estruturadas da internet.

✨ Funcionalidades
Busca de Página Web: Realiza requisições HTTP para obter o conteúdo de uma URL específica.
Análise de HTML: Converte o código HTML da página em um objeto Python navegável.
Extração de Dados:
Extrai todos os títulos <h2> da página.
Extrai todos os links <a> (âncoras) com seus respectivos atributos href.
Exibição Estruturada: Apresenta os dados extraídos de forma clara e organizada no terminal.
Tratamento de Erros: Lida com falhas de conexão ou URLs inválidas, informando o usuário.

🚀 Como Usar
Para usar este web scraper, siga os passos abaixo:

Instale as Dependências:
Abra seu terminal ou prompt de comando e execute:

Bash

pip install requests beautifulsoup4
Isso instala as bibliotecas necessárias para fazer requisições e analisar HTML.

Clone o Repositório:

Bash

git clone https://github.com/tomandradecs/raspador-de-dados.git
cd raspador-de-dados

Execute o Script Python:

Bash

python web_scraper.py
Forneça a URL:
O programa pedirá que você digite a URL da página que deseja raspar.

Exemplo de interação:

Digite a URL da página que deseja acessar: https://www.scrapethissite.com/pages/simple/
Título: A Great Website to Scrape
Link: None
----------------------------------------
Título: Other Examples
Link: /pages/
----------------------------------------
(A saída exata dependerá da estrutura do site que você escolher raspar.)

🛠️ Tecnologias Utilizadas
Python 3.x
requests: Biblioteca para fazer requisições HTTP.
BeautifulSoup4 (bs4): Biblioteca para parsing de HTML e XML.

🤝 Contribuição
Tem ideias para melhorar este scraper, adicionar mais funcionalidades ou refinar a extração de dados? Suas contribuições são muito bem-vindas!

Abra uma Issue para discutir sua sugestão ou um problema.
Faça um Fork do projeto.
Crie uma nova branch para suas alterações.
Envie um Pull Request detalhando suas modificações.

📄 Licença
Este projeto está licenciado sob a Licença MIT. Para mais detalhes, consulte o arquivo LICENSE.

📧 Contato
Tom Andrade - tom_andrade.ad@outlook.com

LinkedIn: linkedin.com/in/tom-andrade-08476a367/

GitHub: github.com/tomandradecs
