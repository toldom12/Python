#imie = input ("wpisz swoję imię ")


#print(imie)

print("wybierz operacje" )
print("1. dodaj ")
print("2. odejmij  ")
print("3. Pomnóż  ")
print("4. podziel ")
print("5 . poteguj")
print("6. zwroc reszte z dzielenia ")
odpowiedz = input ("wpisz cyfre ")
num1 = int(input("wpisz 1 cyfre"))
num2 = int(input("wpisz 2 cyfre"))

if odpowiedz == 1 :
    print(num1," ,+, ",num2 ,"  = ",num1+num2)

elif odpowiedz == 2 :
    print(num1," ,-, ",num2 ,"  = ",num1-num2)
elif odpowiedz == 3 :

    print(num1," ,*, ",num2 ,"  = ",num1* num2)
elif odpowiedz == 4:

    print(num1," ,:, ",num2 ,"  = ",num1/num2)
elif odpowiedz == 5:

 #else
   # print("niepoprawny wybor ")
