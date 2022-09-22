class car:
    def __init__(self, x, y, speed, transmition):
        self.color = x
        self.type = y
        self.speed = speed
        self.transmition = transmition

    def moving(self):
        name = self.type
        speed = self.speed
        print(f"{name} is Running now in {speed} KM/h")


BMW = car("RED", "BWM", 200, 'A')
print(BMW.speed)

Ferrari = car("Black", "Ferrari", 400, 'M')

Ferrari.moving()
BMW.moving()
