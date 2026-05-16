from fastapi import FastAPI


app = FastAPI(
    title="ShiftWatch API",
    description="ML reliability and distribution shift monitoring API.",
    version="0.1.0",
)


@app.get("/health")
def health() -> dict[str, str]:
    return {"status": "ok"}
