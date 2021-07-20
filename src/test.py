from dataclasses import dataclass


@dataclass(frozen=True)
class Coord:
    x: int
    y: int
    z: int


a = Coord(1, 2, 3)
print(a)
