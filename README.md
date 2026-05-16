# ShiftWatch

ShiftWatch is an ML reliability and distribution shift monitoring platform for urban mobility forecasting. It detects when current demand patterns move away from the historical baseline, surfaces demand anomalies, and estimates when a forecasting model may be less trustworthy.

The first version focuses on public NYC taxi data. The project will aggregate trip records into zone-time demand features, build forecasting baselines, compute drift and anomaly scores, and expose the results through a FastAPI backend and an interactive dashboard.

## Why This Project Exists

Forecasting models can keep producing predictions even when the real world has changed. In urban mobility, demand can shift because of holidays, weather, events, airport disruption, public transit issues, and long-term changes in commuting behavior.

ShiftWatch asks a production-style question:

> Should we still trust this forecast under the current data environment?

## Planned MVP

- Ingest a small slice of public NYC taxi trip data.
- Clean trips and aggregate demand by pickup zone and time window.
- Build a seasonal naive forecasting baseline.
- Compute forecast residual anomaly scores.
- Compare rolling windows against a baseline period with drift metrics.
- Combine drift, uncertainty, error, and anomaly signals into a reliability score.
- Serve dashboard-ready outputs through FastAPI.
- Build a Streamlit dashboard with forecast, drift, anomaly, and reliability views.

## Repository Layout

```text
data/
  raw/                 # local raw data, ignored by Git
  processed/           # local processed data, ignored by Git
  samples/             # small shareable samples when useful
notebooks/             # exploratory analysis
src/shiftwatch/        # core Python package
  ingestion/           # data loading
  etl/                 # cleaning and aggregation
  features/            # feature engineering
  models/              # forecasting, drift, anomaly, regime modules
  engine/              # monitoring and reliability logic
  utils/               # shared config and helpers
api/                   # FastAPI app and routes
dashboard/             # Streamlit dashboard
reports/               # architecture, methodology, and results notes
tests/                 # pytest suite
Plan/                  # project plan source and PDF
```

## Setup

```bash
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```

## Current Status

Phase 0 is in progress: project structure, configuration, documentation, and architecture notes are being established. The next milestone is Phase 1: ingesting and cleaning the first public mobility dataset.

## Data Source

The recommended first dataset is NYC Taxi and Limousine Commission trip record data. The first development pass should use a small monthly slice so the pipeline stays fast and easy to debug.
