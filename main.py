import tensorflow as tf   
tf.get_logger().setLevel('ERROR')

############################################################################################
import IA as ia
import gestion_partie as gp
from pygame import * 
import affichage as af
import pygame
from time import sleep

def main():
    plateau = gp.Plateau()
    taille = (600, 600)
    pygame.init()



    train = True
    aff_fenetre = 1
    if aff_fenetre:
        fenetre = pygame.display.set_mode(taille, pygame.RESIZABLE)
    nbr_gen=0

    while True:
        while train:
                nbr_gen+=1
                print("== Generation ",nbr_gen," ==")
                generation = ia.Generation()
                for i in range(len(generation.liste_serpent)):
                    if int(generation.liste_serpent[i].name) %25 == 0:
                        print("serpent numéro",generation.liste_serpent[i].name )
                    tour = 0
                    while tour <= plateau.tour:
                        tour +=1
                        if aff_fenetre:
                            af.affichage_partie(plateau, fenetre)
                        generation.liste_serpent[i].score = plateau.score
                        plateau.snake.direction= generation.liste_serpent[i].choose_an_action(plateau)
                        plateau.actualiser(plateau.avancer())     

                    
                print("la moyenne des serpents est:",generation.get_average())    
                
                generation.save_best_model()
        
        af.affichage_partie(plateau, fenetre)
        score = plateau.actualiser(plateau.avancer())
        
        sleep(0.4)
    
if __name__ == "__main__":
     main()