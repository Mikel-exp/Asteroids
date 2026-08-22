from constants import *
from circleshape import *

class Shot(CircleShape):
    #sets up constructor and inherits from the circleshape parent class
    def __init__(self, x: int, y: int):
        super().__init__(x, y, SHOT_RADIUS)
    #draws the shot
    def draw(self, screen):
        pygame.draw.circle(
            screen,
            "white",
            self.position,
            self.radius,
            LINE_WIDTH
            )

    #updates the shots position    
    def update(self, dt):
        self.position += (self.velocity*dt)
