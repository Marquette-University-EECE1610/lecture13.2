from __future__ import annotations


class Point:
    """A point in 2D space."""

    def __init__(self, init_x: float, init_y: float) -> None:
        """Store the x and y coordinates."""
        self.x = init_x
        self.y = init_y

    def __str__(self) -> str:
        """Return a readable string for a Point object."""
        # TODO: return a string such as Point(3.0, 4.0)
        return "TODO"


def main() -> None:
    p1 = Point(3.0, 4.0)
    print(p1)


if __name__ == "__main__":
    main()
