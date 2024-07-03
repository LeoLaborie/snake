import pygame
import random as rd
from copy import deepcopy
class Plateau:
    def __init__(self):
        self.snake = Snake()
        self.liste_repetition= []
        self.pomme = []
        self.score = 0
        self.tour = 0
        self.grille = [
                    [0,0,0,0,0,0,0,0,0,0],
                    [0,0,0,0,0,0,0,0,0,0],
                    [0,0,0,0,0,0,0,0,0,0],
                    [0,0,0,0,0,0,0,0,0,0],
                    [0,0,1,2,3,0,0,0,0,0],
                    [0,0,0,0,0,0,0,0,0,0],
                    [0,0,0,0,0,0,0,0,0,0],
                    [0,0,0,0,0,0,0,0,0,0],
                    [0,0,0,0,0,0,0,0,0,0],
                    [0,0,0,0,0,0,0,0,0,0],
                ]
        self.generer_pomme()
    def restart(self):
        self.liste_repetition = []
        self.snake = Snake()
        self.score = 0
        self.tour = 0
        self.grille = [
                    [0,0,0,0,0,0,0,0,0,0],
                    [0,0,0,0,0,0,0,0,0,0],
                    [0,0,0,0,0,0,0,0,0,0],
                    [0,0,0,0,0,0,0,0,0,0],
                    [0,0,1,2,3,0,0,0,0,0],
                    [0,0,0,0,0,0,0,0,0,0],
                    [0,0,0,0,0,0,0,0,0,0],
                    [0,0,0,0,0,0,0,0,0,0],
                    [0,0,0,0,0,0,0,0,0,0],
                    [0,0,0,0,0,0,0,0,0,0],
                ]
        self.generer_pomme()
        
    def actualiser(self, retirer=None ):
        if retirer is True:
            for x,ligne in enumerate(self.grille):
                for y,colonne in enumerate(ligne):
                    if colonne not in [-1, 0]:
                        self.grille[x][y] = self.grille[x][y]-1
      
        self.grille[self.snake.get_file()[-1][0]][self.snake.get_file()[-1][1]] = len(self.snake.get_file())
        self.grille[self.pomme[0]][self.pomme[1]] = -1

        self.verifier_boucle()

        return self.score

    def verifier_boucle(self):
        grille = deepcopy(self.grille)
        """
        for ligne in self.grille:
            grille.append(ligne.copy())
        
        if self.tour == 1:
            self.liste_repetition = []
        
        grille2 = []
        for ligne in grille:
            grille2.append(ligne.copy())
            """
        if grille in self.liste_repetition:
            self.restart()
        if len(self.liste_repetition) > 100:
            self.liste_repetition.pop(0)
        self.liste_repetition.append(deepcopy(grille))
        


    def avancer(self):
        self.tour += 1
        if self.snake.direction == "droite":
            self.snake.enfiler([self.snake.file[-1][0], self.snake.file[-1][1]+1])
        elif self.snake.direction == "gauche":
            self.snake.enfiler([self.snake.file[-1][0], self.snake.file[-1][1]-1])
        elif self.snake.direction == "bas":
            self.snake.enfiler([self.snake.file[-1][0]+1, self.snake.file[-1][1]])
        elif self.snake.direction == "haut":
            self.snake.enfiler([self.snake.file[-1][0]-1, self.snake.file[-1][1]])
            
        if self.verifier_serpent_collision():
            self.restart()
            return None
        if not self.verifier_serpent_manger_pomme():
            self.snake.defiler()
            return True

    def generer_pomme(self):
        compteur = 0
        for x in range(10):
            for y in range(10):
                if self.grille[x][y] == 0:
                    compteur+=1
        case_pomme = rd.randint(0,compteur)
        compteur = 0
        for x in range(10):
            for y in range(10):
                if not ([x,y]  in self.snake.get_file() or [x,y] == self.pomme):
                    if compteur == case_pomme:
                        self.grille[x][y] = -1
                        self.pomme = [x,y]
                        return
                    compteur+=1
            


    def verifier_serpent_collision(self):

        serpent = self.snake.get_file()
        tete = serpent[-1]
        if 0>tete[0] or tete[0] > 9 or 0>tete[1]or tete[1]  > 9:
            return True
        if serpent.count(tete) > 1:
            return True
        
        return False

    def verifier_serpent_manger_pomme(self):
        tete = self.snake.get_file()[-1]
        if tete == self.pomme:
            self.score +=1
            self.generer_pomme()
            
            return True
       
        return False
    
class Snake:
    def __init__(self):
        self.file = [[4,2],[4,3],[4,4]]
        self.direction = "droite"

    def defiler(self):
        return self.file.pop(0)
    
    def enfiler(self, coo):
        self.file.append(coo)

    def get_file(self):
        return self.file