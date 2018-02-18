import csv
import random
from faker import Faker

lines=int(input('How many lines? '))
fk=Faker('pt_BR')
z=open("1.csv","a")
w=csv.writer(z)
w.writerow(('id','name','address','occupation','company','cpf','email','birthday'))
for i in range(lines):

    w.writerow((i+1,fk.name(),fk.street_address(),random.choice(['Pilot','Teacher','Fighter','Driver']),random.choice(['Apple','IBM','Google','Netflix']),fk.ssn(),fk.email(),fk.date()))
