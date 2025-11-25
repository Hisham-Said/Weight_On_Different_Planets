class Planets:
    planets:str
    weight:float
    #constructor
    def __init__(self , weight):
        self.weight = weight
    def calculate_weight(self):
        print("In Which of the following Planet you want your Weight?")
        print("1.Mercury")
        print("2.Venus")
        print("3.Mars")
        print("4.Jupiter")
        print("5.Saturn")
        print("6.Uranus")
        print("7.Neptune")
        self.planets = int(input("Enter your choice : "))
        if(self.planets==1):
            W = self.weight*(37.6/100)
            W = round(W , 2)
            print(f"Weight Mercury = {W}")
        elif(self.planets==2):
            W = self.weight*(88.9/100)
            W = round(W , 2)
            print(f"Weight Venus = {W}")
        elif(self.planets==3):
            W = self.weight*(37.8/100)
            W = round(W , 2)
            print(f"Weight Mars = {W}")
        elif(self.planets==4):
            W = self.weight*(236.0/100)
            W = round(W , 2)
            print(f"Weight Jupiter = {W}")
        elif(self.planets==5):
            W = self.weight*(108.1/100)
            W = round(W , 2)
            print(f"Weight Saturn = {W}")
        elif(self.planets==6):
            W = self.weight*(81.5/100)
            W = round(W , 2)
            print(f"Weight Uranus = {W}")
        elif(self.planets==7):
            W = self.weight*(114.0/100)
            W = round(W , 2)
            print(f"Weight Neptune = {W}")
        else:
            print(f"Invalid!")
weight  = float(input("Enter your Weight on Earth : "))
user = Planets(weight)   
user.calculate_weight()