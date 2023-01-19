# Movie Project
[![NPM](https://img.shields.io/npm/l/react)](https://github.com/pauloliveiram/adote/blob/main/license) ![NPM](https://img.shields.io/badge/Status-Em%20desenvolvimento-orange)

## Sobre o projeto

O Adote é uma aplicação fullstack web desenvolvida na Pystack Week do canal Pythonando, que consiste em uma plataforma para intermediar adoção de animais, em que realiza a conexão entre pessoas que desejam colocar um animal para adoção com pessoas que queiram adotar. Um usuário pode cadastrar um animal na plataforma e outro usuário pode solicitar a sua adoção, podendo ser aceita ou recusada. 

## Tecnologias utilizadas

### Back-end

- Python
- Django

### Front-end

- HTML
- CSS
- JavaScript

## Features

- Criação e autenticação de usuário
- Cadastro de animais
- Ver animais disponíveis para adoção
- Busca de animais por cidade e raça
- Solicitação de adoção
- Dashboard com dados sobre as adoções


## Como executar o projeto

### Pré-requisitos

- Python ≥ 7.0
- Pip


```bash

# Clonar repositório
git clone https://github.com/pauloliveiram/adote.git

# Entrar na pasta do projeto
cd movie-adote

# Criar um ambiente virtual 
python -m venv venv
	
# Ativar o ambiente virtual

(Windows) venv\Scripts\activate
(Linux) source venv/bin/activate
					
# Instalar as dependências do projeto
pip install -r requirements.txt
								
# Executar as migrações no banco de dados
python manage.py migrate
							
# Executar o servidor
python manage.py runserver
```							

# Autor

Paulo Oliveira

[https://www.linkedin.com/in/pauloliveiram/](https://www.linkedin.com/in/pauloliveiram/)


