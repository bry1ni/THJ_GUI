import pygame

CARD_SIZE = (146, 300)

paddingTop = 100
paddingLeft = 150
board = [['back', 'back', 'back', 'back', 'back'],
         ['BEWD', 'CybD', 'DM', 'EHNeos', 'REBD']]

screen = pygame.display.set_mode((1000, 633))
pygame.display.set_caption("YOGIOH ! THJ")
screen.fill((0, 0, 0))

back = pygame.image.load('Cards/back.png').convert_alpha()
BEWD = pygame.image.load('Cards/BEWD.png').convert_alpha()
CybD = pygame.image.load('Cards/CybD.png').convert_alpha()
DM = pygame.image.load('Cards/DM.png').convert_alpha()
EHNeos = pygame.image.load('Cards/EHNeos.png').convert_alpha()
REBD = pygame.image.load('Cards/REBD.png').convert_alpha()

cards = [back, BEWD, CybD, DM, EHNeos, REBD]

images = {
    'back': back,
    'BEWD': BEWD,
    'CybD': CybD,
    'DM': DM,
    'EHNeos': EHNeos,
    'REBD': REBD
}

screenWallPaper = pygame.image.load('screenWP.png').convert_alpha()

done = False

choosenCard = None

card_rects = [pygame.Rect((j * CARD_SIZE[0], i * CARD_SIZE[1]), CARD_SIZE) for i in
              range(len(board)) for j in range(len(board[i]))]

while not done:

    for event in pygame.event.get():
        if event.type == pygame.QUIT or (event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE):
            done = True
            pygame.quit()

        if event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1:
                for num, cardRect in enumerate(card_rects):
                    if cardRect.collidepoint(event.pos):
                        choosenCard = num

    screen.blit(screenWallPaper, (0, 0))
    for i in range(len(board)):
        for j in range(len(board[i])):
            screen.blit(images[board[i][j]], (j * CARD_SIZE[0] + paddingLeft, i * CARD_SIZE[1] + paddingTop))

    if choosenCard is not None:
        pygame.draw.rect(screen, (0, 255, 0), card_rects[choosenCard], 3)

    pygame.display.update()
    pygame.display.flip()
