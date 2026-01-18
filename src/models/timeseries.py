import pandas as pd
from sklearn.metrics import mean_absolute_error
from sklearn.linear_model import LinearRegression
from pathlib import Path

FEATURES_DIR = Path("data/features")

def train_baseline():
    df = pd.read_csv(FEATURES_DIR / "timeseries_features.csv")

    X = df[["lag_1", "lag_7", "lag_14", "rolling_mean_7"]]
    y = df["sales"]

    split = int(len(df) * 0.8)
    X_train, X_test = X.iloc[:split], X.iloc[split:]
    y_train, y_test = y.iloc[:split], y.iloc[split:]

    model = LinearRegression()
    model.fit(X_train, y_train)

    preds = model.predict(X_test)
    mae = mean_absolute_error(y_test, preds)

    print(f"Baseline MAE: {mae:.2f}")

    df_test = df.iloc[split:].copy()
    df_test["prediction"] = preds
    df_test.to_csv(FEATURES_DIR / "baseline_forecast.csv", index=False)

if __name__ == "__main__":
    train_baseline()
