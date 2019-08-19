class Sim:
  

    def __init__(self,name,sex,age,initial_money):
        self.name=name
        self.sex=sex
        self.age=age
        self.initial_money=initial_money
    
    def sayhello(self):
        print('Hello I am '+ self.name)

    def purchase(self, purchase, cost):
        print("I am going to buy a "+ purchase +"That cost: "+ str(cost))


Duke=Sim("Duke",'Male',40,400)
Duke.sayhello()


Lara=Sim('Lara','Female',21,210)


Lara.purchase('Bag',20)


print(Duke.initial_money)