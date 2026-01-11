# 1. Käytetään virallista Python-imagea pohjana. → kevyt Python-image (nopeampi build).
FROM python:3.12-slim 

# 2. Asennetaan järjestelmäriippuvuudet (tarvitaan psycopg2:lle)
RUN apt-get update && apt-get install -y \
    gcc \
    libpq-dev \
    && rm -rf /var/lib/apt/lists/*

# 3. Asetetaan työskentelykansio konttiin. WORKDIR /app → kaikki komennot ajetaan tästä hakemistosta.
# Tämä luo Dockerin sisälle hakemiston /app, johon kaikki projektitiedostot menevät.
# Se on siis kontissa oleva “virtuaalikansio”.
WORKDIR /app

# Kaikki seuraavat komennot (COPY, RUN, CMD jne.) ajetaan tästä hakemistosta käsin.

# 4. Kopioidaan riippuvuudet ja asennetaan ne. → Asennetaan paketit erikseen, 
#jotta Docker osaa käyttää välimuistia (nopeuttaa buildeja).
#Ainoa asia, jolla on merkitystä, on että requirements.txt on ajan tasalla — koska se kertoo Dockerille, mitä kirjastoja asentaa.
#(.) polussa =   Nykyinen työhakemisto kontissa (tässä /app)
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# 5. Kopioidaan koko projektin loppu lähdekoodi konttiin
COPY . .

# 6. Altistetaan portti (Django runserver tai gunicorn kuuntelee tätä)→ DRF palvelee portissa 8000.
EXPOSE 8000

# 7. Käynnistyskomento gunicornilla. → Tuotantoon sopiva serveri, joka osaa palvella Djangoa.
CMD ["gunicorn", "easylist.wsgi:application", "--bind", "0.0.0.0:8000"]