def create_residue_factors(dataset):

    normalization_values = {
        "application_rate": {
            "min": dataset["application_rate"].min(),
            "max": dataset["application_rate"].max()
        },

        "number_of_applications": {
            "min": dataset["number_of_applications"].min(),
            "max": dataset["number_of_applications"].max()
        },

        "soil_half_life": {
            "min": dataset["soil_half_life"].min(),
            "max": dataset["soil_half_life"].max()
        },

        "phi": {
            "min": dataset["phi"].min(),
            "max": dataset["phi"].max()
        },

        "total_rainfall": {
            "min": dataset["total_rainfall"].min(),
            "max": dataset["total_rainfall"].max()
        },

        "average_temperature": {
            "min": dataset["average_temperature"].min(),
            "max": dataset["average_temperature"].max()
        },

        "solar_radiation": {
            "min": dataset["solar_radiation"].min(),
            "max": dataset["solar_radiation"].max()
        },

        "cuticle_thickness": {
            "min": dataset["cuticle_thickness"].min(),
            "max": dataset["cuticle_thickness"].max()
        }
    }


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


# Calculate the residue factor based on cuticle thickness

    dataset["cuticle_thickness_factor"] = (
        dataset["cuticle_thickness"] - dataset["cuticle_thickness"].min()
    ) / (
        dataset["cuticle_thickness"].max()
        - dataset["cuticle_thickness"].min()
    )

# Calculate the residue factor based on surface roughness

    roughness_mapping = {
        "Low": 0.0,
        "Medium": 0.5,
        "High": 1.0
    }

    dataset["surface_roughness_factor"] = (
        dataset["surface_roughness"].map(roughness_mapping)
)

 # Calculate the residue factor based on plant organ

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

    dataset["plant_organ_factor"] = (
        dataset["plant_organ_harvested"].map(plant_organ_mapping)
    )
    return dataset, normalization_values