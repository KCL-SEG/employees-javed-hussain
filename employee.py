"""Employee pay calculator."""
"""ENTER YOUR SOLUTION HERE!"""

class Employee:
    def __init__(self, name, contractLength, commissionType, wage):
        self.name = name
        self.contractType = contractType
        self.comission = commissionType
        self.wage = wage

    def get_pay(self):
        pay = self.wage * self.contractLength
        return pay

    def __str__(self):
        if self.contractLength == 1:
            return f"{self.name} works on a monthly salary of {self.wage}. Their total pay is {self.get_pay()}."
        else:
            return f"{self.name} works on a contract of {self.contractLength} at {self.wage}/hour. Their total pay is {self.get_pay()}."
        


# Billie works on a monthly salary of 4000.  Their total pay is 4000.
billie = Employee('Billie',1, 'None', 4000)

# Charlie works on a contract of 100 hours at 25/hour.  Their total pay is 2500.
charlie = Employee('Charlie',100, "", 25)

# Renee works on a monthly salary of 3000 and receives a commission for 4 contract(s) at 200/contract.  Their total pay is 3800.
renee = Employee('Renee',1,"",3000)

# Jan works on a contract of 150 hours at 25/hour and receives a commission for 3 contract(s) at 220/contract.  Their total pay is 4410.
jan = Employee('Jan',150,"",25)

# Robbie works on a monthly salary of 2000 and receives a bonus commission of 1500.  Their total pay is 3500.
robbie = Employee('Robbie',1,"",2000)

# Ariel works on a contract of 120 hours at 30/hour and receives a bonus commission of 600.  Their total pay is 4200.
ariel = Employee('Ariel',120,"",30)
