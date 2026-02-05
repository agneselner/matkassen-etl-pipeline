Matkassen – ETL-projekt

Detta är ett ETL-projekt som jag har gjort för att öva på Python, datatvätt och hur man bygger en pipeline.

Projektet handlar om data från matkassar som:
	•	läses in
	•	tvättas och struktureras
	•	sparas i en SQLite-databas

⸻

Vad projektet gör
	1.	Läser in rå data om matkassar
	2.	Rensar datan (saknade värden, datatyper m.m.)
	3.	Sparar den färdiga datan i en SQLite-databas
	4.	Använder notebooks för att kontrollera och analysera resultatet
	5. Beräknar KPI:er (kundbetyg, churn, sentiment)
6. Skapar visualiseringar för affärsinsikter

⸻

Projektstruktur

matkassen-etl-pipeline/
├── README.md
├── .gitignore
├── requirements.txt
├── matkassen-etl/
│   └── notebook/
│       ├── pipeline/
│       │   └── etl_pipeline.py
│       ├── matkassen_tvattad.ipynb
│       ├── sqlite_load.ipynb
│       ├── validation_sqlite.ipynb
│       └── kpi_features.ipynb


⸻

Har avänt mig av
	•	Python
	•	Pandas
	•	SQLite
	•	Jupyter Notebook
	•	Git och GitHub

⸻
  
SQLite-databasen innehåller rensad och transformerad data som genereras av ETL-pipelinen.



Hur man kör projektet lokalt

pip install -r requirements.txt

ETL-pipelinen kan köras via:
- Jupyter Notebook (etl_pipeline.ipynb)
- eller Python-fil (etl_pipeline.py)

Resultatet sparas i en lokal SQLite-databas (matkassen.db).


⸻


Jag gjorde detta projekt för att:
	•	bli bättre på Python
	•	förstå hur ETL-pipelines fungerar
	•	träna på att jobba med Git och GitHub

⸻

Status

Projektet är färdigt och fungerar lokalt.
