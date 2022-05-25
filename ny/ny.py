import json

with open('stateRequirementsJSON.json') as file:
    us_dict = json.load(file)
    ny_dict = us_dict["NY"]

with open("ny/ny_requirements.json", "w") as file:
    json.dump(ny_dict, file)

# print(us_dict)