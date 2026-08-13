import pandas as pd


def load_data(data_path):
    chemical_table = pd.read_excel(
        data_path / "chemical_features.xlsx"
    )

    crop_table = pd.read_excel(
        data_path / "crop_features.xlsx"
    )

    application_table = pd.read_excel(
        data_path / "application_features.xlsx"
    )

    weather_table = pd.read_excel(
        data_path / "weather_features.xlsx"
    )

    residue_table = pd.read_excel(
        data_path / "residue_features.xlsx"
    )

    return (
        chemical_table,
        crop_table,
        application_table,
        weather_table,
        residue_table
    )