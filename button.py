import pygame


class button:
    """Create a button, then blit the surface in the while loop"""

    def __init__(self, text="text", position=(100, 100), font=10, bg="black", color="White", feedback="text", size=(0, 0)):
        self.x, self.y = position
        self.position = position
        self.font = pygame.font.SysFont("Arial", font)
        self.feedback = feedback
        self.change_text(text, bg)
        self.text = self.font.render(text, 1, pygame.Color(color))
        if size[0] != 0 and size[1] != 0:
            self.size = size
        else:
            self.size = self.text.get_size()
        self.surface = pygame.Surface(self.size)
        self.surface.fill(bg)
        self.surface.blit(self.text, (0, 0))
        self.rect = pygame.Rect(self.x, self.y, self.size[0], self.size[1])
        self.sizeX, self.sizeY = self.rect.size
        self.positionRD = tuple(map(lambda x, y: x + y, position, self.size))


    def change_text(self, text="newtext", bg="black", color = "White"):
        self.text = self.font.render(str(text), 1, pygame.Color(color))
        self.size = self.text.get_size()
        self.surface = pygame.Surface(self.size)
        self.surface.fill(bg)
        self.surface.blit(self.text, (0, 0))
        self.rect = pygame.Rect(self.x, self.y, self.size[0], self.size[1])
        self.sizeX, self.sizeY = self.rect.size

    def output(self, screen):
        screen.blit(self.surface, (self.x, self.y))

    def click(self, mouse, event):
        if mouse[0] > self.x and mouse[1] > self.y and mouse[0] < self.sizeX and mouse[1] < self.sizeY:
            event()