def __init__(self, initialAge):
    # Add some more code to run some checks on initialAge
    if initialAge > 0:
        self.age = initialAge
    else:
        print("Age is not valid, setting age to 0.")
        self.age = 0


def amIOld(self):
    if self.age < 13:
        print("You are young.")
    elif self.age < 18 and self.age >= 13:
        print("You are a teenager.")
    else:
        print("You are old.")


def yearPasses(self):
    self.age = self.age+1
