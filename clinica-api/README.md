# pdw
Sistematização da matéria PDW
# Clínica Saúde Integrada 

Este projeto é uma aplicação web simples que simula uma clínica médica, permitindo a consulta dinâmica de especialidades e profissionais, verificar disponibilidade dos médicos e enviar mensagens diretamente para a clínica.

---

## Organização do Projeto
clinica-saude-integrada/

clinica-api/          # Backend (API Flask)
- apy.py
- profissionais.json
- requirements.txt

clinica-frontend/     # Frontend (HTML/CSS/JS)
- main.html
-fotos
  -profissionais
  -servicos



---

## Funcionalidades

- Consulta de especialidades médicas;
- Listagem dinâmica de profissionais;
- Busca por especialidade e nome do profissional;
- Exibição de disponibilidade dos profissionais;
- Formulário para contato com a clínica.

---

##  Tecnologias utilizadas

### Backend:

- **Python** (Flask)
- **Flask-Cors** (para permitir requisições cross-origin)

### Frontend:

- HTML/CSS
- JavaScript (Vanilla JS)
- Fetch API

---

##  Como executar o projeto

###  Pré-requisitos

- Python 3.7 ou superior
- Navegador moderno (Chrome, Firefox, Edge)

### Passos para executar o Backend (API)

1. Abra um terminal e navegue até o diretório da API:

cd clinica-api


2. Instale as dependências:

pip install -r requirements.txt


5. Inicie a aplicação Flask:

python Apy.py


Após iniciado, o backend estará disponível em:

 **`http://127.0.0.1:5000/profissionais`**

---

### Executando o Frontend

Abra o arquivo `main.html` diretamente no navegador, ou use uma extensão como **Live Server** do Visual Studio Code para maior praticidade.

---

## Estrutura dos dados (JSON)

Exemplo do arquivo `profissionais.json`:

```json
{
  "profissionais": [
    {"nome": "Ana Silva", "especialidade": "Cardiologista" },
    {"nome": "Pedro Lima", "especialidade": "Nutricionista"},
    {"nome": "Mariana Costa", "especialidade": "Radiologista"},
    {"nome": "João Pereira", "especialidade": "Dermatologista"},
    {"nome": "Carla Souza", "especialidade": "Nutricionista"}
  ]
}
```

---

## Instalando Flask e Flask-Cors manualmente

Caso precise instalar manualmente (fora do arquivo `requirements.txt`), utilize os comandos:


pip install Flask==3.0.2
pip install flask-cors==4.0.0




## 👨‍💻 Desenvolvido por:

- **Frederico Martins Engel**

