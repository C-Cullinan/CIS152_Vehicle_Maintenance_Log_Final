"""
* Name : Final Project, Vehicle Maintenance Log Application
* Author: Cabe Cullinan
* Created : 3/26/24
* Course: CIS 152 - Data Structure
* Version: 2.0
* OS: Windows 11
* IDE: PyCharm
* Copyright : This is my own original work
* based on specifications issued by our instructor
* Description : An application that acts as a log for vehicle maintenance, and future maintenance, including GUI
* Academic Honesty: I attest that this is my original work.
* I have not used unauthorized source code, either modified or
* unmodified. I have not given other fellow student(s) access
* to my program.
"""
import tkinter as tk
from tkinter import ttk


# linked list methods/classes, will be used to track vehicles added to the log, and have a method to print L list
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None

    def append(self, data):
        new_node = Node(data)
        if self.head is None:  # if no head, set this data as head
            self.head = new_node
            return
        last_node = self.head
        while last_node.next:  # locate the last item in linked list
            last_node = last_node.next
        last_node.next = new_node  # point 2nd to last item to the last item, being added

    def print_list(self):
        current_node = self.head
        while current_node:
            print(f"Make: {current_node.data.make} Model: {current_node.data.model} Year: {current_node.data.year}")
            current_node = current_node.next
# end of linked list methods


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
    def __init__(self):
        self.mainLog = []   # array holding current maintenance items
        self.futureLog = []   # array to hold future maintenance items

    def add_vehicle(self):
        make = make_input.get()
        model = model_input.get()
        year = year_input.get()
        # writing to log text box
        vehicle_text.config(state='normal')
        vehicle_text.delete('1.0', tk.END)
        # title for vehicle text box
        if make and model and year:
            # all text fields filled, then
            self.mainLog.append([make, model, year])
            for entry in self.mainLog:
                vehicle_text.insert(tk.END, f"{entry[0]} | {entry[1]} | {entry[2]} \n")
        else:
            vehicle_text.insert(tk.END, "All fields must contain text!")
        vehicle_text.config(state='disabled')

    def print_maintenance(self):
        for maintenance in self.mainLog:
            print(f"Date: {maintenance.date}  Mileage: {maintenance.mileage}  Price:{maintenance.price}$  "
                  f"Part #:{maintenance.partNum}  Description:{maintenance.description}")

    def print_future_main(self):
        for FutureMaintenance in self.futureLog:
            print(f"Price:{FutureMaintenance.price}$  Part #:{FutureMaintenance.partNum}  Description:"
                  f"{FutureMaintenance.description}  Priority:{FutureMaintenance.priority}")

    def add_future_maintenance_for_vehicle(self):
        make = c_make_input.get().lower()
        model = c_model_input.get().lower()
        year = c_year_input.get()

        price = fmPri_inp.get()  # Get price from input box
        part_num = fmPN_inp.get()  # Get part number from input box
        description = fmDe_inp.get()  # Get description from input box
        priority = fmPr_inp.get()  # Get priority from input box

        # Find the specified vehicle
        for vehicle in self.mainLog:
            if vehicle[0].lower() == make and vehicle[1].lower() == model and vehicle[2] == year:
                # Create a new future maintenance entry
                future_maintenance_entry = FutureMaintenance(price, part_num, description, priority)
                # Ensure that the vehicle list contains the future maintenance list
                if len(vehicle) < 4:
                    vehicle.append([])
                if len(vehicle) < 5:
                    vehicle.append([])  # Append an empty future maintenance list if not present
                # Append the new future maintenance entry to the vehicle's future maintenance list
                vehicle[4].append(future_maintenance_entry)
                # Display the added future maintenance and existing future maintenance for the vehicle
                self.check_viewMaint()
                return  # Exit the loop after finding the specified vehicle
            else:
                # Vehicle not found in the log
                FutmainT.config(state='normal')
                FutmainT.delete('1.0', tk.END)
                FutmainT.insert(tk.END, "Vehicle not found in log. Cannot add future maintenance.")
                FutmainT.config(state='disabled')

    def sort_mainlog(self, key='date'):
        # method for sorting the log, default sorts it by date
        key = key.lower()   # sets input to lowercase
        if key == 'date':
            self.mainLog.sort(key=lambda x: x.date)
        elif key == 'mileage':
            self.mainLog.sort(key=lambda x: x.mileage)
        elif key == 'price':
            self.mainLog.sort(key=lambda x: x.price)

    def check_viewMaint(self):
        make = c_make_input.get().lower()
        model = c_model_input.get().lower()
        year = c_year_input.get()
        match = False
        for vehicle in self.mainLog:
            if vehicle[0].lower() == make and vehicle[1].lower() == model and vehicle[2] == year:
                match = True
                break
        mainT.config(state='normal')
        FutmainT.config(state='normal')
        if len(vehicle) < 4:
            vehicle.append([])
        if len(vehicle) < 5:
            vehicle.append([])
        if match:
            mainT.delete('1.0', tk.END)
            FutmainT.delete('1.0', tk.END)
            # Print existing data in the specified vehicle's mainLog
            for entry in self.mainLog:
                if entry[0].lower() == make and entry[1].lower() == model and entry[2] == year:
                    mainT.delete('1.0', tk.END)
                    mainT.insert(tk.END, "Date\tMileage\tPrice\tPart#\tDescription\n")
                    mainT.insert(tk.END, "---------------------------------------------------------\n")

                    FutmainT.delete('1.0', tk.END)
                    FutmainT.insert(tk.END, "Price\tPart#\tDescription\tPriority\n")
                    FutmainT.insert(tk.END, "---------------------------------------------------------\n")
                    for maintenance in entry[3]:  # entry[3] contains the list of Maintenance instances
                        mainT.insert(tk.END, f"{maintenance.date}\t{maintenance.mileage}\t{maintenance.price}\t"
                        f"{maintenance.partNum}\t{maintenance.description}\n")

                    future_maintenance_entries = sorted(entry[4], key=lambda x: x.priority)
                    # above implements the sort of the priority queue, before printing items to futmainT text widget
                    for futmaintenance in future_maintenance_entries:
                        FutmainT.insert(tk.END,
                                        f"{futmaintenance.price}\t{futmaintenance.partNum}\t"
                                        f"{futmaintenance.description}\t{futmaintenance.priority}\n")
        else:
            mainT.delete('1.0', tk.END)
            mainT.insert(tk.END, "Vehicle not found in log.")
            FutmainT.delete('1.0', tk.END)
            FutmainT.insert(tk.END, "Vehicle not found in log.")
        mainT.config(state='disabled')
        FutmainT.config(state='disabled')

    def add_maintenance_for_vehicle(self):
        make = c_make_input.get().lower()
        model = c_model_input.get().lower()
        year = c_year_input.get()

        date = date_input.get()  # Get date from input box
        mileage = mileage_input.get()  # Get mileage from input box
        price = price_input.get()  # Get price from input box
        part_num = part_num_input.get()  # Get part number from input box
        description = description_input.get()  # Get description from input box

        # Find the specified vehicle
        for vehicle in self.mainLog:
            if vehicle[0].lower() == make and vehicle[1].lower() == model and vehicle[2] == year:
                # Create a new maintenance entry
                maintenance_entry = Maintenance(date, mileage, price, part_num, description)
                # Ensure that the vehicle list contains the maintenance list
                if len(vehicle) < 4:
                    vehicle.append([])  # Append an empty maintenance list if not present
                # Append the new maintenance entry to the vehicle's maintenance list
                vehicle[3].append(maintenance_entry)
                # Display the added maintenance and existing maintenance for the vehicle
                self.check_viewMaint()
                # self.display_vehicle_maintenance(vehicle)
                return  # Exit the loop after finding the specified vehicle
            else:
                # Vehicle not found in the log
                mainT.config(state='normal')
                mainT.delete('1.0', tk.END)
                mainT.insert(tk.END, "Vehicle not found in log. Cannot add maintenance.")
                mainT.config(state='disabled')

    def sort_by_price(self):
        # this works like a selection sort, searching for the smallest element in the array, and then putting that eleme
        # ment to the first position in the array, and so on until the entire array is sorted.
        make = c_make_input.get().lower()
        model = c_model_input.get().lower()
        year = c_year_input.get()

        for vehicle in self.mainLog:
            if vehicle[0].lower() == make and vehicle[1].lower() == model and vehicle[2] == year:
                if len(vehicle) > 3:  # Ensure maintenance list exists
                    vehicle[3].sort(key=lambda x: float(x.price))  # Sort by converting price to float
        self.check_viewMaint()

    def sort_by_mile(self):
        # this works like a selection sort, searching for the smallest element in the array, and then putting that eleme
        # ment to the first position in the array, and so on until the entire array is sorted.
        make = c_make_input.get().lower()
        model = c_model_input.get().lower()
        year = c_year_input.get()

        for vehicle in self.mainLog:
            if vehicle[0].lower() == make and vehicle[1].lower() == model and vehicle[2] == year:
                n = len(vehicle[3])
                for i in range(n):
                    min_index = i
                    for j in range(i + 1, n):
                        if vehicle[3][j].mileage < vehicle[3][min_index].mileage:
                            min_index = j
                    vehicle[3][i], vehicle[3][min_index] = vehicle[3][min_index], vehicle[3][i]
        self.check_viewMaint()

    def sort_by_date(self):
        # this works like a selection sort, searching for the smallest element in the array, and then putting that eleme
        # ment to the first position in the array, and so on until the entire array is sorted.
        make = c_make_input.get().lower()
        model = c_model_input.get().lower()
        year = c_year_input.get()

        for vehicle in self.mainLog:
            if vehicle[0].lower() == make and vehicle[1].lower() == model and vehicle[2] == year:
                n = len(vehicle[3])
                for i in range(n):
                    min_index = i
                    for j in range(i + 1, n):
                        if vehicle[3][j].date < vehicle[3][min_index].date:
                            min_index = j
                    vehicle[3][i], vehicle[3][min_index] = vehicle[3][min_index], vehicle[3][i]
        self.check_viewMaint()



root = tk.Tk()
# application title
root.title("Vehicle Maintenance Log")

# label and input for Vehicle Make
make_label = ttk.Label(root, text="Make")
make_label.grid(row=1, column=3)
make_input = ttk.Entry(root)
make_input.grid(row=2, column=3)

# label and input for Vehicle Model
model_label = ttk.Label(root, text="Model")
model_label.grid(row=1, column=4)
model_input = ttk.Entry(root)
model_input.grid(row=2, column=4)

# label and input for Vehicle Year
year_label = ttk.Label(root, text="Year")
year_label.grid(row=1, column=5)
year_input = ttk.Entry(root)
year_input.grid(row=2, column=5)

vlog_label = ttk.Label(root, text="Vehicle's")
vlog_label.config(font=("TkDefaultFont", 14))
vlog_label.grid(row=0, column=3, columnspan=3)

# text widget containing vehicles
vehicle_text = tk.Text(root, height=10, width=30)
vehicle_text.config(state='disabled')
vehicle_text.grid(row=3, column=3, columnspan=3)

# button to add vehicle info to log
veh_obj = Vehicle()
addV_button = ttk.Button(root, text="Add Vehicle", command=veh_obj.add_vehicle)
addV_button.grid(row=2, column=6)

"""
Above contains everything for vehicle Log text box and input fields/button
"""

# labels and input for user selecting what vehicle's maintenance log to display
input_label = ttk.Label(root, text='Input Desired Vehicle:')
input_label.grid(row=6, column=2)

c_make_label = ttk.Label(root, text='Make')
c_make_label.grid(row=5, column=3)
c_make_input = ttk.Entry(root)
c_make_input.grid(row=6, column=3)

c_model_label = ttk.Label(root, text='Model')
c_model_label.grid(row=5, column=4)
c_model_input = ttk.Entry(root)
c_model_input.grid(row=6, column=4)

c_year_label = ttk.Label(root, text='Year')
c_year_label.grid(row=5, column=5)
c_year_input = ttk.Entry(root)
c_year_input.grid(row=6, column=5)

mlog_label = ttk.Label(root, text='Maintenance')
mlog_label.config(font=("TkDefaultFont", 14))
mlog_label.grid(row=4, column=1, columnspan=3)

# text widget for maintenance items
mainT = tk.Text(root, height=10)
mainT.config(state='disabled')
mainT.grid(row=7, column=1, columnspan=3)

# button to view maintenance log
view_maint = ttk.Button(root, text='View Maintenance', command=veh_obj.check_viewMaint)
view_maint.grid(row=6, column=6)

# Adding input boxes for maintenance details
date_label = ttk.Label(root, text="Date")
date_label.grid(row=8, column=1)
date_input = ttk.Entry(root)
date_input.grid(row=9, column=1)

mileage_label = ttk.Label(root, text="Mileage")
mileage_label.grid(row=8, column=2)
mileage_input = ttk.Entry(root)
mileage_input.grid(row=9, column=2)

price_label = ttk.Label(root, text="Price")
price_label.grid(row=8, column=3)
price_input = ttk.Entry(root)
price_input.grid(row=9, column=3)

part_num_label = ttk.Label(root, text="Part Number")
part_num_label.grid(row=10, column=1)
part_num_input = ttk.Entry(root)
part_num_input.grid(row=11, column=1)

description_label = ttk.Label(root, text="Description")
description_label.grid(row=10, column=2)
description_input = ttk.Entry(root)
description_input.grid(row=11, column=2)

# Button to add maintenance
add_maintenance_button = ttk.Button(root, text="Add Maintenance", command=veh_obj.add_maintenance_for_vehicle)
add_maintenance_button.grid(row=11, column=3)

"""
Above is for maintenance log and adding new data
now adding GUI for future maintenance log and adding new data
will share same vehicle selection input and button GUI, but different input boxxes
"""

fmlog_label = ttk.Label(root, text='Future Maintenance')
fmlog_label.config(font=("TkDefaultFont", 14))
fmlog_label.grid(row=4, column=5, columnspan=3)

FutmainT = tk.Text(root, height=10)
FutmainT.config(state='disabled')
FutmainT.grid(row=7, column=5, columnspan=3)

# price
fmPri_label = ttk.Label(root, text='Price')
fmPri_label.grid(row=8, column=5)
fmPri_inp = ttk.Entry(root)
fmPri_inp.grid(row=9, column=5)

# part#
fmPN_label = ttk.Label(root, text='Part#')
fmPN_label.grid(row=8, column=6)
fmPN_inp = ttk.Entry(root)
fmPN_inp.grid(row=9, column=6)

# description
fmDe_label = ttk.Label(root, text='Description')
fmDe_label.grid(row=8, column=7)
fmDe_inp = ttk.Entry(root)
fmDe_inp.grid(row=9, column=7)

# priority
fmPr_label = ttk.Label(root, text='Priority')
fmPr_label.grid(row=10, column=5)
fmPr_inp = ttk.Entry(root)
fmPr_inp.grid(row=11, column=5)

# button to add future maintenance
futureMain_button = ttk.Button(root, text="Add Future Maintenance", command=veh_obj.add_future_maintenance_for_vehicle)
futureMain_button.grid(row=11, column=6)

# sorting maintenance log buttons
dateSortbut = ttk.Button(root, text="Sort by Date", command=veh_obj.sort_by_date)
dateSortbut.grid(row=6, column=0)

mileSortbut = ttk.Button(root, text="Sort by Mileage", command=veh_obj.sort_by_mile)
mileSortbut.grid(row=7, column=0)

priceSortbut = ttk.Button(root, text="Sort by Price", command=veh_obj.sort_by_price)
priceSortbut.grid(row=8, column=0)

# to run
root.mainloop()
