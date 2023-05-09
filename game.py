from ball import Ball
from player import Player
import pygame


class Game:
    def __init__(self) -> None:
        pygame.font.init() #Inicializa a fonte do pygame
        self.points = [0, 0] #Variavel que ira salvar os pontos dos jogadores
        self.font = pygame.font.SysFont("Comic Sans", 30) #Pego a fonte que desejo junto com o tamanho dela.
        self.screen = pygame.display.set_mode((800, 600))
        self.player_1 = Player()
        self.player_2 = Player('right')
        self.ball = Ball()

    
    def loop(self):
        fps = pygame.time.Clock()
        while True:
            fps.tick(60)
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    exit()
                else:
                    self.player_1.event(event)
                    self.player_2.event(event)

            self.player_1.actions(1 / max(10, fps.get_fps()))
            self.player_2.actions(1 / max(10, fps.get_fps()))
            self.ball.actions(1 / max(60, fps.get_fps()))

            self.player_1.collide() #Verifica a colisão com as paredes
            self.player_2.collide() #Verifica a colisão com as paredes
            self.ball.collide(self.points) #Verifica a colisão com as paredes

            self.ball.collide_player(self.player_1) #Verifica as colisões com o player 1
            self.ball.collide_player(self.player_2) #Verifica as colisões com o player 2

            self.render()


    def render(self):
        self.screen.fill((0, 0, 0))
        self.player_1.render(self.screen)
        self.player_2.render(self.screen)
        self.ball.render(self.screen)

        text = self.font.render(f'{self.points[0]} | {self.points[1]}', True, (255, 255, 255)) #Renderiza o texto dos pontos na cor branca e salva na variavel
        self.screen.blit(text, (800//2-text.get_rect().width//2, 10)) #Coloca na tela o que foi renderizado no meio do eixo X e a 10px de altura

        pygame.display.flip()
