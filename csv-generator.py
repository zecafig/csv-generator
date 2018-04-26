#!/usr/bin/env python3

import csv
import random
import datetime
import sys
from faker import Faker

fake = Faker("pt_BR")
filename = datetime.datetime.now().strftime("%Y%m%d%H%M%S")
outcsvfile = open("%s.csv" % filename, "w")
w = csv.writer(outcsvfile, dialect="excel")
listoffields = []
invalid_input = True

ftypes = (
    (
        "Name",                     # Field Name
        fake,                       # Field Generation Object
        "name",                     # Field Generation Method Name
        ()                          # Parameters
    ),
    (
        "Mother Name",
        fake,
        "name_female",
        ()
    ),
    (
        "Father Name",
        fake,
        "name_male",
        ()
    ),
    (
        "Phone Number",
        fake,
        "phone_number",
        ()
    ),
    (
        "Job",
        fake,
        "job",
        ()
    ),
    (
        "Email",
        fake,
        "safe_email",
        ()
    ),
    (
        "Birthday",
        fake,
        "date",
        ("%d/%m/%Y")
    ),
    (
        "Company",
        fake,
        "company",
        ()
    ),
    (
        "Street Name",
        fake,
        "street_name",
        ()
    ),
    (
        "City",
        fake,
        "city",
        ()
    ),
    (
        "State",
        fake,
        "state_abbr",
        ()
    ),
    (
        "CPF",
        fake,
        "cpf",
        ()
    ),
    (
        "CNPJ",
        fake,
        "cnpj",
        ()
    ),
    (
        "Social Class",
        random,
        "choice",
        (['A','B1','B2','C1','C2','DE'])
    ),
    (
        "Gender",
        random,
        "choice",
        (["Male", "Female"])
    ),
    (
        "Boolean",
        random,
        "choice",
        ([True, False])
    ),
)
   
while True:
    try:
        lines = int(input("How many lines of random data? "))
        if lines <=0:
            print("Not an option! Try again. ")
            continue    
        break
    except :
        print("Not an option! Try again. ") 
        continue

while True:
    
        selected_field = input('Choose fields to  your csv. [h - list possible fields. q - finish and generate csv. r - reset] ')

        if selected_field in ["h","?"]:
            # Help
            for i, z in enumerate(ftypes):
                print(str(i) + " - " + z[0]) 
        elif selected_field == "r":
            # Reset List
            listoffields = []
            print("List Reseted!")
        elif selected_field == "q":
            # Finish and Gen
            print("Generating CSV...")

            # CSV Header  
            h = []
            for col in listoffields:    
                h.append(ftypes[col][0])
            w.writerow(h)

            # CSV Dynamic Data In Selected Row Order
            for row in range(lines):
                r = []
                for col in listoffields:
                    if ftypes[col][3] and len(ftypes[col][3]) > 0:
                        r.append(getattr(ftypes[col][1], ftypes[col][2])(ftypes[col][3]))
                    else:
                        r.append(getattr(ftypes[col][1], ftypes[col][2])())
                
                w.writerow(r)
                #print(r)

            print("Exported file: %s.csv" % filename )
            outcsvfile.close()
            sys.exit(0)
        else:
            try:
                selected_field = int(selected_field)

                if selected_field < 0 or selected_field > len(ftypes) - 1:
                    raise Exception()

                if selected_field not in listoffields:
                    listoffields.append(selected_field)
                    print('Selected fields:')
                    print(listoffields)
                else:
                    print('Field already exists. Removing Field: %s' % selected_field)
                    listoffields.remove(selected_field)
                    print(listoffields)
            except:
                print('Invalid option! Try again. ')
                print('Selected fields:')
                print(listoffields)
