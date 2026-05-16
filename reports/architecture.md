# ShiftWatch Architecture

## System Flow

```text
Public mobility data
    -> ingestion
    -> cleaning and aggregation
    -> zone-time feature engineering
    -> forecasting, drift detection, and anomaly detection
    -> reliability engine
    -> FastAPI endpoints
    -> Streamlit dashboard
```

## MVP Modules

| Layer | Responsibility |
| --- | --- |
| `src/shiftwatch/ingestion` | Load raw public trip data from local files or public URLs. |
| `src/shiftwatch/etl` | Clean invalid records, parse timestamps, and aggregate trips. |
| `src/shiftwatch/features` | Build lag, rolling, calendar, and zone-level features. |
| `src/shiftwatch/models` | Forecast demand, score anomalies, and compute drift metrics. |
| `src/shiftwatch/engine` | Combine model outputs into reliability status and alert summaries. |
| `api` | Serve forecast, drift, anomaly, regime, and reliability outputs. |
| `dashboard` | Present monitoring outputs through a user-facing dashboard. |

## Initial Data Contract

The first processed dataset should be one row per pickup zone and time window:

| Column | Description |
| --- | --- |
| `timestamp` | Start of the aggregation window. |
| `pickup_zone_id` | Taxi pickup zone identifier. |
| `demand_count` | Number of trips in the window. |
| `avg_trip_distance` | Average trip distance for trips in the window. |
| `avg_fare_amount` | Average fare amount for trips in the window. |
| `hour` | Hour of day. |
| `day_of_week` | Day of week. |
| `is_weekend` | Weekend indicator. |

## Phase 1 Target

The next milestone is a reproducible script that reads one month of NYC taxi data and writes a processed Parquet file to `data/processed/`.
