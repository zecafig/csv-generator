import csv
import random
import datetime
from faker import Faker

lines = int(input("How many lines? "))

fk = Faker("pt_BR")

z = open("%s.csv" % datetime.datetime.now().strftime("%Y%m%d%H%M%S"), "w")
w = csv.writer(z)
w.writerow(("id", "name", "address", "occupation", "company", "cpf", "email", "birthday"))

for i in range(lines):
    w.writerow((
    	i+1, 
    	fk.name(), 
    	fk.street_address(), 
    	random.choice(["Pilot", "Teacher", "Fighter", "Driver"]), 
    	random.choice(["Apple", "IBM", "Google", "Netflix"]), 
    	fk.ssn(), 
    	fk.email(), 
    	fk.date()
    ))