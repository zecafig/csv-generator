import csv
import random
import datetime
from faker import Faker

fk = Faker("pt_BR")
filename = datetime.datetime.now().strftime("%Y%m%d%H%M%S")
z = open("%s.csv" % filename, "w")
w = csv.writer(z)
listoffields = []
a = [0,1,2,3,4,5,6,7,8,9,10,11,12,13,14]
listoffields = []
valid = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16]
validnumfields = [0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,99]
invalid_input = True

fielddict = {
'1':'i+',
'2':'faker.name()',
'3':'fake.name_female()',
'4':'fake.name_male()',
'5':'fake.phone_number()',
'6':'fake.phone_number()',
'7':'random.choice([True, False])',
'8':'fake.job()',
'9':'fake.safe_email(*args, **kwargs)',
'10':'fake.date(pattern="%Y-%m-%d", end_datetime=None)',
'11':'fake.company()',
'12':'fake.street_name()',
'13':'fake.city()',
'14':'fake.state_abbr()',
'15': "random.choice(['A','B1','B2','C1','C2','D','E'])",
'16':'random.choice(["MALE","FEMALE"])'}

fieldlist = [
"display this information",
"id",
"name",
"mother's name",
"father's name",
"phone number",
"mobile",
"boolean",
"job",
"email",
"birthday",
"company",
"address",
"city",
"state",
"social class",
"gender"
]
   
while True:
    try:
        lines = int(input("How many lines of random data? "))
        if lines <=0:
            print("Not an option! Try again. ")
            continue    
    except ValueError:
        print("Not an option! Try again. ") 
        continue
    else:
        break    

def start():
    while True:
        try:
            numfields = int(input('Choose fields to  your csv. 0 to list possible fields. 99 to finish and generate csv.'))
        except ValueError:
            print("Not an option! Try again. ") 
            continue
        else:
            break  

    if numfields == 0:
        for i, z in enumerate(fieldlist):
            print(str(i)+" - "+z) 
        

    elif numfields != 99:
        if numfields in valid:
            if numfields not in listoffields:
                listoffields.append(numfields)
                print('Selected fields:')
                print(listoffields)
            else:
                print('Field already exists')
                print(listoffields)
                start()
        else:
            print('Not an option! Try again. ')
            print('Selected fields:')
            print(listoffields)
            start()

    else:
        print('99 fecha a lista e gera o csv com os seguintes campos:')
        print(listoffields)
        print('aqui TEM QUE PARAR E DAI vem a instrucao de gerar os dados com os campos do faker')

        # imprime o header do csv        
        # w.writerow(("email", "name", "mother", "mobile", "gender", "birthday"))

        # imprime o header do csv       
        # for i in range(lines):
        #     w.writerow((
        #     	fk.email(), 
        #     	fk.name(), 
        #     	fk.name(), 
        #         fk.phone_number(),
        #     	"male" if random.randrange(2) == 0 else "female", 
        #     	fk.date()
        #     ))

        # print("Exported file: %s.csv" % filename )
        exit()

while invalid_input:
    start()