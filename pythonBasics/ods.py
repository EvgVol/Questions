import pandas as pd

# Создаём данные для примера: информация о животных
data = {
    "Animal": ["Tiger", "Elephant", "Penguin", "Kangaroo", "Panda"],
    "Habitat": ["Forest", "Savannah", "Antarctica", "Australia", "Mountains"],
    "Diet": ["Carnivore", "Herbivore", "Carnivore", "Herbivore", "Herbivore"],
    "Average Lifespan (years)": [15, 60, 20, 12, 20],
    "Conservation Status": ["Endangered", "Vulnerable", "Near Threatened", "Least Concern", "Vulnerable"]
}

# Создаём DataFrame
df = pd.DataFrame(data)

# Сохраняем данные в формате ODS
file_path = "/mnt/data/animals_data.ods"
df.to_excel(file_path, index=False, engine="odf")

file_path
