"""Lecture 3 starter: return a new Point from a method.

Goals:
- Practice writing __str__.
- Practice returning a new object instead of changing the old one.
- Trace what self, parameters, and the returned object refer to.
"""

from __future__ import annotations


class Point:
    """A point in 2D space."""

    def __init__(self, init_x: float, init_y: float) -> None:
        self.x = init_x
        self.y = init_y

    def __str__(self) -> str:
        return f"Point({self.x}, {self.y})"

    def halfway(self, target: Point) -> Point:
        mid_x = (self.x + target.x) / 2
        mid_y = (self.y + target.y) / 2
        return Point(mid_x, mid_y)


def main() -> None:
    """Try midpoint on a few points."""
    p1 = Point(3.0, 4.0)
    print("original p1:", p1)

    p2 = Point(5.0, 12.0)
    print("original p2:", p2)

    mid = p1.halfway(p2)
    print("midpoint:", mid)


if __name__ == "__main__":
    main()
