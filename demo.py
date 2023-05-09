import sys
import physim
import pygame
import random

import settings

pygame.init()


class BoxConstraint(physim.Constraint):
    def apply(self, objects: list[physim.VerletObject]):
        for obj in objects:
            if obj.position.y > settings.HEIGHT - 20:
                obj.position.y = settings.HEIGHT - 20
            if obj.position.x > settings.WIDTH - obj.properties.radius:
                obj.position.x = settings.WIDTH - obj.properties.radius
            elif obj.position.x < obj.properties.radius:
                obj.position.x = obj.properties.radius


solver = physim.VerletSolver()
solver.constraints.append(BoxConstraint())

screen = pygame.display.set_mode((settings.WIDTH, settings.HEIGHT))
clock = pygame.time.Clock()

while True:
    screen.fill(0)
    for event in pygame.event.get():
        match event.type:
            case pygame.QUIT:
                pygame.quit()
                sys.exit(0)
            case pygame.MOUSEBUTTONDOWN:
                p = pygame.mouse.get_pos()
                solver.add(physim.construct_verlet_object(
                    physim.Vector2(p[0], p[1]), physim.Vector2(0.0, 1000.0), random.randint(10, 25)))

    for obj in solver.objects:
        pygame.draw.circle(screen, 0xffffff, (obj.position.x,
                           obj.position.y), obj.properties.radius)

    for _ in range(8):
        solver.update(1 / 120 / 8)
    pygame.display.flip()
    clock.tick(120)
