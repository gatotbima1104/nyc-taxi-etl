# NYC Taxi ETL Pipeline

An automated ETL pipeline for NYC Yellow Taxi trip data that extracts raw records from public sources, performs data cleansing and validation, and generates clean datasets, invalid-record reports, and pipeline execution logs.

## Workflow

```text
Extract → Transform → Validate → Load → Report
````

## Features

* Extract NYC Taxi trip data
* Extract taxi zone lookup data
* Data cleaning and validation
* Generate valid and invalid datasets
* Generate ETL report

## Project Structure

```text
.
├── data/
├── etl/
│   ├── extract.py
│   ├── transform.py
│   └── load.py
├── utils/
├── logs/
├── reports/
├── app.py
├── script_entrypoint.sh
├── Dockerfile
├── docker-compose.yml
└── requirements.txt
```

## Data Source

NYC Taxi & Limousine Commission (TLC)

https://www.nyc.gov/site/tlc/about/tlc-trip-record-data.page

## Requirements

- Python 3.13+

- Docker

## Clone Repository

```bash
git clone https://github.com/gatotbima1104/nyc-taxi-etl.git
cd nyc-taxi-etl
```

## Environment Setup

Create a `.env` file from the example template:

```bash
cp .env.example .env
```

Open the `.env` file and configure the dataset URL:

```env
TAXI_DATA_URL=https://d37ci6vzurychx.cloudfront.net/trip-data/yellow_tripdata_2026-01.parquet
```

> **Note:** You can replace the URL with any available NYC Yellow Taxi dataset file if you want to process data from a different month.

## Run Locally on MacOS

Make venv environment:

```bash
python3 -m venv venv
source venv/bin/activate
```

Install dependencies:

```bash
pip install -r requirements.txt
```

Run pipeline:

```bash
python3 app.py
```

## Run with Docker

Start:

```bash
docker compose up
```

View logs:

```bash
docker compose logs -f
```

Stop:

```bash
docker compose down
```

## Environment Variables

```yaml
TAXI_DATA_URL=https://d37ci6vzurychx.cloudfront.net/trip-data/yellow_tripdata_2026-01.parquet

TAXI_ZONE_LOOKUP_URL=https://d37ci6vzurychx.cloudfront.net/misc/taxi_zone_lookup.csv
```

## Output

```text
data/transformed/
└── transformed_yellow_tripdata_2026_01.csv

data/mart/valid/
└── valid_yellow_tripdata_2026_01.csv

data/mart/invalid/
└── invalid_yellow_tripdata_2026_01.csv

reports/
└── report.json
```

### Example Terminal Report

```text
==================================================
DATA QUALITY REPORT

Dataset Summary
---------------
Total Records      : 3,724,889
Valid Records      : 3,555,245 (95.45%)
Invalid Records    :   169,644 (4.55%)

Invalid Record Breakdown
------------------------
Duration Invalid   : 45,070
Distance Invalid   : 125,738

Pipeline
--------
Execution Time     : 63.49s

==================================================
```

### Example JSON Report

```json
{
    "timestamp": "2026-06-14T09:20:30.136673",
    "total_records": 3724889,
    "valid_records": 3555245,
    "invalid_records": {
        "total": 169644,
        "invalid_duration": 45070,
        "invalid_distance": 125738
    },
    "execution_time_seconds": 63.49
}
```

## Tech Stack

* Python
* Pandas
* Docker
