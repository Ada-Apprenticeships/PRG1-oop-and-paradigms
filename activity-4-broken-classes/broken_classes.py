"""
Three things below are wrong. Nothing crashes.

Three small classes, each with one fault. Every output looks like
an output a working program would produce.
"""


# ---------- 1 ----------

class Waitlist:
    waiting = []

    def __init__(self, name):
        self.name = name

    def add(self, registration):
        self.waiting.append(registration)

    def size(self):
        return len(self.waiting)


north = Waitlist("North entrance")
south = Waitlist("South entrance")

north.add("AB12 CDE")
north.add("XY99 ZZZ")
south.add("LM34 NOP")

print(f"North waiting: {north.size()}")
print(f"South waiting: {south.size()}")


# ---------- 2 ----------

class Barrier:
    def __init__(self):
        self.is_open = False

    def open_barrier(self):
        is_open = True

    def status(self):
        if self.is_open:
            return "open"
        return "closed"


barrier = Barrier()
print("---")
print(f"Barrier starts {barrier.status()}")
barrier.open_barrier()
print(f"After opening, barrier is {barrier.status()}")


# ---------- 3 ----------

class Permit:
    def __init__(self, registration, zone):
        self.registration = registration
        self.zone = zone


issued = [Permit("AB12 CDE", "A"), Permit("XY99 ZZZ", "B")]


def has_permit(issued, registration, zone):
    """Return True if a permit has been issued for that car in that zone."""
    return Permit(registration, zone) in issued


print("---")
print(f"AB12 CDE in zone A? {has_permit(issued, 'AB12 CDE', 'A')}")
print(f"QQ11 QQQ in zone A? {has_permit(issued, 'QQ11 QQQ', 'A')}")
