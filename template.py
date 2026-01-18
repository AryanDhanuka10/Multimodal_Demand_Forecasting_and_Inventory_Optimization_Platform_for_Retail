import os

PROJECT_NAME = "retail_demand_forecasting"

structure = [
    "data/raw",
    "data/processed",
    "data/features",
    "notebooks",
    "src/data",
    "src/models",
    "src/training",
    "src/inference",
    "src/decision_engine",
    "src/api",
    "src/utils",
    "configs",
    "logs",
    "tests",
    "docker"
]

files = [
    "src/data/load_data.py",
    "src/data/preprocess.py",
    "src/models/cnn_model.py",
    "src/models/timeseries_model.py",
    "src/models/sentiment_model.py",
    "src/models/tabular_model.py",
    "src/training/train_pipeline.py",
    "src/inference/predict.py",
    "src/decision_engine/inventory_logic.py",
    "src/api/main.py",
    "src/utils/logger.py",
    "configs/config.yaml",
    "docker/Dockerfile",
    "requirements.txt",
    "README.md"
]

def create_project():
    os.makedirs(PROJECT_NAME, exist_ok=True)
    for folder in structure:
        os.makedirs(os.path.join(PROJECT_NAME, folder), exist_ok=True)

    for file in files:
        file_path = os.path.join(PROJECT_NAME, file)
        with open(file_path, "w") as f:
            f.write("# Auto-generated file\n")

    print("Project structure created successfully.")

if __name__ == "__main__":
    create_project()
