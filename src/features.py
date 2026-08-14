def create_residue_factors(dataset):
#Calculate the residue factors based on the application rate
    dataset["application_rate_factor"] = (
    dataset["application_rate"] - dataset["application_rate"].min()
) / (
    dataset["application_rate"].max()
    - dataset["application_rate"].min()
)
#Calculate the residue factors based on the number of applications
    dataset["number_of_applications_factor"] = (
    dataset["number_of_applications"]
    - dataset["number_of_applications"].min()
) / (
    dataset["number_of_applications"].max()
    - dataset["number_of_applications"].min()
)
#Calculate the residue factors based on the soil half-life
    dataset["chemical_half_life_factor"] = (
    dataset["soil_half_life"] - dataset["soil_half_life"].min()
) / (
    dataset["soil_half_life"].max()
    - dataset["soil_half_life"].min()
)
#Calculate the residue factors based on the PHI
    dataset["phi_factor"] = 1 - (
    (dataset["phi"] - dataset["phi"].min())
    / (dataset["phi"].max() - dataset["phi"].min())
)

#Calculate the residue factors based on the total rainfall
    dataset["rainfall_factor"] = 1 - (
    (dataset["total_rainfall"] - dataset["total_rainfall"].min())
    / (
        dataset["total_rainfall"].max()
        - dataset["total_rainfall"].min()
    )
)

#Calculate the residue factors based on the average temperature
    dataset["temperature_factor"] = 1 - (
    (dataset["average_temperature"] - dataset["average_temperature"].min())
    / (
        dataset["average_temperature"].max()
        - dataset["average_temperature"].min()
    )
)

#Calculate the residue factors based on the solar radiation
    dataset["solar_radiation_factor"] = 1 - (
    (dataset["solar_radiation"] - dataset["solar_radiation"].min())
    / (
        dataset["solar_radiation"].max()
        - dataset["solar_radiation"].min()
    )
)
    return dataset
