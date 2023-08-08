# converting from cel to fah in degrees
temp = 37
fah = (temp* 9/5) + 32

print(temp, "degrees celsius is equal to ", fah, "fahranheit")
#using encapsulation in python in employee infor.

class employee:
    def __init__(self, name,salary):
        self._name = name  
        self._salary = salary  

    def Name(self):
        return self._name

    def Salary(self):
        return self._salary

    def Raise(self, amount):
        self._salary += amount

employee = employee("ochieng devote", 850000)

print(employee.Name())
print(employee.Salary())
employee.Raise(150000)
print("the new salary is ",employee.Salary())

