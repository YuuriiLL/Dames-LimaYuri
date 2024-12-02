import pygame
import sys

def bouge_bas_droite():
    global pion_pos_x, pion_pos_y
    if pion_pos_x < 9 and pion_pos_y < 9:
        pion_pos_x += 1
        pion_pos_y += 1
        dessine_case()
        screen.blit(pion, (pion_pos_x * case_size[0], pion_pos_y * case_size[1]))

def bouge_bas_gauche():
    global pion_pos_x, pion_pos_y
    if pion_pos_x > 0 and pion_pos_y < 9:
        pion_pos_x -= 1
        pion_pos_y += 1
        dessine_case()
        screen.blit(pion, (pion_pos_x * case_size[0], pion_pos_y * case_size[1]))

def bouge_haut_droite():
    global pion_pos_x, pion_pos_y
    if pion_pos_x < 9 and pion_pos_y > 0:
        pion_pos_x += 1
        pion_pos_y -= 1
        dessine_case()
        screen.blit(pion, (pion_pos_x * case_size[0], pion_pos_y * case_size[1]))

def bouge_haut_gauche():
    global pion_pos_x, pion_pos_y
    if pion_pos_x > 0 and pion_pos_y > 0:
        pion_pos_x -= 1
        pion_pos_y -= 1
        dessine_case()
        screen.blit(pion, (pion_pos_x * case_size[0], pion_pos_y * case_size[1]))

def dessine_case():
    for i in range(10):  # Boucle pour les lignes
        for a in range(10):  # Boucle pour les colonnes
            x = i * largeur_x / 10
            y = a * longeur_y / 10
            couleur = blanc if (i + a) % 2 == 0 else noir
            pygame.draw.rect(screen, couleur, (x, y, largeur_x / 10, longeur_y / 10))





pygame.init()

pion_pos_x = 0
pion_pos_y = 0

largeur_x = 600
longeur_y = 600

case_size = (largeur_x / 10, longeur_y / 10)

blanc = (176, 215, 254)
noir = (75, 124, 204)

path_to_images = "img\\MA-24_pion.png"
pion_noir = "img\\MA-24_pion_noir.png"

screen = pygame.display.set_mode((largeur_x, longeur_y))

pygame.display.set_caption("Jeux dames")
screen.fill(blanc)

dessine_case()

pion = pygame.image.load(path_to_images)
pion = pygame.transform.scale(pion, (largeur_x / 10, longeur_y / 10))
screen.blit(pion, (0, 0))

pygame.display.flip()

# Ajout d'une temporisation minimale
temps_derniere_action = 0
delai = 100

running = True
while running:
    temps_actuel = pygame.time.get_ticks()
    keys = pygame.key.get_pressed()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif temps_actuel - temps_derniere_action > delai:
            if keys[pygame.K_DOWN] and keys[pygame.K_RIGHT]:
                bouge_bas_droite()
                temps_derniere_action = temps_actuel
            elif keys[pygame.K_DOWN] and keys[pygame.K_LEFT]:
                bouge_bas_gauche()
                temps_derniere_action = temps_actuel
            elif keys[pygame.K_UP] and keys[pygame.K_RIGHT]:
                temps_derniere_action = temps_actuel
                pass
            elif keys[pygame.K_UP] and keys[pygame.K_LEFT]:
                temps_derniere_action = temps_actuel
                pass

    pygame.display.update()

pygame.quit()
sys.exit()