# 1. Käytetään virallista Python-imagea pohjana. → kevyt Python-image (nopeampi build).
FROM python:3.12-slim 

# 2. Asennetaan järjestelmäriippuvuudet (tarvitaan psycopg2:lle)
RUN apt-get update && apt-get install -y \
    gcc \
    libpq-dev \
    && rm -rf /var/lib/apt/lists/*

# 2. Asetetaan työskentelykansio konttiin. WORKDIR /app → kaikki komennot ajetaan tästä hakemistosta.
WORKDIR /app

# 3. Kopioidaan riippuvuudet ja asennetaan ne. → Asennetaan paketit erikseen, 
#jotta Docker osaa käyttää välimuistia (nopeuttaa buildeja).
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# 4. Kopioidaan koko projektin lähdekoodi konttiin
COPY . .

# 5. Altistetaan portti (Django runserver tai gunicorn kuuntelee tätä)→ DRF palvelee portissa 8000.
EXPOSE 8000

# 6. Käynnistyskomento gunicornilla. → Tuotantoon sopiva serveri, joka osaa palvella Djangoa.
CMD ["gunicorn", "easylist.wsgi:application", "--bind", "0.0.0.0:8000"]