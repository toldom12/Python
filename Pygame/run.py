import pygame,sys
from rocket import Rocket
class Game (object) :



    def __init__(self):




        #Config
        self.tps_max = 100
        #Initialization



        pygame.init()
        self.screen = pygame.display.set_mode((1280, 720))
        self.tps_clock=pygame.time.Clock()
        self.tps_delta=0.0
        self.player = Rocket(self)

        while True :
            for event in pygame.event.get():  # pobieramy zdarzenia wszystkie jakie sie wydarzyły eventy pobieramy i zapisujemy do zmiennej event
                if event.type == pygame.QUIT:
                    sys.exit(0)
                elif event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:  # key=klawisz
                    sys.exit(0)

                    # TICKING - ZEBY fragment wykonywal sie np 20 razy na sekunde (predkosc)
                self.tps_delta += self.tps_clock.tick() / 1000.0  # zwraca delta T -czas miedzy klatkami /ile czasu zajelo nam wykonanie calej peli
            while (self.tps_delta > 1 / self.tps_max):  # co 20 s bedziemy sprawdzac czy uzytkownik nie naciska przycisko
                self.tick()
                self.tps_delta -= 1 / self.tps_max


         #Drawing

                self.screen.fill((0, 0, 0))  # czyscimy ekrean #zera ze czarny
                self.draw()
                pygame.display.flip()  # zamieniamy miejscam




    def tick (self):

        self.player.tick()


    def draw (self):
     self.player.draw()

if __name__ =="__main__" :
    Game()










