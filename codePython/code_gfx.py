import pygame
import sys

# Dimensions et couleurs
largeur_x = 600
longeur_y = 600
case_size = (largeur_x / 10, longeur_y / 10)
blanc = (255, 255, 255)
noir = (255,192,203)

# Chemins des images
path_to_pion_blanc = "../img/MA-24_pion.png"
path_to_pion_noir = "../img/MA-24_pion_noir.png"

# Initialiser Pygame
pygame.init()

# Création de la fenêtre de jeu
screen = pygame.display.set_mode((largeur_x, longeur_y))
pygame.display.set_caption("Jeu de dames")
screen.fill(blanc)

# Chargement et mise à l'échelle des pions
pion_blanc = pygame.image.load(path_to_pion_blanc)
pion_blanc = pygame.transform.scale(pion_blanc, (largeur_x // 10, longeur_y // 10))

pion_noir = pygame.image.load(path_to_pion_noir)
pion_noir = pygame.transform.scale(pion_noir, (largeur_x // 10, longeur_y // 10))

def dessine_case():
    """Dessine les cases du plateau de jeu."""
    for i in range(10):  # Lignes
        for a in range(10):  # Colonnes
            x = i * largeur_x / 10
            y = a * longeur_y / 10
            couleur = blanc if (i + a) % 2 == 0 else noir
            pygame.draw.rect(screen, couleur, (x, y, largeur_x / 10, longeur_y / 10))

def placer_pions():
    """Place les pions sur le plateau."""
    # Placer les pions blancs (lignes 0 à 3) sur les cases noires
    for i in range(4):
        for j in range(10):
            if (i + j) % 2 != 0:  # Placer sur les cases noires
                screen.blit(pion_blanc, (j * case_size[0], i * case_size[1]))

    # Placer les pions noirs (lignes 6 à 9) sur les cases noires
    for i in range(6, 10):
        for j in range(10):
            if (i + j) % 2 != 0:  # Placer sur les cases noires
                screen.blit(pion_noir, (j * case_size[0], i * case_size[1]))

def initialiser_gfx():
    """Initialise l'interface graphique et les ressources."""
    screen.fill(blanc)  # Réinitialise l'écran pour dessiner à nouveau les cases
    dessine_case()      # Dessine le plateau
    placer_pions()      # Place les pions sur le plateau
    pygame.display.flip()  # Met à jour l'écran

# Appel de la fonction d'initialisation
initialiser_gfx()

# Gestion de la boucle principale
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

# Quitter proprement
pygame.quit()
sys.exit()
