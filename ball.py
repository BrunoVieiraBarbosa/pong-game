import pygame, random


class Ball:
    def __init__(self) -> None:
        self.size = (5, 5)
        self.pos = self.reset_pos()
        self.direction = self.get_direction()
        self.speed = 300


    def reset_pos(self):
        return [800//2-self.size[0]//2, 600//2-self.size[1]//2]


    def get_direction(self):
        direction = [random.randint(-10, 10)/10, random.randint(-10, 10)/10]
        direction[0] = .6 if .0 <= direction[0] <= .6 else -.6 if .0 >= direction[0] >= -.6 else direction[0]
        direction[1] = .6 if .0 <= direction[1] <= .6 else -.6 if .0 >= direction[1] >= -.6 else direction[1]
        return direction


    def actions(self, delta_time):
        dist = delta_time*self.speed
        self.pos[0] += (dist * self.direction[0])
        self.pos[1] += (dist * self.direction[1])


    def collide(self, points):
        if self.pos[1] < 0: #Verifica se a posição Y é menor que o topo da tela.
            self.pos[1] = 0
            self.direction[1] *= -1 #Inverte a direção Y do bola
        elif self.pos[1]+self.size[1] > 600: #Verifica se a posição Y é maior que o limite inferior da tela.
            self.pos[1] = 600-self.size[1]
            self.direction[1] *= -1 #Inverte a direção Y do bola
        
        if self.pos[0] < 0: #Verifica se a posição X é menor que o lado esquerdo da tela.
            points[1] += 1 #Soma 1 ponto para o player 2
            self.pos = self.reset_pos() #Gera uma nova posição para a bola (Pois teve pontuação)
            self.direction = self.get_direction() #Gera uma nova direção para a bola
        elif self.pos[0] + self.size[0] > 800: #Verifica se a posição X é maior que o lado direito da tela.
            points[0] += 1 #Soma 1 ponto para o player 1
            self.pos = self.reset_pos() #Gera uma nova posição para a bola (Pois teve pontuação)
            self.direction = self.get_direction() #Gera uma nova direção para a bola


    def collide_player(self, player):
        if (self.pos[1] + self.size[1] >= player.pos[1] and
            self.pos[1] <= player.pos[1] + player.size[1] and
            self.pos[0] <= player.pos[0] + player.size[0] and
            self.pos[0] + self.size[0] >= player.pos[0]):
            self.direction[0] *= -1


    def render(self, screen):
        pygame.draw.rect(screen, (255, 255, 255), (self.pos, self.size))