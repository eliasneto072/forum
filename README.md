# Fórum de Discussão em Django

## Descrição

Este projeto é um fórum de discussão completo desenvolvido com o framework Django. Ele oferece uma plataforma robusta para a criação e gerenciamento de salas de discussão, pesquisa de tópicos e gerenciamento de conteúdo.

## Funcionalidades

- Criação e Gerenciamento de Salas
- Pesquisa e Navegação de Tópicos
- Gerenciamento de Conteúdo
- Interface Simples

## Tecnologias Utilizadas

- Django
- HTML
- Postgres
- Docker

## Instalação

Para instalar e executar o projeto, siga estas etapas:

1. Clone o Repositório
2. Crie um Ambiente Virtual (python -m venv .venv) e Ative (cd .venv/scripts/activate)
3. Instale as Dependências
4. Aplique as Migrações
5. Crie um Superusuário
6. Inicie o Servidor de Desenvolvimento

## Preview app
https://github.com/user-attachments/assets/f6510484-6cbb-4f52-a295-a91d21b7567c

## Contato
Para dúvidas ou mais informações, entre em contato através do e-mail: eliasneto072@gmail.com.



## Docker deployment

1. Copy `.env.example` to `.env`
2. Update `SECRET_KEY`, `DB_PASSWORD` and `ALLOWED_HOSTS`
3. Run: `docker compose up --build -d`
4. Open: `http://localhost:8000`

Stop containers:
- `docker compose down`

Stop and remove database volume:
- `docker compose down -v`

https://forum-207f.onrender.com/
