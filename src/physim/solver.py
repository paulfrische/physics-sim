from dataclasses import dataclass, field

from .verlet_object import VerletObject


@dataclass
class Solver:
    objects: list[VerletObject] = field(default_factory=list)

    def update(self, dt: float):
        self.apply_gravity()
        self.apply_constraint()
        self.solve_collisions()
        self.update_positions(dt)

    def update_positions(self, dt: float):
        for obj in self.objects:
            obj.update_position(dt)

    def apply_gravity(self):
        for obj in self.objects:
            obj.accelerate(obj.properties.gravity)

    # def apply_constraint(self):
    #     position = pygame.Vector2(WIDTH/2, HEIGHT/2)
    #     for obj in self.objects:
    #         delta = obj.position - position
    #         distance = delta.length()
    #         if distance > CONSTRAINT_RADIUS - RADIUS:
    #             n = delta / distance
    #             obj.position = position + n * (CONSTRAINT_RADIUS - RADIUS)

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
                    obj.position += obj.properties.radius / min_distance * delta * n
                    obj2.position -= obj.properties.radius / min_distance * delta * n
