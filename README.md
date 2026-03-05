# Matkassen – ETL-projekt

Detta är ett ETL-projekt där jag har byggt en pipeline i Python för att läsa in, rensa och analysera data från en matkasse-tjänst.

Projektet fokuserar på datakvalitet, transformation av data, lagring i databas samt analys genom KPI:er och sentimentanalys.

---

# Vad projektet gör

1. Läser in rådata från CSV  
2. Utför datatvätt (saknade värden, datatyper, inkonsistenta kategorier)  
3. Skapar nya analyskolumner (feature engineering)  
4. Genomför sentimentanalys på kundomdömen  
5. Sparar den rensade datan i en SQLite-databas  
6. Beräknar KPI:er och skapar visualiseringar  

---

# Tekniker och bibliotek

Projektet använder:

- Python  
- Pandas (datahantering)  
- SQLite (databaslagring)  
- Matplotlib (visualisering)  
- Hugging Face Transformers (BERT-modell för sentimentanalys)  
- Jupyter Notebook  
- Git & GitHub  

---

# Projektstruktur

---

# ETL-pipeline

## Extract

Rådata läses in från en CSV-fil med Pandas.

En initial datautforskning (EDA) görs för att identifiera datatyper, saknade värden och inkonsistenta kategorier.

## Transform

Flera transformationer görs för att förbättra datakvaliteten:

- standardisering av kategorier  
- hantering av saknade värden  
- konvertering av datumformat  
- logiska kontroller av vissa fält  

Feature engineering används också för att skapa nya kolumner som underlättar analys.

Exempel på nya kolumner:

- veckodag  
- månad  
- churn-indikator  
- sentimentklassificering  

## Sentimentanalys

Sentimentanalys genomförs på kundomdömen med en BERT-baserad modell via Hugging Face.

Omdömen klassificeras som:

- Positiv  
- Neutral  
- Negativ  

Denna information används senare i KPI-analysen för att förstå kundnöjdhet.

## Load

Den rensade och transformerade datan sparas i en lokal SQLite-databas (`matkassen.db`).

Databasen innehåller tabeller med:

- rensad data  
- valideringsdata  

---

# Validering

För att säkerställa att pipelinen fungerar på ny data kördes hela processen även på ett separat valideringsdataset.

Pipelinen hanterar samma dataproblem automatiskt utan manuella ändringar.

---

# KPI:er och analys

Flera KPI:er beräknas för att skapa affärsinsikter, exempelvis:

- kundbetyg per kasstyp  
- churn-rate  
- leveransstatus per kategori  
- sentimentfördelning i kundrecensioner  

Visualiseringar skapas med Matplotlib för att tydliggöra resultaten.

---

# Reflektion

## Syfte och upplägg

Målet med projektet var att bygga en reproducerbar ETL-pipeline som läser rådata från CSV, tvättar och transformerar data, laddar resultatet till en SQLite-databas och skapar KPI:er samt sentimentanalys på kundomdömen.

## Datakvalitet – största utmaningar

De vanligaste problemen i datan var inkonsistenta kategorier, olika datumformat och saknade värden i vissa kolumner. Dessa problem hanterades genom att skapa separata funktioner för olika typer av datatvätt, vilket gjorde koden mer strukturerad och lättare att felsöka.

## Val av NLP-metod

Sentimentanalys genomfördes med en BERT-modell via Hugging Face. Fördelen med detta är att modellen kan köras lokalt utan API-kostnader och utan risk för rate limits. Nackdelen är att modellen inte är tränad specifikt på denna typ av data, vilket kan påverka precisionen.

## Affärsnytta av KPI:er

KPI:erna ger insikter om kundnöjdhet och beteende. Till exempel kan churn-rate visa hur många kunder som avslutar sin prenumeration, medan sentimentanalysen ger en bild av hur kunder upplever produkterna och leveransen.

## Validering

Pipelinen testades även på ett separat valideringsdataset för att säkerställa att transformationerna fungerar även på ny data utan manuella ändringar.

## Förbättringar framåt

Framtida förbättringar skulle kunna vara mer avancerad felhantering, bättre hantering av edge cases samt utvärdering av sentimentmodellen mot ett manuellt märkt testdataset.

---

# Hur man kör projektet lokalt

Installera beroenden:

ETL-pipelinen kan köras via:

- Jupyter Notebook (`etl_pipeline.ipynb`)
- Python-fil (`etl_pipeline.py`)

Resultatet sparas i en lokal SQLite-databas (`matkassen.db`).

---

# Syfte med projektet

Projektet genomfördes för att:

- utveckla kunskaper i Python  
- förstå hur ETL-pipelines byggs  
- arbeta med datakvalitet och transformation  
- använda Git och GitHub i ett dataanalysprojekt  

---

# Status

Projektet är färdigt och fungerar lokalt.



“Detta används för att verifiera att datan laddats korrekt.”
sqlite3 matkassen.db "SELECT count(*) FROM matkassen_tvattad;"
sqlite3 matkassen.db "PRAGMA table_info(matkassen_tvattad);"