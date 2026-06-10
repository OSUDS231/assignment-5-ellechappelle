import pandas as pd

def parse_line(line):
    clean_line = line.strip()
    fields = clean_line.split('|')
    for i in range(4):
        fields[i] = float(fields[i])
    return fields

def add_to_dict(parsed_line, data_dict):
    if len(parsed_line) != len(data_dict):
        raise ValueError("number of fields does not match dictionary keys.")

    keys = list(data_dict.keys())

    for i in range(len(parsed_line)):
        data_dict[keys[i]].append(parsed_line[i])

def load_data(filename):
    data_dict = {
        "sepal_length": [],
        "sepal_width": [],
        "petal_length": [],
        "petal_width": [],
        "species": [],
    }

    with open(filename, "r") as f:
        lines = f.readlines()
        for line in lines:
            if line.strip() != "":
                parsed_line = parse_line(line)
                add_to_dict(parsed_line, data_dict)

    return pd.DataFrame(data_dict)



def species_mean(data, species, measurement):
    filtered_data = data[data["species"] == species]
    return filtered_data[measurement].mean()

df = load_data("iris.txt")
print(type(species_mean(df, "Iris-setosa", "sepal_length")))
print(species_mean(df, "Iris-versicolor", "petal_length"))
print(species_mean(df, "Iris-virginica", "petal_width"))