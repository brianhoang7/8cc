# Author: Brian Hoang
# Date: 11/20/2019
# Description: creates class that creates employees with name, id, salary, and email and function that takes in those 4
#as parameters to create employees in the class and in a separate dictionary

class Employee:
    #initializes class members
    def __init__(self,name,ID_number,salary,email_address):
        self.name = name
        self.ID_number = ID_number
        self.salary = salary
        self.email_address = email_address
#creates dictionary for employees
dic_employee = {}
def make_employee_dict(name, ID_number, salary, email_address):
    tally = 0
    #for loop that takes 1st member of each list and creates a class object and dictionary key with object information
    for tally in range(len(name)):
        name[tally] = Employee(ID_number[tally], salary[tally],email_address[tally])
        dic_employee[ID_number[tally]] = name[tally]
        tally+=1
    return dic_employee