# Use uma imagem leve do Python como base
FROM python:3.12.5-slim

# Define o diretório de trabalho no contêiner
WORKDIR /app

# Copia os arquivos do projeto para o contêiner
COPY . /app

# Instala as dependências do sistema necessárias
RUN apt-get update && apt-get install -y \
    build-essential \
    libpq-dev \
    --no-install-recommends && rm -rf /var/lib/apt/lists/*

# Instala as dependências do Python
RUN pip install --no-cache-dir --upgrade pip \
    && pip install --no-cache-dir -r requirements.txt

# Realiza as migrações antes de iniciar o servidor
RUN  python manage.py migrate

# Expõe a porta padrão do Django
EXPOSE 8000

# Comando de inicialização do servidor
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
