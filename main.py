import csv
import whatsapp
import sys

test_list = [
    # Add Tuples here
    # (Name:str, whatsapp.link_builder(PhoneNo:int), Class:int, Departments:str)
    ("Anjishnu",whatsapp.link_builder("8777865356"))
     ]

csvlist = whatsapp.returnDictData("form.csv", "Name", "Number")
active_list = csvlist # or test_list

# filtered = []

# for user in active_list:
#      print(user[2])
#      if user[2]==8:
#          filtered.append(user)

whatsapp.send_message(active_list, False)

