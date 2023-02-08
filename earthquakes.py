import json

infile = open("eq_data.json", "r")

earthquakes = json.load(infile)


# 1 num of earthquakes
print("The number of Earthquakes is", (len(earthquakes["features"])))
print()

# 2 new dictionary
eq_dict = {}
for earthquake in earthquakes["features"]:
    if (earthquake["properties"]["mag"]) > 6:
        eq_dict.update(
            {
                ((earthquake["properties"]["place"])): {
                    "magnitude": ((earthquake["properties"]["mag"])),
                    "longitude": ((earthquake["geometry"]["coordinates"][0])),
                    "latitude": ((earthquake["geometry"]["coordinates"][1])),
                }
            }
        )


print(eq_dict)
print()
# 3 print info

for key in eq_dict:
    print(f"Location: {key}")
    print(f"Magnitude: {eq_dict[key]['magnitude']}")
    print(f"Longitude: {eq_dict[key]['longitude']}")
    print(f"Latitude: {eq_dict[key]['latitude']}")
    print("\n")
