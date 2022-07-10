# A different version that can be used when a csv is separated by ; in a single column
# A good example would be Sensor_Data_RTH1.csv file, located in sample_files folder.
import pandas as pd

# Instead of a semicolon, if the csv file is structured in such a way
# a comma can also be used as a separator.
csv_data = pd.read_csv("sample.csv", sep=";")
csv_data.to_json("sample.json", orient="records")
