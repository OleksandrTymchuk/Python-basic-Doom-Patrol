import json

# with open('test.json', 'r') as f:
#     data = json.load(f)
#     print(data['menu']['value'])

data = {'test': 'test'}

with open('test1.json', 'w') as f:
    json.dump(data, f, sort_keys=True)
