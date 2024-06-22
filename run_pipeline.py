from pipelines.training_pipeline import train_pipeline
from zenml.client import Client


if __name__ == "__main__":
    print(Client().active_stack.experiment_tracker.get_tracking_uri())
    training = train_pipeline()
    training.run()

# mlflow ui --backend-store-uri "file:/Users/mlevydaniel/Library/Application Support/zenml/local_stores/d7a64701-5796-4beb-b08c-a76c15c97a50/mlruns"
