#!/usr/bin/env python3

import csv
import random
import datetime
from faker import Faker

lines = int(input("How many lines? "))

fk = Faker("pt_BR")

filename = datetime.datetime.now().strftime("%Y%m%d%H%M%S")

z = open("%s.csv" % filename, "w")
w = csv.writer(z)
w.writerow(("email", "name", "mother", "mobile", "gender", "birthday"))

for i in range(lines):
    w.writerow((
    	fk.email(), 
    	fk.name(), 
    	fk.name(), 
        fk.phone_number(),
    	"male" if random.randrange(2) == 0 else "female", 
    	fk.date()
    ))

print("Exported file: %s.csv" % filename )
