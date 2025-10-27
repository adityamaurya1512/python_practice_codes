

class Car:
    def __init__(self,brandName):
        self.wheels=4
        self.brandname=brandName
    def showBrandname(self):
        print(f"this is {self.brandname}")


bmw = Car("bmw")

bmw.showBrandname()
