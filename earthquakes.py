"""
the eq_data file is a json file that contains detailed information about
earthquakes around the world for a period of a month.

NOTE: No hard-coding allowed except for keys for the dictionaries

1) print out the number of earthquakes


2) iterate through the dictionary and extract the location, magnitude, 
   longitude and latitude of the location and put it in a new
   dictionary, name it 'eq_dict'. We are only interested in earthquakes that have a 
   magnitude > 6. Print out the new dictionary.

3) using the eq_dict dictionary, print out the information as shown below (first three shown):

Location: Northern Mid-Atlantic Ridge
Magnitude: 6.2
Longitude: -36.0923
Latitude: 35.4364


Location: 166km SSE of Muara Siberut, Indonesia
Magnitude: 6.1
Longitude: 100.0208
Latitude: -2.8604


Location: 14km ENE of Puerto Madero, Mexico
Magnitude: 6.6
Longitude: -92.2981
Latitude: 14.7628

"""


import json

infile = open("eq_data.json", "r")

eq = json.load(infile)


# Part 1 - Print Number of Earthquakes

print("\n\n" "Number of Earthquakes: ", len(eq["features"]), "\n\n")

# Part 2 - Create new dict

eq_dict = {}
eq_dict["eq_details"] = []

for detail in eq["features"]:

    if detail["properties"]["mag"] > 6:

        eq = {}

        eq["loc"] = detail["properties"]["place"]
        eq["mag"] = detail["properties"]["mag"]
        eq["long"] = detail["geometry"]["coordinates"][0]
        eq["lat"] = detail["geometry"]["coordinates"][1]

        eq_dict["eq_details"].append(eq)


# Part 3 - Print details from new dict


for eq in eq_dict["eq_details"]:
    print("Location: ", eq["loc"])
    print("Magnitude: ", eq["mag"])
    print("Longitude: ", eq["long"])
    print("Latitude: ", eq["lat"])
    print()
    print()


"""
eqdata = {}

for eq in list_of_eqs:
   location = eq['location']

   eqdata[eq['location']] = {'mag': _____, 'lat': _____, 'lon':_____}

print(eqdata) #put the print statement outside of the for loop

"""


# create a fork, create a clone from that fork, update gitignore, push to my github repository, create virtual enviornment
# you may be required to read from the file, do something with a dictionary and spit out an output onto a file
