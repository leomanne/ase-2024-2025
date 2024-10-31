# Usa l'immagine base di Python
FROM python:3.12-slim

# Imposta la directory di lavoro
WORKDIR /app

# Copia il file dei requisiti nell'immagine
COPY requirements.txt .

# Installa le dipendenze
RUN pip install --no-cache-dir -r requirements.txt

# Copia il codice dell'app nell'immagine
COPY . .

# Espone la porta per Flask
EXPOSE 5000

# Comando per avviare Flask
CMD ["flask", "run", "--host=0.0.0.0", "--port=5000"]
