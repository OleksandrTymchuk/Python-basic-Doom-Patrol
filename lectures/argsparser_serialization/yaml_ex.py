import yaml

with open('test.yml', 'r', newline='') as f:
    text = yaml.safe_load(f)
    print(text[0]['martin']['skills'])
