from dataclasses import dataclass, field

from .vector import Vector2


@dataclass
class PhysicsProperties:
    radius: int
    gravity: Vector2 = field(default_factory=Vector2)


@dataclass
class VerletObject:
    """This class represents a 2D ball like object.

    Attributes:
        properties: contains specific properties
        position_old: used to calculate speed/acceleration
        position: used to calculate speed/acceleration
        acceleration: the current acceleration
        dt: the delta time between the current and the last frame
    """
    properties: PhysicsProperties
    position: Vector2
    position_old: Vector2
    acceleration: Vector2
    dt: float

    @property
    def speed(self):
        return (self.position - self.position_old)

    def update(self, dt: float):
        velocity = self.position - self.position_old
        self.dt = dt
        self.position_old = self.position
        self.position = self.position + velocity + self.acceleration * dt * dt
        self.acceleration = Vector2()

    def accelerate(self, acceleration):
        self.acceleration += acceleration
