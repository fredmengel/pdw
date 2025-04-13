Clínica Saúde Integrada

Sistematização da matéria PDW. Este projeto é uma aplicação web simples que simula uma clínica médica, permitindo a consulta de especialidades, verificação de disponibilidade de profissionais e envio de mensagens.

Organização do projeto:


*Backend: clinica-api (contém apy.py, profissionais.json e requirements.txt)

*Frontend: clinica-frontend/fotos (subpastas profissionais e servicos)

*Página principal: index.html (na raiz)

*Funcionalidades:

Consulta de especialidades médicas

Listagem dinâmica de profissionais com fotos

Busca por especialidade e nome

Exibição de disponibilidade

Formulário de contato

*Tecnologias utilizadas:

Backend (Render): Python (Flask) e Flask-Cors

Frontend (GitHub Pages): HTML5, CSS3, JavaScript (Vanilla JS) e Fetch API

Links públicos:

API no Render: https://pdw.onrender.com/profissionais

Site no GitHub Pages: https://fredmengel.github.io

Como executar localmente:
Requisitos:

Python 3.7+

Navegador moderno

Passos:

Acesse a pasta clinica-api

Instale as dependências: pip install -r requirements.txt

Execute: python apy.py

A API estará disponível em http://127.0.0.1:10000/profissionais

Para abrir o frontend localmente, abra o arquivo index.html no navegador ou use o Live Server no VSCode.

Exemplo de profissionais.json:

{
"profissionais": [
{ "nome": "Ana Silva", "especialidade": "Cardiologista", "disponivel": true, "foto": "ana_silva.jpg" },
{ "nome": "Pedro Lima", "especialidade": "Nutricionista", "disponivel": false, "foto": "pedro_lima.jpg" },
{ "nome": "Mariana Costa", "especialidade": "Radiologista", "disponivel": true, "foto": "mariana_costa.jpg" },
{ "nome": "João Pereira", "especialidade": "Dermatologista", "disponivel": true, "foto": "joao_pereira.jpg" },
{ "nome": "Carla Souza", "especialidade": "Nutricionista", "disponivel": true, "foto": "carla_souza.jpg" }
]
}

Instalação manual de dependências (se não usar requirements.txt):

pip install Flask==3.0.2

pip install flask-cors==4.0.0

Desenvolvido por: Frederico Martins Engel
