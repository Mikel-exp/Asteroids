from circleshape import *
from constants import *
from logger import *
import random
class Asteroid(CircleShape):

    def __init__(self, x: float, y: float, radius: float) -> None:
        super().__init__(x, y, radius)

    def draw(self, screen):
        pygame.draw.circle(
            screen,
            "white",
            self.position,
            self.radius,
            LINE_WIDTH
            )
    def update(self, dt):
        self.position += (self.velocity*dt)
    
    def split(self):
        self.kill()
        if self.radius <= ASTEROID_MIN_RADIUS:
            return
        else:
            log_event("asteroid_split")
            random_angle = random.uniform(20, 50)
            asteroid_angle_1 = self.velocity.rotate(random_angle)
            asteroid_angle_2 = (self.velocity.rotate(-random_angle))
            new_radius = self.radius - ASTEROID_MIN_RADIUS
            asteroid_1 = Asteroid(self.position.x, self.position.y, new_radius)
            asteroid_1.velocity = asteroid_angle_1 * 1.2
            asteroid_2 = Asteroid(self.position.x, self.position.y, new_radius)
            asteroid_2.velocity = asteroid_angle_2 * 1.2

