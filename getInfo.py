import requests
import json
Data = []
for i in range(1,136):
    response = requests.get("http://39.97.119.9:8000/kg_api/paragraphs/?format=json&page="+str(i))
    print("第{}条数据".format(i))
    Data.append(response.json())

jsonPath = "book.json"
with open(jsonPath, 'w', encoding='utf-8') as f:
    json.dump(Data ,f, ensure_ascii=False)
