import json

# Transform json input to python objects
with open("../<file in>.json") as input_json:
    input_dict = json.load(input_json)

    output_dict = []
    # Filter python objects with list comprehensions
    for x in input_dict['attribs']:
        try:
            if ((x['current'] == '')
            or (isinstance(x['current'], int))
            or (x['current'].isdigit())
            or (x['current'].startswith('@{'))
            or (x['current'].startswith('(@{'))
            or (x['name'].endswith('mod'))
            or (x['name'] == 'class')
            or (x['name'] == 'race')):
                output_dict.append(x)
                continue
            if x['current'] != '':
                x['current'] = 'gibberish'
                output_dict.append(x)
        except:
            continue


    

    with open("../<file out>", 'w') as output_json:
        # Transform python object back into json
        json_dump = json.dumps(output_dict)
        # Dump json to file
        output_json.write(json_dump)