"""
* Name : Final Project, Vehicle Maintenance Log Application
* Author: Cabe Cullinan
* Created : 3/26/24
* Course: CIS 152 - Data Structure
* Version: 1.0
* OS: Windows 11
* IDE: PyCharm
* Copyright : This is my own original work
* based on specifications issued by our instructor
* Description : An application that acts as a log for vehicle maintenance, and future maintenance
* Academic Honesty: I attest that this is my original work.
* I have not used unauthorized source code, either modified or
* unmodified. I have not given other fellow student(s) access
* to my program.
"""
import unittest


class Maintenance:
    # maintenance class, contains the repair info to be kept in the log
    def __init__(self, date, mileage, price, part_num, description):
        self.date = date
        self.mileage = mileage
        self.price = price
        self.partNum = part_num
        self.description = description


class FutureMaintenance:
    def __init__(self, price, part_num, description, priority):
        self.price = price
        self.partNum = part_num
        self.description = description
        self.priority = priority


class Vehicle:
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year
        self.mainLog = []   # array holding current maintenance items
        self.futureLog = []   # array to hold future maintenance items

    def print_maintenance(self):
        for maintenance in self.mainLog:
            print(f"Date: {maintenance.date}  Mileage: {maintenance.mileage}  Price:{maintenance.price}$  "
                  f"Part #:{maintenance.partNum}  Description:{maintenance.description}")

    def print_future_main(self):
        for FutureMaintenance in self.futureLog:
            print(f"Price:{FutureMaintenance.price}$  Part #:{FutureMaintenance.partNum}  Description:"
                  f"{FutureMaintenance.description}  Priority:{FutureMaintenance.priority}")

    def add_maintenance(self, date, mileage, price, part_num, description):
        maintenance1 = Maintenance(date, mileage, price, part_num, description)
        self.mainLog.append(maintenance1)

    def add_future_maintenance(self, price, part_num, description, priority):
        future_main = FutureMaintenance(price, part_num, description, priority)
        self.futureLog.append(future_main)
        self.futureLog.sort(key=lambda x: x.priority)  # sorts the futureLog array based on priority variable

    def sort_mainlog(self, key='date'):
        # method for sorting the log, default sorts it by date
        key = key.lower()   # sets input to lowercase
        if key == 'date':
            self.mainLog.sort(key=lambda x: x.date)
        elif key == 'mileage':
            self.mainLog.sort(key=lambda x: x.mileage)
        elif key == 'price':
            self.mainLog.sort(key=lambda x: x.price)


# testing for accessing elements and classes

hilda = Vehicle('Mercedes', "300D", 1987)
print(hilda.make, hilda.model, hilda.year)
hilda.add_maintenance('3/26/2024', 134000, 40, 12345678, "Replaced glow plugs")
for maintenance in hilda.mainLog:
    print(f"Date: {maintenance.date}, Mileage: {maintenance.mileage}, Price: {maintenance.price},"
          f" Part#: {maintenance.partNum}, Description: {maintenance.description}")
# can also access the maintenance log items this way
print(hilda.mainLog[0].date)

# testing for future maintenance log
hilda.add_future_maintenance(250, 1234, 'New Front bumper', 3)
print('Price: ' + str(hilda.futureLog[0].price))
print('Description: ' + str(hilda.futureLog[0].description))

# testing linked list for vehicle logs
heinz = Vehicle('Mercedes', 'SL500', 1995)
ford = Vehicle('Ford', 'Ranger', 2000)


# testing priorty queue sort for future maintenance
hilda.add_future_maintenance(300, 122, 'Leather Upholstery', 1)
hilda.add_future_maintenance(50, 4445, 'Interior Trim', 2)

print(hilda.futureLog[0].priority)  # prints priority 1
print(hilda.futureLog[1].priority)  # priority 2
print(hilda.futureLog[2].priority)  # priority 3

# testing print functions of both maintenance, and future maintenance logs
hilda.add_maintenance('4/9/2024', 135000, 50, 1234, 'Changed Oil and Filter')
hilda.add_maintenance('3/29/2024', 134500, 100, 58493, 'Replaced Front Bumper')
hilda.print_maintenance()

hilda.print_future_main()
