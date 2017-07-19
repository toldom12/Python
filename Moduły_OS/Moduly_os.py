import os

#for  kat in os.listdir(".") :
  #  if os.path.isfile(kat) :
   #  print("katalog  {} jest plikiem " .format(kat))
   # else :
   #  print("katalog  {} nie jest plikiem  ".format(kat))
  #  if os.path.isdir(kat) :
    #    print("{} jest folderem".format(kat) )
#print(lista)

#os.mkdir("lambo")

#os.rename("lambo","ferrari")
#os.remove("sd")

#os.rmdir("ferrari")
#os.remove("adam1")


path = "pliki/01/dane.txt"
#os.makedirs(path)
#open("dane.txt","w").close()
#print(path)
#print(os.path.dirname(path))
#print(os.path.basename(path))
#print(os.path.abspath(path))

dir_name= os.path.dirname(path)
os.makedirs(dir_name)
open(path ,"w").close()


