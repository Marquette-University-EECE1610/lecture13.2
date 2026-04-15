"""Lecture 3 starter: make Rectangle objects print cleanly.

Goals:
- Practice writing __str__ so print(rectangle) is readable.
- Keep computation methods separate from output.
- Continue using constructors and methods.
"""

from __future__ import annotations


class Rectangle:
    """A simple rectangle described by width and height."""

    def __init__(self, width: float, height: float) -> None:
        """Store the rectangle dimensions."""
        self.width = width
        self.height = height

    def __str__(self) -> str:
        """Return a readable string for a Rectangle object.

        Example idea:
            Rectangle(width=3.0, height=4.0)
        """
        # TODO: return a string. Do not print here.
        return "TODO"


def main() -> None:
    """Create a few rectangles and test the methods."""
    rect1 = Rectangle(3.0, 4.0)
    rect2 = Rectangle(5.5, 2.0)

    print("Testing __str__:")
    print(rect1)
    print(rect2)


if __name__ == "__main__":
    main()
