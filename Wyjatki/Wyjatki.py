
try :
    plik =open("test.txt ","w")
    plik.read("Y")
    plik.close()

except FileNotFoundError as e :

    print("plik nie istnieje ")
    print(e)
except Exception as  e:
   print("nieznany blad ")
   print(e)

except IndentationError as e :
    print("lipa ")
    print(e)