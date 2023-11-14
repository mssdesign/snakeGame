import pygame
import time
import random

pygame.init()

# Definindo cores
branco = (255, 255, 255)
preto = (0, 0, 0)
vermelho = (213, 50, 80)
verde = (0, 255, 0)
azul = (50, 153, 213)

# Tamanho da tela
largura, altura = 600, 400

# Inicializando a tela
tela = pygame.display.set_mode((largura, altura))
pygame.display.set_caption('Jogo da Cobrinha')

# Velocidade e tamanho da cobra
cobra_tamanho = 10
cobra_velocidade = 15

# Fonte da mensagem
fonte = pygame.font.SysFont("bahnschrift", 25)

def pontuacao(pontos):
    valor = fonte.render("Pontos: " + str(pontos), True, azul)
    tela.blit(valor, [0, 0])

def nossa_cobra(cobra_tamanho, lista_cobra):
    for x in lista_cobra:
        pygame.draw.rect(tela, preto, [x[0], x[1], cobra_tamanho, cobra_tamanho])

def mensagem(msg, cor):
    mesg = fonte.render(msg, True, cor)
    tela.blit(mesg, [largura / 6, altura / 3])

def jogo():
    fim_de_jogo = False
    fim_de_jogo_total = False

    # Posição inicial da cobra
    x1 = largura / 2
    y1 = altura / 2

    # Variáveis de movimento
    x1_mudanca = 0
    y1_mudanca = 0

    # Lista da cobra
    lista_cobra = []
    comprimento_cobra = 1

    # Posição da comida
    comida_x = round(random.randrange(0, largura - cobra_tamanho) / 10.0) * 10.0
    comida_y = round(random.randrange(0, altura - cobra_tamanho) / 10.0) * 10.0

    while not fim_de_jogo:

        while fim_de_jogo_total == True:
            tela.fill(branco)
            mensagem("Você perdeu! Pressione Q-Sair ou C-Jogar Novamente", vermelho)
            pontuacao(comprimento_cobra - 1)
            pygame.display.update()

            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_q:
                        fim_de_jogo = True
                        fim_de_jogo_total = False
                    if event.key == pygame.K_c:
                        jogo()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                fim_de_jogo = True
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    x1_mudanca = -cobra_tamanho
                    y1_mudanca = 0
                elif event.key == pygame.K_RIGHT:
                    x1_mudanca = cobra_tamanho
                    y1_mudanca = 0
                elif event.key == pygame.K_UP:
                    y1_mudanca = -cobra_tamanho
                    x1_mudanca = 0
                elif event.key == pygame.K_DOWN:
                    y1_mudanca = cobra_tamanho
                    x1_mudanca = 0

        if x1 >= largura or x1 < 0 or y1 >= altura or y1 < 0:
            fim_de_jogo_total = True

        x1 += x1_mudanca
        y1 += y1_mudanca
        tela.fill(branco)
        pygame.draw.rect(tela, verde, [comida_x, comida_y, cobra_tamanho, cobra_tamanho])
        cabeca_cobra = []
        cabeca_cobra.append(x1)
        cabeca_cobra.append(y1)
        lista_cobra.append(cabeca_cobra)
        if len(lista_cobra) > comprimento_cobra:
            del lista_cobra[0]

        for x in lista_cobra[:-1]:
            if x == cabeca_cobra:
                fim_de_jogo_total = True

        nossa_cobra(cobra_tamanho, lista_cobra)
        pontuacao(comprimento_cobra - 1)

        pygame.display.update()

        if x1 == comida_x and y1 == comida_y:
            comida_x = round(random.randrange(0, largura - cobra_tamanho) / 10.0) * 10.0
            comida_y = round(random.randrange(0, altura - cobra_tamanho) / 10.0) * 10.0
            comprimento_cobra += 1

        clock = pygame.time.Clock()
        clock.tick(cobra_velocidade)

    pygame.quit()
    quit()

jogo()
