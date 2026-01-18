from fastapi import FastAPI

app = FastAPI(title="Retail Demand Forecasting API")

@app.get("/")
def health_check():
    return {"status": "API running"}
