from dataclasses import dataclass, field

from .verlet_object import VerletObject
from .constraint import Constraint


@dataclass
class VerletSolver:
    objects: list[VerletObject] = field(default_factory=list)
    constraints: list[Constraint] = field(default_factory=list)
    dt: float = 0.0

    def update(self, dt: float):
        self.dt = dt
        self.apply_gravity()
        self.apply_constraint()
        self.solve_collisions()
        self.update_positions()

    def update_positions(self):
        for obj in self.objects:
            obj.update(self.dt)

    def apply_gravity(self):
        for obj in self.objects:
            obj.accelerate(obj.properties.gravity)

    def apply_constraint(self):
        for constraint in self.constraints:
            constraint.apply(self.objects)
        # position = pygame.Vector2(WIDTH/2, HEIGHT/2)
        # for obj in self.objects:
        #     delta = obj.position - position
        #     distance = delta.length()
        #     if distance > CONSTRAINT_RADIUS - RADIUS:
        #         n = delta / distance
        #         obj.position = position + n * (CONSTRAINT_RADIUS - RADIUS)

    def add(self, object: VerletObject):
        self.objects.append(object)

    def solve_collisions(self):
        count = len(self.objects)
        for i in range(count):
            obj = self.objects[i]
            for k in range(i+1, count):
                obj2 = self.objects[k]
                collision_axis = obj.position - obj2.position
                distance = collision_axis.length
                min_distance = obj.properties.radius + obj2.properties.radius
                if distance < min_distance:
                    n = collision_axis / distance
                    delta = min_distance - distance
                    obj.position += n * obj.properties.radius / min_distance * delta
                    obj2.position -= n * obj.properties.radius / min_distance * delta
