import numpy as np
import joblib
from pathlib import Path

PROJECT_ROOT = Path(__file__).resolve().parent.parent
MODEL_PATH = PROJECT_ROOT / "models" / "residue_model.joblib"

from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_absolute_error, mean_squared_error, r2_score

from .features import create_residue_factors


def train_residue_model(dataset):

    # Create the residue factors
    dataset, normalization_values = create_residue_factors(dataset)

    # Select model features
    features = [
        "application_rate_factor",
        "number_of_applications_factor",
        "chemical_half_life_factor",
        "phi_factor",
        "rainfall_factor",
        "temperature_factor",
        "solar_radiation_factor",
        "cuticle_thickness_factor",
        "surface_roughness_factor",
        "plant_organ_factor"
    ]

    X = dataset[features]
    y = dataset["residue_at_harvest"]

    # Split the data
    X_train, X_test, y_train, y_test = train_test_split(
        X,
        y,
        test_size=0.2,
        random_state=42
    )

    # Create and train the model
    model = LinearRegression()
    model.fit(X_train, y_train)

    # Make predictions
    predictions = model.predict(X_test)

    # Evaluate
    mae = mean_absolute_error(y_test, predictions)
    rmse = np.sqrt(mean_squared_error(y_test, predictions))
    r2 = r2_score(y_test, predictions)

    print("Linear Regression")
    print("MAE:", mae)
    print("RMSE:", rmse)
    print("R²:", r2)

    # Save the trained model
    joblib.dump(model, MODEL_PATH)

    # Save normalization values
    joblib.dump(
        normalization_values,
        "normalization_values.joblib"
    )

    return model