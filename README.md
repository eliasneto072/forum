# 🚀 AeroForum

**AeroForum** é uma aplicação web full stack desenvolvida com **Django**, focada em simular um **fórum moderno**, com autenticação, área administrativa e deploy real em produção.

O projeto foi criado com foco em **boas práticas**, **Docker**, **PostgreSQL** e **deploy em cloud**, servindo como **projeto de portfólio profissional**.

🔗 **Aplicação em produção:**  
👉 https://forum-207f.onrender.com

---

## 🧠 Objetivo do Projeto

Demonstrar domínio prático em:

- Backend com Django
- Banco de dados relacional (PostgreSQL)
- Dockerização de aplicações
- Deploy real em produção (Render)
- Boas práticas de configuração e segurança
- Gerenciamento de variáveis de ambiente
- Servir arquivos estáticos corretamente em produção

---

## 🛠️ Tecnologias Utilizadas

### Backend
- **Python 3.12**
- **Django 4.2 (LTS)**
- **Django REST Framework**
- **Gunicorn**

### Banco de Dados
- **PostgreSQL**

### Infraestrutura / Deploy
- **Docker**
- **Render (Free Tier)**
- **WhiteNoise** (servir arquivos estáticos)
- **dotenv** (configuração por ambiente)

---

## 📦 Arquitetura do Projeto

- Aplicação **totalmente containerizada**
- Separação de ambientes via variáveis (`.env`)
- Banco PostgreSQL externo (cloud)
- Arquivos estáticos coletados com `collectstatic`
- Servidos em produção via WhiteNoise
- Admin do Django habilitado para gerenciamento

---

## ⚙️ Variáveis de Ambiente

Exemplo de configuração:

```env
SECRET_KEY=your-secret-key
DEBUG=False
ALLOWED_HOSTS=forum-207f.onrender.com
DATABASE_URL=postgres://user:password@host:5432/dbname
```
⚠️ O arquivo .env não é versionado por segurança.

---

## 🐳 Rodando Localmente com Docker

1️⃣ Clone o repositório
git clone https://github.com/eliasneto072/forum.git
cd forum-main

2️⃣ Suba os containers
docker compose up --build

A aplicação ficará disponível em:
http://localhost:8000

---

## 🚀 Deploy em Produção

O deploy é feito via Render, utilizando:

- **Dockerfile customizado**
- **PostgreSQL gerenciado**
- **Variáveis de ambiente seguras**
- **Gunicorn como servidor WSGI**
  
Cada novo push no branch principal gera um redeploy automático.

---

## 👨‍💻 Autor

**Desenvolvido por Elias Neto
📍 Brasil 
💼 Desenvolvedor Backend / Full Stack
📫 Aberto a oportunidades e desafios profissionais **

