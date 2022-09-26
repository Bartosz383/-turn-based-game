import pygame, sys
from settings import *
# from debug import debug

class Game:
    def __init__(self):

        # general setup
        pygame.init()
        self.screen = pygame.display.set_mode((WIDTH, HEIGTH))
        # Game name Title
        pygame.display.set_caption('Bastion')
        self.clock = pygame.time.Clock()

    def run(self):
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()

            self.screen.fill('black')
            # debug('Test msg :)')
            pygame.display.update()
            self.clock.tick(FPS)

if __name__ == "__main__":
    game = Game()
    game.run()


class Pet:
    def __init__(self, name, type, lvl):
        self.name = name
        self.type = type
        self.lvl = lvl

    def show(self):
        print(f"I am {self.name} and my type is {self.type}")

class PetWater(Pet):
    def getLvl(self):
        return self.lvl

    def attack(self):
        print("I attack you")

class PetFire(Pet):
    def getLvl(self):
        return self.lvl

    def attack(self):
        print("I burn you")

class CharactersPets:
    def __init__(self, maxPets):
        self.maxPets = maxPets
        self.pets = []

    def addPet(self, pet):
        if len(self.pets) < self.maxPets:
            self.pets.append(pet)
            return True
        return False

    def getAverageLvl(self):
        value = 0
        for pets in self.pets:
            value += pets.getLvl()

        return value / len(self.pets)



def menu():
    a = 1
    while a:
        command = input('''
                Menu
    Wpisz 'imie' by wyświetlić imie
    Wpisz 'nazwisko' by wyświetlić nazwisko             
    Wpisz 'wyjście' żeby wyjsć
            
    ''')

    match command:
        case "imie":
            imie()
        case "nazwisko":
            nazwisko()
        case "wyjście":
            a = 0
        case other:
            print("Nie wiem o co chodzi")


def imie():
    print("moje imie to Paweł")

def nazwisko():
    print("Moje nazwisko to Kwiatkowski")



