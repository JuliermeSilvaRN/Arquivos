import pygame
import random

# Iniciando o pygame
pygame.init()
# Titulo da tela do jogo
pygame.display.set_caption('Snake')

# Variaveis
# Definindo tamanho da tela
largura, altura = 800, 600
# Colocar as variaveis dentro de uma tupla
tela = pygame.display.set_mode((largura, altura))
# Variavel para controlar o tempo
relogio = pygame.time.Clock()

# Cores no padrão RBG (Quanto de Vermelho, Verde e Azul na cor)
preta = (0, 0, 0)
branca = (255, 255, 255)
vermelha = (255, 0, 0)
verde = (0, 255, 0)
# azul = (0, 0, 255)

# Parâmetros da cobrinha
tamanho_quadrado = 20
velocidade_atualizacao = 15

def gerar_comida():
    # Gera uma posição aleatoria dividido pelo tamanho da cobra para a comida
    # ficar no mesmo alinhamento da cobra
    comida_x = round(random.randrange(0, largura - tamanho_quadrado) / float(tamanho_quadrado)) * float(tamanho_quadrado)
    comida_y = round(random.randrange(0, altura - tamanho_quadrado) / float(tamanho_quadrado)) * float(tamanho_quadrado)
    return comida_x, comida_y

def desenhar_comida(tamanho, comida_x, comida_y):
    # Desenhando a comida na cor verde
    pygame.draw.rect(tela, verde, [comida_x, comida_y, tamanho, tamanho]) 
    
def desenhar_cobra(tamanho, pixels):
    for pixel in pixels:
        pygame.draw.rect(tela, branca, [pixel[0],pixel[1], tamanho,tamanho])
        
def desenhar_pontuacao(pontuacao):
    # Definindo a fonte e tamanho
    fonte = pygame.font.SysFont("Arial", 30)
    texto = fonte.render(f'Pontos: {pontuacao}', True, vermelha)
    # Inserir o texto na tela e posicionando
    tela.blit(texto, [1,1])
    
def selecionar_velocidade(tecla):
    if tecla == pygame.K_DOWN:
        velocidade_x = 0
        velocidade_y = tamanho_quadrado
    elif tecla == pygame.K_UP:
        velocidade_x = 0
        velocidade_y = - tamanho_quadrado
    elif tecla == pygame.K_RIGHT:
        velocidade_x = tamanho_quadrado
        velocidade_y = 0
    elif tecla == pygame.K_LEFT:
        velocidade_x = - tamanho_quadrado
        velocidade_y = 0
    return velocidade_x, velocidade_y

def rodar_jogo():
    fim_jogo = False
    
    # Variaveis iniciais do jogo
    # Posição inicial 
    x = largura / 2
    y = largura / 2
    # Velocidade inicial
    velocidade_x = 0
    velocidade_y = 0
    
    tamanho_cobra = 1
    # Cobra começa como uma lista vazia
    pixels = []
    
    comida_x, comida_y = gerar_comida()
    
    # Criar um loop de jogo
    while not fim_jogo:
        # Tela preenchida com a cor preta
        tela.fill(preta)
        
        # Pegar interação do teclado ou mouse do usuario
        for evento in pygame.event.get():
            # Se clicar no x da tela fecha o jogo
            if evento.type == pygame.QUIT:
                fim_jogo = True
            # Senão clicar no x, pegar a tecla apertada no teclado
            elif evento.type == pygame.KEYDOWN:
                velocidade_x, velocidade_y = selecionar_velocidade(evento.key)
                
        # Desenhar os objetos do jogo na tela
        # Comida
        desenhar_comida(tamanho_quadrado, comida_x, comida_y)
        # Pontuação
        desenhar_pontuacao(tamanho_cobra-1)
        
        # Se a cobra toca nas bordas fim de jogo
        if x < 0 or x >= largura or y < 0 or y >= altura:
            fim_jogo = True
            
        # Atualizar a posição da cobra
        x += velocidade_x
        y += velocidade_y
        
        # Movimentação da cobra
        pixels.append([x, y])
        # Se o tamanho da lista for maior que o tamanho da cobra
        if len(pixels) > tamanho_cobra:
            # Deletar o primeiro elemento da lista
            del pixels[0]
            
        # Verificar se a cobra bateu nela mesma, fim do jogo
        for pixel in pixels[:-1]:
            if pixel == [x, y]:
                fim_jogo = True
        
        # Desenhando a cobra
        desenhar_cobra(tamanho_quadrado, pixels)
        
        # Atualizando a tela do jogo
        pygame.display.update()
        
        # Criar uma nova comida
        # Se a cobra tiver a mesma posição de x e y da comida
        if x == comida_x and y == comida_y:
            # Almentar a cobra em um quadrado
            tamanho_cobra +=1
            # Gerar uma nova comida aleatoriamente
            comida_x, comida_y = gerar_comida()
            
        relogio.tick(velocidade_atualizacao)
            
rodar_jogo()