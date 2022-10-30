# START
# With this script I can access the key values of a
# json file and have the value types for the mapping.
import json

def trial():

    with open('Sensor_Data_RTH3.json') as w:
        data = json.loads(w.read())
        keys = data[0].keys()
        # print(keys)
        my_dict = []
        for i in keys:
            my_dict.append(i)

        values_dict = []
        result = []
        for j in range(len(my_dict)):
            temp = my_dict[j]
            values_dict = data[j][temp]
            result.append(values_dict)

        print(my_dict)
        # print(result)

        values_type = []
        for t in range(len(result)):
            if my_dict[t] != 'Timestamp':
                if type(result[t]) == int:
                    values_type.append('long')
                    # print("Int Here")
                elif type(result[t]) == float:
                    values_type.append('double')
                    # print("Float Here")
                elif type(result[t]) == str:
                    values_type.append('keyword')
                    # print("String Here")
                else:
                    values_type.append(False)
                    # print(False)
            else:
                values_type.append('date')
                # print("Date Here")

        print(values_type)

        people = dict()
        ipeople = dict()
        for i in range(len(my_dict)):
            if my_dict[i] != 'Timestamp':
                people[my_dict[i]] = {'type': values_type[i]}
            else:
                people[my_dict[i]] = {'type': values_type[i], "format": "yyyy-MM-dd HH:mm:ss"}

        new_people = ['properties', 'mappings']
        for i in range(len(new_people) - 1):
            ipeople[new_people[i + 1]] = {new_people[i]: people}

            ip = ipeople['mappings']
            print(ip)


trial()
# json_data_types()
