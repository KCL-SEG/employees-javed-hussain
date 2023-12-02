"""Employee pay calculator."""
"""ENTER YOUR SOLUTION HERE!"""

class Employee:
    def __init__(self, name, contractLength, commissionType, wage, commission):
        self.name = name
        self.contract = contractLength
        self.commissionType = commissionType
        self.commission = commission
        self.wage = wage

    def get_pay(self):
        pay = self.wage * self.contract + self.commissionType * self.commission
        return pay

    def __str__(self):
        string = ""
        if self.contract == 1:
            string += f"{self.name} works on a monthly salary of {self.wage}"
        else:
            string += f"{self.name} works on a contract of {self.contract} hours at {self.wage}/hour"
        if self.commissionType == 1:
            string += f" and receives a bonus commission of {self.commission}."
        elif self.commissionType == 0:
            string += f"."
        else:
            string += f" and receives a commission for {self.commissionType} contract(s) at {self.commission}/contract."
        string +=  f" Their total pay is {self.get_pay()}."
        


# Billie works on a monthly salary of 4000.  Their total pay is 4000.
billie = Employee('Billie',1, 0, 4000, 0)

# Charlie works on a contract of 100 hours at 25/hour.  Their total pay is 2500.
charlie = Employee('Charlie',100, 0, 25, 0)

# Renee works on a monthly salary of 3000 and receives a commission for 4 contract(s) at 200/contract.  Their total pay is 3800.
renee = Employee('Renee',1, 4,3000, 200)

# Jan works on a contract of 150 hours at 25/hour and receives a commission for 3 contract(s) at 220/contract.  Their total pay is 4410.
jan = Employee('Jan',150,3 ,25, 220)

# Robbie works on a monthly salary of 2000 and receives a bonus commission of 1500.  Their total pay is 3500.
robbie = Employee('Robbie',1,1,2000, 1500)

# Ariel works on a contract of 120 hours at 30/hour and receives a bonus commission of 600.  Their total pay is 4200.
ariel = Employee('Ariel',120,1,30, 600)
