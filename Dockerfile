# Imagem leve com Python
FROM python:3.12-slim

# Evita arquivos .pyc e melhora logs
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

# Pasta de trabalho no container
WORKDIR /app

# Dependências de sistema (psycopg2 precisa disso em alguns casos)
RUN apt-get update && apt-get install -y --no-install-recommends \
    build-essential \
    libpq-dev \
  && rm -rf /var/lib/apt/lists/*

# Copia requirements e instala deps
COPY requirements.txt /app/
RUN pip install --no-cache-dir -r requirements.txt

# Copia o projeto
COPY . /app/

# Coleta estáticos (vai gerar /app/staticfiles)
# (se der erro aqui por falta de env, deixe para rodar no compose)
# RUN python manage.py collectstatic --noinput

# Porta padrão
EXPOSE 8000

# Comando padrão (vamos sobrescrever no compose com migrations + collectstatic)
CMD ["gunicorn", "studybud.wsgi:application", "--bind", "0.0.0.0:8000"]
