"""
Two bays, one class.

The same class as activity 1, used twice. The interesting part is
what each object knows, and what the word self is actually doing.
"""


class Bay:
    def __init__(self, number, size):
        self.number = number
        self.size = size
        self.registration = None

    def is_free(self):
        return self.registration is None

    def park(self, registration):
        if self.registration is None:
            self.registration = registration
            return True
        return False

    def describe(self):
        if self.registration is None:
            return f"Bay {self.number} ({self.size}): free"
        return f"Bay {self.number} ({self.size}): {self.registration}"


first = Bay(1, "standard")
second = Bay(2, "accessible")

print(first.describe())
print(second.describe())

first.park("AB12 CDE")

print(first.describe())
print(second.describe())

print(first.is_free())
print(second.is_free())

print(first.number, second.number)

third = second
third.park("XY99 ZZZ")
print(third.describe())
print(second.describe())
