# START
# With this script I can access the key values of a
# json file and have the value types for the mapping.
import json
from django.core.files.storage import default_storage
import os

### THIS IS THE ORIGINAL VERSION COMBINED WITH THE ORIGINAL to_elastic() function ###
"""
def json_data_types(file_name):
    with default_storage.open(os.path.join('files', file_name)) as w:
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

        #print(my_dict)
        #print(result)

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

        #print(values_type)

        text = '"type"'
        form = '"format"'
        date_form = '"yyyy-MM-dd HH:mm:ss"'
        prop = '"properties"'
        mapp = '"mappings"'

        mediate_body = []
        body = []
        mm = []

        for i in range(len(result)):
            if my_dict[i] != 'Timestamp':
                t = "".join(my_dict[i])
                t1 = "".join(values_type[i])
                mm.append('"' + t + '"' + " : " + "{ " + text + " : " + '"' + t1 + '"' + " }" + ",")
            else:
                t = "".join(my_dict[i])
                t1 = "".join(values_type[i])
                mm.append('"' + t + '"' + " : " + "{ " + text + " : " + '"' + t1 + '"' + " , " + form + " : " + date_form + " }" + ",")

        t2 = "".join(mm)
        t2 = t2.rstrip(t2[-1])
        body.append(mapp + " : " + "{ " + prop + " : " + "{ " + t2 + " }" + "}")
        t3 = "".join(body)
        mediate_body.append("{ " + t3 + " }")
        # print(mediate_body)
        t4 = "".join(mediate_body)
        #print(t4)
 
    return t4
"""
# In case of testing and making changes run the script 
# autonomously by removing comments in print commands.
# END

 
#################### START SECOND APPROACH ###########################
# This version is appliable with the "bulky upload version" of a document, because when using the requests library
# and trying to apply custom mapping, the json doc must contain the data inside the 'mappings' attribute.

def json_data_types(file_name):

    with default_storage.open(os.path.join('files', file_name)) as w:
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
    return ip


#################### END SECOND APPROACH ###########################