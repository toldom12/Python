#class Rodzice() :
    #    def __init__(self):
      #      print("joł joł ")

       # def parent(self):
       #     print ("rodzice rodzice ")

       # def szturchnij(self) :
      #      print ("elo elo ")

#class Dziecko(Rodzice):
      #  def _init_(self):
      #      super().__init__()
        #    print ("siemanko w 2 klasie ")
      #  def szturchnij(self ):
        #    print("joł joł ")


#dziecko=Dziecko ()

#class Pracownik() :
   # def __init__(self,imie ):
      #  self.imie =imie
     #   self.nazwisko= ("Bialek")
     #   self.but=("44")# Apteka(Pracownik):
   # def __init__(self,zawod):
   #    super().__init__("Handlarz ")
    #    self.zawod=("Aptekarz")
   #     self.zarobki=("2200 zl ")

#class Cos_Wincyj(Pracownik) :
  #  def __init__(self,rok_urodzenia ):
   #     super().__init__(rok_urodzenia)
    #    self.plec=("meszczyzna")




#print(p1.imie)


class Person () :
    def __init__(self,age,name):
        self.name=(name)
        self.surname=("Kwiatowksu")
        self.age=(age)

class Employee(Person):
    def __init__(self,position):
        super().__init__("25")
        self.position=position
        self.specialization="Python"

class Client(Person):
    def __init__(self,name):
        super().__init__(name)
        self.order ="website"

pracownik=Employee("programmer")
print(pracownik.position)
print(pracownik.age)

pracownik=Employee("designer ")
print(pracownik.position)
print(pracownik.age)

klient=Client("marta")
print(klient.name)


klient=Client("kamila")
print(klient.name)





















