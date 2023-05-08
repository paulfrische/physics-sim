import sys
import physim
import pygame

pygame.init()


class LinkConstraint(physim.Constraint):
    def __init__(self, a: physim.VerletObject | physim.Vector2, b: physim.VerletObject | physim.Vector2, distance: float) -> None:
        self.a = a
        self.b = b
        self.distance = distance

    def apply(self, objects: list[physim.VerletObject]):
            if isinstance(self.a, physim.VerletObject) and isinstance(self.b, physim.VerletObject):
                between = self.a.position - self.b.position
                delta = self.distance - between.length
                self.a.position += between.normal / 2 * delta
                self.b.position -= between.normal / 2 * delta
            elif isinstance(self.a, physim.VerletObject) and isinstance(self.b, physim.Vector2):
                between = self.a.position - self.b
                delta = self.distance - between.length
                self.a += between.normal * delta
            elif isinstance(self.a, physim.Vector2) and isinstance(self.b, physim.VerletObject):
                between = self.a - self.b.position
                delta = self.distance - between.length
                self.b.position -= between.normal * delta


solver = physim.VerletSolver()
obj1 = physim.construct_verlet_object(physim.Vector2(200.0, 300.0), physim.Vector2(0.0, 1000.0), 15)
obj2 = physim.construct_verlet_object(physim.Vector2(100.0, 300.0), physim.Vector2(0.0, 1000.0), 15)
c1 = LinkConstraint(physim.Vector2(300.0, 300.0), obj1, 120.0)
c2 = LinkConstraint(obj1, obj2, 120.0)
solver.add(obj1)
solver.add(obj2)
solver.constraints.append(c1)
solver.constraints.append(c2)

screen = pygame.display.set_mode((600, 600))
clock = pygame.time.Clock()

while True:
    screen.fill(0)
    for event in pygame.event.get():
        match event.type:
            case pygame.QUIT:
                pygame.quit()
                sys.exit(0)

    pygame.draw.circle(screen, 0xffffff, (300.0, 300.0), 15)
    pygame.draw.line(screen, 0xffffff, (300.0, 300.0), (obj1.position.x, obj1.position.y), 10)
    pygame.draw.line(screen, 0xffffff, (obj1.position.x, obj1.position.y), (obj2.position.x, obj2.position.y), 10)
    for obj in solver.objects:
        pygame.draw.circle(screen, 0xffffff, (obj.position.x,
                           obj.position.y), obj.properties.radius)

    for _ in range(8):
        solver.update(1 / 120 / 8)

    pygame.display.flip()
    clock.tick(120)
