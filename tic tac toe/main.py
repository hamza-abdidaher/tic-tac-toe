import pygame
import sys

# Initialisation de Pygame
pygame.init()

# Définition des couleurs
BLANC = (255, 255, 255)
NOIR = (0, 0, 0)
ROUGE = (255, 0, 0)
BLEU = (0, 0, 255)

# Paramètres du jeu
largeur, hauteur = 600, 600
taille_case = largeur // 3
FPS = 60

# Initialisation de l'écran
ecran = pygame.display.set_mode((largeur, hauteur))
pygame.display.set_caption("Tic Tac Toe")

# Initialisation de la police
police = pygame.font.Font(None, 36)

def afficher_message(message, couleur, y_offset=0):
    texte = police.render(message, True, couleur)
    rect = texte.get_rect(center=(largeur // 2, hauteur // 2 + y_offset))
    ecran.blit(texte, rect)

def verifier_victoire(grille):
    # Vérifier les lignes et les colonnes
    for i in range(3):
        if grille[i][0] == grille[i][1] == grille[i][2] != 0:
            return grille[i][0], [(i, 0), (i, 1), (i, 2)]
        if grille[0][i] == grille[1][i] == grille[2][i] != 0:
            return grille[0][i], [(0, i), (1, i), (2, i)]

    # Vérifier les diagonales
    if grille[0][0] == grille[1][1] == grille[2][2] != 0:
        return grille[0][0], [(0, 0), (1, 1), (2, 2)]
    if grille[0][2] == grille[1][1] == grille[2][0] != 0:
        return grille[0][2], [(0, 2), (1, 1), (2, 0)]

    return None, []

def dessiner_grille(grille):
    for i in range(1, 3):
        pygame.draw.line(ecran, NOIR, (i * taille_case, 0), (i * taille_case, hauteur), 3)
        pygame.draw.line(ecran, NOIR, (0, i * taille_case), (largeur, i * taille_case), 3)

    for i in range(3):
        for j in range(3):
            valeur = grille[i][j]
            if valeur == 1:
                pygame.draw.circle(ecran, ROUGE, (j * taille_case + taille_case // 2, i * taille_case + taille_case // 2), taille_case // 2 - 10, 3)
            elif valeur == 2:
                pygame.draw.line(ecran, BLEU, (j * taille_case + 20, i * taille_case + taille_case - 20),
                                 (j * taille_case + taille_case - 20, i * taille_case + 20), 3)

def main():
    grille = [[0, 0, 0],
              [0, 0, 0],
              [0, 0, 0]]

    joueur_actuel = 1
    tour = 0

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            if event.type == pygame.MOUSEBUTTONDOWN:
                colonne = event.pos[0] // taille_case
                ligne = event.pos[1] // taille_case

                if grille[ligne][colonne] == 0:
                    grille[ligne][colonne] = joueur_actuel
                    tour += 1

                    gagnant, positions_gagnantes = verifier_victoire(grille)
                    if gagnant is not None:
                        for position in positions_gagnantes:
                            pygame.draw.rect(ecran, BLANC, (position[1] * taille_case, position[0] * taille_case, taille_case, taille_case))
                        pygame.display.flip()
                        pygame.time.delay(1000)  # Pause d'une seconde pour l'effet visuel

                        ecran.fill(BLANC)
                        afficher_message(f"Joueur {gagnant} a gagné!", NOIR, -50)
                        pygame.display.flip()
                        pygame.time.delay(2000)  # Pause de deux secondes pour afficher le message de victoire
                        return

                    joueur_actuel = 3 - joueur_actuel  # Changer de joueur

        ecran.fill(BLANC)
        dessiner_grille(grille)

        if tour == 9:
            afficher_message("Match nul!", NOIR)
            pygame.display.flip()
            pygame.time.delay(2000)  # Pause de deux secondes pour afficher le message de match nul
            return

        pygame.display.flip()
        pygame.time.Clock().tick(FPS)

if __name__ == "__main__":
    main()
    pygame.quit()
    sys.exit()
