import pygame

KEYS_BASE = {
        'left': {'up': pygame.K_w, 'down': pygame.K_s, 'stop': None},
        'right': {'up': pygame.K_UP, 'down': pygame.K_DOWN, 'stop': None}
    }


class Player:
    def __init__(self, player='left') -> None:
        self.side = player
        self.size = (10, 80)

        if self.side == 'left':
            self.pos = [10, 600//2-self.size[1]//2]
        else:
            self.pos = [800 - self.size[0]*2, 600//2-self.size[1]//2]

        self.keys = KEYS_BASE[self.side]
        self.speed = 300
        self.direction = ['stop']


    def event(self, event):
        if event.type == pygame.KEYDOWN:
            if self.keys['up'] == event.key:
                self.direction.insert(0, 'up')

            if self.keys['down'] == event.key:
                self.direction.insert(0, 'down')

        if event.type == pygame.KEYUP:
            if self.keys['up'] == event.key:
                self.direction.remove('up')

            if self.keys['down'] == event.key:
                self.direction.remove('down')


    def actions(self, delta_time):
        dist = delta_time*self.speed
        if self.direction[0] == 'up':
            self.pos[1] -= dist
        
        if self.direction[0] == 'down':
            self.pos[1] += dist


    def collide(self):
        if self.pos[1] < 0: #Verifica se a posição Y é menor que o topo da tela.
            self.pos[1] = 0
        elif self.pos[1]+self.size[1] > 600: #Verifica se a posição Y é maior que o limite inferior da tela.
            self.pos[1] = 600-self.size[1]


    def render(self, screen):
        pygame.draw.rect(screen, (255, 255, 255), (self.pos, self.size))
