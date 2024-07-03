import pygame
import sys
def affichage_partie(plateau, fenetre):
    
    fenetre.fill((0,0,0))

    for x in range(10):
        for y in range(10):
                #if plateau.grille[y][x] == 1:
                #    pygame.draw.rect(fenetre, (50,50,50), pygame.Rect(x*60, y*60, 60, 60))
                if plateau.grille[y][x] not in [-1, 0]:
                    pygame.draw.rect(fenetre, (50,250,50), pygame.Rect(x*60, y*60, 60, 60))
                elif plateau.grille[y][x] == -1:
                    pygame.draw.rect(fenetre, (250,50,50), pygame.Rect(x*60, y*60, 60, 60))

    for event in pygame.event.get():
                if event.type == pygame.QUIT : # si on veut fermer la fenêtre
                    sys.exit()
    pygame.display.flip()
