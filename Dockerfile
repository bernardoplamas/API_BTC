# Use uma imagem base do Python
FROM python:3.8-slim

# Define o diretório de trabalho dentro do container
WORKDIR /app

# Copia o código fonte para dentro do container
COPY . .

# Instala as dependências necessárias
RUN pip install --no-cache-dir -r requirements.txt

# Comando a ser executado quando o container for iniciado
CMD ["python", "branch.py"]