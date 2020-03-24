import json

with open("EZ_Transport.json") as file_data:
    print(file_data)
    json_data = json.load(file_data)
    print(type(json_data))

    print(json_data["transportation_types"][0]["name"])

    json_data["transportation_types"][0]["name"] = "Taxi"
    print(json.dumps(json_data["transportation_types"], indent=4))


file = open("EZ_Transport.json", "w")
file.write(json.dumps(json_data, indent=2))
file.close()
