import json
import pandas as pd


with open('Sensor_Data_RTH2.json') as f:
    data = json.loads(f.read())

    for i in range(len(data)):
        new_key1 = "Entity-Name"
        old_key1 = "Entity Name"
        data[i][new_key1] = data[i].pop(old_key1)

        new_key2 = "CO2"
        old_key2 = "CO2 (ppm)"
        data[i][new_key2] = data[i].pop(old_key2)

        new_key3 = "NH3"
        old_key3 = "NH3 (ppm)"
        data[i][new_key3] = data[i].pop(old_key3)

        new_key4 = "ambient_noise"
        old_key4 = "ambient_noise (dB)"
        data[i][new_key4] = data[i].pop(old_key4)

        new_key5 = "ambient_light"
        old_key5 = "ambient_light (lux)"
        data[i][new_key5] = data[i].pop(old_key5)

        new_key6 = "humidity"
        old_key6 = "humidity (%)"
        data[i][new_key6] = data[i].pop(old_key6)

        new_key7 = "temperature"
        old_key7 = "temperature (°C)"
        data[i][new_key7] = data[i].pop(old_key7)

    with open('Sensor_Data_RTH3.json', 'w') as w:
        json.dump(data, w)
