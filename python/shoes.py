class Shoes:

    def __init__(self, footsize, size=42):
        self.size = size
        self.footsize = footsize
        self.color = (0, 0, 0)
        self.distance = 0

    def walk(self):
        self.distance += self.size + self.footsize
        print(str(self.color) + " shoe of size " + str(self.size) + " is walking!")

    def run(self):
        self.distance += self.size + int(3 * self.footsize / 2)
        print(str(self.color) + " shoe of size " + str(self.size) + " is running!")


s1 = Shoes(100, 51)
s1.color = (255, 255, 128)

s2 = Shoes(110)

s1.run()
s2.run()
s1.walk()
s2.walk()

print("s1.distance = " + str(s1.distance))
print("s2.distance = " + str(s2.distance))
