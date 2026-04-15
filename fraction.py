from __future__ import annotations


class Fraction:
    """A simple fraction with a numerator and denominator."""

    def __init__(self, numerator: int, denominator: int) -> None:
        """Store the numerator and denominator.
        Assumption for today: denominator will not be 0.
        """
        self.numerator = numerator
        self.denominator = denominator

    def __str__(self) -> str:
        """Return a readable string for a Fraction object."""
        return f"{self.numerator}/{self.denominator}"

    def double(self) -> None:
        """Mutate the Fraction to be double this one."""
        self.numerator = 2 * self.numerator


def main() -> None:
    f = Fraction(1, 3)
    print(f"before: {f}")
    f.double()
    print(f"after: {f}")

    f1 = Fraction(2, 4)
    f2 = f1
    f3 = Fraction(2, 4)

    f1.double()

    print(f"f1: {f1}")
    print(f"f2: {f2}")
    print(f"f3: {f3}")


if __name__ == "__main__":
    main()
