from pathlib import Path

import joblib
import pandas as pd
import streamlit as st


BASE_DIR = Path(__file__).resolve().parent.parent

MODEL_PATH = BASE_DIR / "models" / "residue_model.joblib"
NORMALIZATION_PATH = (
    BASE_DIR / "models" / "normalization_values.joblib"
)

# LOAD MODEL AND NORMALIZATION VALUES

model = joblib.load(MODEL_PATH)

normalization_values = joblib.load(
    NORMALIZATION_PATH
)

# CREATE RESIDUE FACTORS

def create_residue_factors(data):

    # Application rate
    app_min = normalization_values["application_rate"]["min"]
    app_max = normalization_values["application_rate"]["max"]

    data["application_rate_factor"] = (
        data["application_rate"] - app_min
    ) / (
        app_max - app_min
    )

    # Number of applications
    applications_min = (
        normalization_values["number_of_applications"]["min"]
    )
    applications_max = (
        normalization_values["number_of_applications"]["max"]
    )

    data["number_of_applications_factor"] = (
        data["number_of_applications"] - applications_min
    ) / (
        applications_max - applications_min
    )

    # Chemical half-life
    half_life_min = (
        normalization_values["soil_half_life"]["min"]
    )
    half_life_max = (
        normalization_values["soil_half_life"]["max"]
    )

    data["chemical_half_life_factor"] = (
        data["soil_half_life"] - half_life_min
    ) / (
        half_life_max - half_life_min
    )

    # PHI
    phi_min = normalization_values["phi"]["min"]
    phi_max = normalization_values["phi"]["max"]

    data["phi_factor"] = 1 - (
        (data["phi"] - phi_min)
        / (phi_max - phi_min)
    )

    # Rainfall
    rainfall_min = (
        normalization_values["total_rainfall"]["min"]
    )
    rainfall_max = (
        normalization_values["total_rainfall"]["max"]
    )

    data["rainfall_factor"] = 1 - (
        (data["total_rainfall"] - rainfall_min)
        / (rainfall_max - rainfall_min)
    )

    # Temperature
    temperature_min = (
        normalization_values["average_temperature"]["min"]
    )
    temperature_max = (
        normalization_values["average_temperature"]["max"]
    )

    data["temperature_factor"] = 1 - (
        (data["average_temperature"] - temperature_min)
        / (temperature_max - temperature_min)
    )

    # Solar radiation
    radiation_min = (
        normalization_values["solar_radiation"]["min"]
    )
    radiation_max = (
        normalization_values["solar_radiation"]["max"]
    )

    data["solar_radiation_factor"] = 1 - (
        (data["solar_radiation"] - radiation_min)
        / (radiation_max - radiation_min)
    )

    # Cuticle thickness
    cuticle_min = (
        normalization_values["cuticle_thickness"]["min"]
    )
    cuticle_max = (
        normalization_values["cuticle_thickness"]["max"]
    )

    data["cuticle_thickness_factor"] = (
        data["cuticle_thickness"] - cuticle_min
    ) / (
        cuticle_max - cuticle_min
    )

    # Surface roughness
    roughness_mapping = {
        "Low": 0.0,
        "Medium": 0.5,
        "High": 1.0
    }

    data["surface_roughness_factor"] = (
        data["surface_roughness"].map(roughness_mapping)
    )

    # Plant organ
    plant_organ_mapping = {
        "Leaf": 1.00,
        "Fruit": 0.85,
        "Stem": 0.75,
        "Seed": 0.70,
        "Grain": 0.70,
        "Bulb": 0.60,
        "Tuber": 0.55,
        "Root": 0.50
    }

    data["plant_organ_factor"] = (
        data["plant_organ_harvested"].map(
            plant_organ_mapping
        )
    )

    return data

# STREAMLIT INTERFACE

st.title("AgroSafe")

st.subheader("Pesticide Residue Prediction")

st.write(
    "Enter the pesticide application, environmental, "
    "and crop information below."
)


# USER INPUTS

application_rate = st.number_input(
    "Application Rate (kg/ha)",
    min_value=0.0,
    value=1.0
)

number_of_applications = st.number_input(
    "Number of Applications",
    min_value=1,
    value=1,
    step=1
)

soil_half_life = st.number_input(
    "Chemical Soil Half-Life (days)",
    min_value=0.0,
    value=10.0
)

phi = st.number_input(
    "Pre-Harvest Interval (days)",
    min_value=0.0,
    value=14.0
)

total_rainfall = st.number_input(
    "Total Rainfall (mm)",
    min_value=0.0,
    value=100.0
)

average_temperature = st.number_input(
    "Average Temperature (°C)",
    value=25.0
)

solar_radiation = st.number_input(
    "Solar Radiation (MJ/m²/day)",
    min_value=0.0,
    value=15.0
)

cuticle_thickness = st.number_input(
    "Cuticle Thickness (µm)",
    min_value=0.0,
    value=10.0
)

surface_roughness = st.selectbox(
    "Surface Roughness",
    ["Low", "Medium", "High"]
)

plant_organ_harvested = st.selectbox(
    "Plant Organ Harvested",
    [
        "Leaf",
        "Fruit",
        "Stem",
        "Seed",
        "Grain",
        "Bulb",
        "Tuber",
        "Root"
    ]
)


# PREDICTION

if st.button("Predict Residue"):

    input_data = pd.DataFrame({
        "application_rate": [application_rate],
        "number_of_applications": [
            number_of_applications
        ],
        "soil_half_life": [soil_half_life],
        "phi": [phi],
        "total_rainfall": [total_rainfall],
        "average_temperature": [
            average_temperature
        ],
        "solar_radiation": [
            solar_radiation
        ],
        "cuticle_thickness": [
            cuticle_thickness
        ],
        "surface_roughness": [
            surface_roughness
        ],
        "plant_organ_harvested": [
            plant_organ_harvested
        ]
    })

    # Convert raw inputs into model factors
    input_data = create_residue_factors(input_data)

    # Features expected by the model
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

    model_input = input_data[features]

    # Prediction
    prediction = model.predict(model_input)

    st.success(
        f"Predicted Residue: {prediction[0]:.4f} mg/kg"
    )