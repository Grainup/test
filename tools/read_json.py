import json
from config import con

def get_json():

    result = []
    with open(f'{con.BASE_DIR}/data/data_false.json', 'r', encoding='utf-8') as f:
        data = json.load(f)
        for key, value in data.items():
            re1 = []
            for k, v in value.items():
                re1.append(v)
            result.append(re1)
        return result


get_j = get_json()
print(get_j)