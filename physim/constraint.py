from abc import ABC, abstractmethod
from .verlet_object import VerletObject


class Constraint(ABC):
    @abstractmethod
    def apply(self, objects: list[VerletObject]):
        ...
