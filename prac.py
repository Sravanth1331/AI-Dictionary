class Car:
    vehicle = "car"
    def __init__(self,name,company,color):
        self.name=name
        self.company=company
        self.color=color

C1 = Car("Verna","Hyundai","Black")
C2 = Car("ZX4","BMW","Neon")

print(C1.name)
