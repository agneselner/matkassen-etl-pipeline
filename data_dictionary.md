# Data Dictionary – Matkassen ETL Pipeline

## Tabeller och Kolumner

### Leveranser (leveranser)
| Kolumn | Typ | Beskrivning |
|--------|-----|-------------|
| `leverans_id` | String | Unikt ID för varje leverans (ex: LEV-2024-000001) |
| `pren_id` | String | Prenumerations-ID (ex: PREN-1001) |
| `kund_id` | String | Kund-ID (ex: KUND-05001) |
| `pren_startdatum` | Datum | Startdatum för prenumeration (YYYY-MM-DD) |
| `paus_från` | Datum | Pausstart för prenumeration om applicable |
| `paus_till` | Datum | Pausslut för prenumeration om applicable |
| `pren_avslutsdatum` | Datum | Slutdatum för prenumeration om applicable |
| `leveransdatum` | Datum | Datum då matkassen leverades (YYYY-MM-DD) |
| `leveransstatus` | Kategori | Status för leverans (Levererad/Missad) |
| `kasstyp` | Kategori | Typ av matkasse (Klassisk, Familj, Vegetarisk, Snabb & Enkel, Standard) |
| `antal_portioner` | Integer | Antal portioner i matkassen (2-6) |
| `kostpreferens` | Kategori | Kostpreferens (Standard, Laktosfri, Vegetarisk, etc.) |
| `veckapris` | Float | Pris för matkassen denna vecka (SEK) |
| `postnummer` | Integer | Kundens postnummer |

### Recept (recept)
| Kolumn | Typ | Beskrivning |
|--------|-----|-------------|
| `leverans_id` | String | Referens till leverans |
| `recept_1` | String | Första receptets namn |
| `recept_2` | String | Andra receptets namn |
| `recept_3` | String | Tredje receptets namn |

### Omdömen (reviews)
| Kolumn | Typ | Beskrivning |
|--------|-----|-------------|
| `leverans_id` | String | Referens till leverans |
| `omdömesdatum` | Datum | Datum då omdöme lämnades (YYYY-MM-DD) |
| `omdömesbetyg` | Float | Betyg från kund (1–5 stjärnor) |
| `omdöme_text` | Text | Kundens fritextrecension |

## Transformeringar Tillämpade

### Datumhantering
- Alla datumkolumner standardiserades till format `YYYY-MM-DD`
- Konverterade till `datetime64` datatyp för korrekt analys
- Saknade datumvärden markeras som `NaT` (Not a Time)

### Numeriska Värden
- `veckapris` konverterad från string till float
- `antal_portioner` konverterad från string till integer
- Outliers och ogiltiga värden identifierades och markerades

### Kategoriska Värden
- `leveransstatus` validerad till endast: Levererad/Missad
- `kasstyp` standardiserad för stavning
- `kostpreferens` mappades till standardkategorier

### Saknade Värden
- Dokumenterade antal saknade värden per kolumn
- Saknade värden i `paus_från` och `paus_till` tolkas som "ingen paus"
- Saknade värden i `pren_avslutsdatum` tolkas som aktiv prenumeration
- Saknade värden i `omdöme_text` och `omdömesbetyg` tolkas som "ingen review lämnad"

### Datavalidering
- Postnummer verifierades mot giltiga svenska postnummer
- Pris validerades för rimliga värden (300-1000 SEK)
- Datumsekvenser kontrollerades (startdatum < avslutsdatum, etc.)

## Datakvalitet Sammanfattning
- **Totalt antal rader**: 2819 leveranser
- **Datumperiod**: 2024-04-05 till 2024-11-28
- **Geografisk täckning**: Sverige (baserat på postnummer)
- **Status**: Data rensad och validerad

