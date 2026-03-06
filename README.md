Matkassen – ETL-projekt

Detta projekt implementerar en komplett ETL-pipeline i Python för att läsa in, rensa, transformera och analysera data från en matkassetjänst.

Projektet fokuserar på datakvalitet, data-transformationer, lagring i databas samt analys genom KPI:er och sentimentanalys av kundrecensioner.

⸻

Projektets syfte

Syftet med projektet är att demonstrera hur en datadriven pipeline kan byggas från rådata till analysresultat.

Projektet tränar följande färdigheter:
	•	bygga en ETL-pipeline i Python
	•	arbeta med datakvalitet och datatransformation
	•	lagra data i en databas
	•	analysera data genom KPI:er och visualiseringar
	•	använda NLP (Natural Language Processing) för att analysera kundomdömen
	•	arbeta med Git och GitHub i ett dataanalysprojekt

⸻

Vad projektet gör

Pipelinen genomför följande steg:
	1.	Läser in rådata från CSV
	2.	Utför datatvätt (saknade värden, datatyper, inkonsistenta kategorier)
	3.	Skapar nya analyskolumner (feature engineering)
	4.	Genomför sentimentanalys på kundomdömen
	5.	Sparar den rensade datan i en SQLite-databas
	6.	Beräknar KPI:er och skapar visualiseringar

⸻

Tekniker och bibliotek

Projektet använder följande tekniker:
	•	Python
	•	Pandas – datahantering och transformation
	•	SQLite – lagring av transformerad data
	•	Matplotlib – visualisering av KPI:er
	•	Hugging Face Transformers – BERT-modell för sentimentanalys
	•	Jupyter Notebook – analys och visualisering
	•	Git & GitHub – versionshantering

⸻

Projektstruktur
matkassen-etl-pipeline/
│
├── matkassen-etl/
│   └── notebook/
│       │
│       ├── pipeline/
│       │   ├── etl_pipeline.py
│       │   └── etl_pipeline.ipynb
│       │
│       ├── sentiment_analys.ipynb
│       ├── kpi_features.ipynb
│       ├── sqlite_load.ipynb
│       ├── validation_sqlite.ipynb
│       │
│       ├── matkassen_data.csv
│       ├── matkassen_validation.csv
│       │
│       ├── kpi_betyg_per_kasstyp.png
│       ├── kpi_churn_andel.png
│       └── sentiment_analys.png
│
├── requirements.txt
├── data_dictionary.md
└── README.md 

ETL-pipeline

Extract

Rådata läses in från en CSV-fil med hjälp av Pandas.

En initial datautforskning (EDA) görs för att identifiera:
	•	datatyper
	•	saknade värden
	•	inkonsistenta kategorier

⸻

Transform

Flera transformationer utförs för att förbättra datakvaliteten:
	•	standardisering av kategorier
	•	hantering av saknade värden
	•	konvertering av datumformat
	•	logiska kontroller av vissa fält

Transformationerna implementeras som separata funktioner i pipelinen för att göra koden mer modulär och lättare att underhålla.

⸻

Feature Engineering

Nya analyskolumner skapas för att möjliggöra bättre analys.

Exempel:
	•	veckodag
	•	månad
	•	churn-indikator
	•	sentimentklassificering

⸻

Sentimentanalys

Sentimentanalys genomförs på kundrecensioner med en BERT-baserad modell från Hugging Face Transformers.

Recensionerna klassificeras i tre kategorier:
	•	Positiv
	•	Neutral
	•	Negativ

Resultatet används senare i analysen för att förstå kundnöjdhet och kundupplevelse.

⸻

Load

Den transformerade datan lagras i en lokal SQLite-databas.

Databasen innehåller tabeller med:
	•	rensad data
	•	valideringsdata

Detta gör att datan kan användas vidare i analyser eller andra system.

⸻

Validering

För att säkerställa att pipelinen fungerar på ny data kördes processen även på ett separat valideringsdataset.

Pipelinen hanterar samma dataproblem automatiskt utan manuella ändringar, vilket visar att transformationerna är reproducerbara.

⸻

KPI:er och analys

Flera KPI:er beräknas för att skapa affärsinsikter, exempelvis:
	•	kundbetyg per kasstyp
	•	churn-rate
	•	leveransstatus per kategori
	•	sentimentfördelning i kundrecensioner

Visualiseringar skapas med Matplotlib för att tydliggöra resultaten.

⸻

Reflektion

Datakvalitet

De största datakvalitetsproblemen i datasetet var:
	•	inkonsistenta kategorier
	•	olika datumformat
	•	saknade värden

Dessa hanterades genom att skapa separata funktioner för varje typ av datatransformation.

⸻

Val av NLP-metod

Sentimentanalysen genomfördes med en BERT-modell via Hugging Face.

Fördelar:
	•	kan köras lokalt
	•	ingen API-kostnad
	•	inga rate limits

Nackdelar:
	•	modellen är inte tränad specifikt på denna datatyp

⸻

Affärsnytta

KPI:erna ger insikter om kundbeteende och kundnöjdhet.

Exempel:
	•	churn-rate visar hur många kunder som avslutar sin prenumeration
	•	sentimentanalysen ger en bild av hur kunder upplever leveransen och produkterna

⸻

Hur man kör projektet lokalt:
Klona repot:
git clone https://github.com/agneselner/matkassen-etl-pipeline.git

Installera beroenden:
pip install -r requirements.txt

Kör ETL-pipelinen: 
python matkassen-etl/notebook/pipeline/etl_pipeline.py

Kör sentimentalanalys
Öppna och kör notebooken:
sentiment_analys.ipynb

Generera KPI-visualiseringar
Kör notebooken::
kpi_features.ipynb

Resultatet sparas i en lokal SQLite-databas (matkassen.db).

⸻

Status

Projektet är färdigt och fungerar lokalt.

