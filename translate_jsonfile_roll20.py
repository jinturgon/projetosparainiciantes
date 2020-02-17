import json
from translate import Translate

filein = input("Enter the name of the JSON file (without .json)...\n")

# Transform json input to python objects
with open("../"+filein+".json", encoding="utf8") as input_json:
    input_dict = json.load(input_json)

    output_dict = []
    count = 0

    # Filter python objects with list comprehensions
    for x in input_dict['attribs']:
        if ((x['current'] == '')
        or (x['current'] == ' ')
        or (x['current'] == '?')
        or (isinstance(x['current'], int))
        or (isinstance(x['current'], float))
        or (x['current'].isdigit())
        or ((x['current'][0].isdigit() and (x['current'][0] == "d" or x['current'][1] == "d")))
        or (x['current'].startswith('@{'))
        or (x['current'].startswith('-'))
        or (x['current'].startswith('(@{'))
        or (x['current'].startswith('%{'))
        or (x['current'].startswith('{{'))
        or (x['name'].startswith('npc'))
        or (x['name'].startswith('encumberance'))
        or (x['name'].endswith('mod'))
        or (x['name'].endswith('base'))
        or (x['name'].endswith('prof'))
        or (x['name'].endswith('flag'))
        or (x['name'].endswith('bonus'))
        or (x['name'].endswith('negative'))
        or (x['name'] == 'class')
        or (x['name'] == 'version')
        or (x['name'] == 'd20')
        or (x['name'] == 'tab')
        or (x['name'] == 'dtype')
        or (x['name'] == 'l1mancer_status')
        or (x['name'] == 'race')):
            output_dict.append(x)
            continue
        count = count + 1
        # Sending text to 'Translate' and executing 'yandex_translate' function
        x['current'] = Translate(x['current']).yandex_translate()

        print(count); print(x['current'])
        output_dict.append(x)

    with open("../"+filein+"_new.json", 'w', encoding="utf8") as output_json:
        input_dict['attribs'] = output_dict
        # Transform python object back into json
        json_dump = json.dumps(input_dict)
        # Dump json to file
        output_json.write(json_dump)

print("Finished!")