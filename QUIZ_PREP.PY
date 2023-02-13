"""""
Process the JSON file named school_data.json. Display only those schools 
that are part of the ACC, Big 12, Big Ten, Pac-12 and SEC divisons. This
information can be found in the ValueLabels file.

Copy that info here:

"NCAA/NAIA conference number football (IC2020)","372","American Athletic Conference"
"NCAA/NAIA conference number football (IC2020)","108","Big Twelve Conference"
"NCAA/NAIA conference number football (IC2020)","107","Big Ten Conference"
"NCAA/NAIA conference number football (IC2020)","130","Southeastern Conference"


Display report for all universities that have a graduation rate for Women over 80%
Display report for all universities that have a total price for in-state students living off campus over $50,000
"""

import json

infile = open("school_data.json", "r")
outfile = open("This_is_a_test.json", "w")
schools = json.load(infile)


outfile.write("This For loop is for women grad rate over 80 percent.")
outfile.write("\n")
outfile.write(f"The number of schools is {len(schools)}")

# for loop
conference = [372, 108, 107, 130]

for school in schools:
    if school["NCAA"]["NAIA conference number football (IC2020)"] in conference:
        if school["Graduation rate  women (DRVGR2020)"] > 80:
            outfile.write("\n")
            outfile.write(str(school["instnm"]))

outfile.write("\n")
outfile.write("This For loop is for universities w/ price over 50k.")
outfile.write("\n")

for school in schools:
    if school["NCAA"]["NAIA conference number football (IC2020)"] in conference:
        if school[
            "Total price for in-state students living on campus 2020-21 (DRVIC2020)"
        ]:
            outfile.write("\n")
            outfile.write(str(school["instnm"]))
