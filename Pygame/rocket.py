import pygame
from pygame.math import Vector2
class Rocket(object) :
    def __init__(self,game):


     self.game=game
     self.speed = 1.2
     self.gravity = 0.5
     size = self.game.screen.get_size()
     self.pos=Vector2(size[0]/2,size[1]/2) #pozycja naszej rakiety
     self.vel=Vector2(0,0) #predkosc aktualna
     self.acc=Vector2(0,0) #przyspieszenie

     size = self.game.screen.get_size()
    #zwraca nam tuple z wartosciami x,y [obiekt jest na srodku ]

    def add_force(self,force ):  #dodajemy sile do przyspieszenia
        self.acc += force



    def tick(self):
        #
        pressed = pygame.key.get_pressed() #pobieramy liste wcisnietych przyciskow
        if pressed[pygame.K_s]:
            self.add_force(Vector2(0,self.speed))
        if pressed[pygame.K_w]:
            self.add_force(Vector2(0,-self.speed))
        if pressed[pygame.K_a]:
            self.add_force(Vector2(-self.speed, 0))
        if pressed[pygame.K_d]:
            self.add_force(Vector2(self.speed, 0))


        #PHYSICS
        self.vel *=0.8     #opor powietrza trzeba uwzglednic
        self.vel -=Vector2(0,-self.gravity) # grawitacja wynosi teraz tyle samo co klawisz W
        self.vel += self.acc
        self.pos += self.vel
        self.acc *= 0

    def draw(self):
        #Base Triangle //podstawowy trojkat
        points = [Vector2(0,-10),Vector2(5,5),Vector2(-5,5)] # rysujemy trojkat
        #rotate points  obracamy katy
        angle =self.vel.angle_to(Vector2(0,1)) #podaj kat miedzy wektore predkosci a katem 0,1
        print(angle)
        points = [p.rotate(angle) for p in points ] #obraca nasza rakiete
        #Fix y axis

        points = [Vector2(p.x,p.y*-1)for p in points ]

        #Add current Position  dodaj obecna pozycje
        points=[(self.pos+p*2) for p in points ] #do kazdego punktu dajemy pozycje w liscie punktow
        pygame.draw.polygon(self.game.screen, (0, 100, 255), points)


        #rect=pygame.Rect(self.pos.x, self.pos.y, 50, 50)#rysujemy kwadrat
        #pygame.draw.rect(self.game.screen, (0, 150, 255), rect)  # 1 #rysujemy kwadrat
