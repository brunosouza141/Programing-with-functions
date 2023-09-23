from math import pi
from datetime import datetime

current_date_and_time = datetime.now()
width = int(input("Enter the width of the tire in mm (ex 205): "))
ratio = int(input("Enter the aspect ratio of the tire (ex 60):"))
diameter = int(input("Enter the diameter of the wheel in inches (ex 15):"))

total = pi * int(width)**2*ratio * (width*ratio+2540*diameter) / 10000000000
print(f"The approximate volume is {total:.2f} liters")
choice = ""
while choice.lower() != "yes" or choice.lower() != "no":
    choice = input(f"""
    Width -> {width}
    Ratio -> {ratio}
    Diameter -> {diameter}
    Do you want to buy tires with the specified dimentions? (yes/no) 
    """)
    if choice.lower() == "yes":
          number = input("what is your phone number?")
          break
    elif choice.lower() == "no":
          print('Thank you!')
          break
    else:
          print('Please type YES or NO only.')
with open("volumes.txt", mode="at") as volumes:
        print(f"{current_date_and_time:%Y-%m-%d}, {width}, {ratio}, {diameter}, {total:.2f}, Phone number -> {number}" ,file=volumes)