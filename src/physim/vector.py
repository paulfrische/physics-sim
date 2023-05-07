import math
from dataclasses import dataclass
from typing import Self


@dataclass
class Vector2:
    x: float = 0.0
    y: float = 0.0

    @property
    def length(self) -> float:
        return math.sqrt(self.x * self.x + self.y * self.y)

    def __add__(self, other: Self | float) -> Self:
        if isinstance(other, float):
            other = Vector2(other, other)
        return Vector2(self.x + other.x, self.y + other.y)

    def __sub__(self, other: Self | float) -> Self:
        if isinstance(other, float):
            other = Vector2(other, other)
        return Vector2(self.x - other.x, self.y - other.y)

    def __mul__(self, other: Self | float) -> Self:
        if isinstance(other, float):
            other = Vector2(other, other)
        return Vector2(self.x * other.x, self.y * other.y)

    def __truediv__(self, other: Self | float) -> Self:
        if isinstance(other, float):
            other = Vector2(other, other)
        return Vector2(self.x / other.x, self.y / other.y)