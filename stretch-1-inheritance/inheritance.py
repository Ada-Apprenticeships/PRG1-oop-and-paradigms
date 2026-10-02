"""
Optional stretch. One class built on top of another.

An ElectricBay is a Bay that also knows about a charger. Everything
a Bay can do, an ElectricBay can do, without any of it being
written twice.
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


class ElectricBay(Bay):
    def __init__(self, number, size, kilowatts):
        super().__init__(number, size)
        self.kilowatts = kilowatts
        self.charging = False

    def park(self, registration):
        parked = super().park(registration)
        if parked:
            self.charging = True
        return parked

    def describe(self):
        base = super().describe()
        if self.charging:
            return f"{base}  [charging at {self.kilowatts} kW]"
        return f"{base}  [{self.kilowatts} kW charger, idle]"


ordinary = Bay(1, "standard")
electric = ElectricBay(2, "standard", 22)

print(ordinary.describe())
print(electric.describe())

ordinary.park("AB12 CDE")
electric.park("XY99 ZZZ")

print(ordinary.describe())
print(electric.describe())

print(electric.is_free())
print(isinstance(electric, Bay))
