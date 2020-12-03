# HTLANL Team 10 Python OOP
class Bill:
    def __init__(self, powerUsed):
        self.powerUsed = powerUsed
        self.cost = self.calcCost()
        self.totalCost = self.addStanding()

    def calcCost(self):
        return self.powerUsed * 12.376

    def addStanding(self):
        return self.cost + 25.00

    def displayCost(self):
        print("The cost of your bill is £{:.2f}".format(self.totalCost))


bill = Bill(10)
bill.displayCost()
