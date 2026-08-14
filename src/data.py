import pandas as pd

# Load data from Excel files
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

# Merge tables into a single dataset
def merge_tables(
    application_table,
    chemical_table,
    crop_table,
    weather_table,
    residue_table
):
    dataset = application_table.merge(
        chemical_table,
        on="chemical_id",
        how="left"
    )

    dataset = dataset.merge(
        crop_table,
        on="crop_id",
        how="left"
    )

    dataset = dataset.merge(
        weather_table,
        on="application_id",
        how="left"
    )

    dataset = dataset.merge(
        residue_table,
        on="application_id",
        how="left"
    )

    return dataset