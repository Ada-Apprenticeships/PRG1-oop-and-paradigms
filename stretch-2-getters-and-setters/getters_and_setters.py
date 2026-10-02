"""
Optional stretch. Controlling what can be changed from outside.

A plain attribute can be set to anything by anyone. A property lets
the class decide what is allowed.
"""


class Permit:
    def __init__(self, registration, days_valid):
        self._registration = registration
        self._days_valid = days_valid

    @property
    def registration(self):
        return self._registration

    @property
    def days_valid(self):
        return self._days_valid

    @days_valid.setter
    def days_valid(self, value):
        if not isinstance(value, int) or value < 1:
            print(f"Rejected: {value} is not a sensible number of days")
            return
        self._days_valid = value


permit = Permit("AB12 CDE", 30)

print(permit.registration)
print(permit.days_valid)

permit.days_valid = 60
print(permit.days_valid)

permit.days_valid = -5
print(permit.days_valid)

permit.days_valid = "a fortnight"
print(permit.days_valid)

permit.registration = "XY99 ZZZ"
