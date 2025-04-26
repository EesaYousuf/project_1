# Rent Calculators
# work_flow of project
""" -->inputs we need from the user
    -->total rent
    -->total food ordered for snacking
    -->Electricity units spend
    -->charge per unit
    -->persons living in room /flat
  """
# output
""" -->total amount you have to pay is"""
# first take inputs from user
rent=int(input("Enter your hostel/flat rent:"))
food=int(input("Enter the amount of food ordered:"))
electricity_spend=int(input("Enter the total of electricty speed:"))
charge_per_unit=int(input("Enter the charge per unit:"))
persons=int(input("Enter the number of persons living in room/flat:"))
# logical part
total_bill=electricity_spend*charge_per_unit
output=(food + rent + total_bill )//persons
print("each person will pay ",output)


