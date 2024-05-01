  # Use a imagem base do Python
FROM python:3.9-slim

# Defina o diretório de trabalho como /app
WORKDIR /app

# Copie o arquivo requirements.txt para o diretório de trabalho
COPY requirements.txt requirements.txt

# Instale as dependências do projeto
RUN pip install -r requirements.txt

# Copie o conteúdo do diretório atual para o diretório de trabalho no contêiner
COPY . .

# Defina as variáveis de ambiente necessárias para o Django
ENV PYTHONUNBUFFERED 1
ENV DJANGO_SETTINGS_MODULE projeto_filmesdb.settings

# Execute as migrações do Django
RUN python manage.py migrate

# Exponha a porta 8000 para acesso externo
EXPOSE 8000

# Comando para iniciar o servidor Django
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
