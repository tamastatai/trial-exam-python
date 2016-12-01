# Create a class that represents a cuboid:
# It should take its three sizes as constructor parameters (numbers)
# It should have a method called `getSurface` that returns the cuboid's surface
# It should have a method called `getVolume` that returns the cuboid's volume

class Cuboid():
    def __init__(self, width, height, length):
        self.width = width
        self.height = height
        self.length = length

    def getSurface(self):
        return (self.width * self.height) * 2 + (self.height * self.length) * 2 + (self.width + self.length) * 2

    def getVolume(self):
        return self.width * self.height * self.length

crashtest = Cuboid(30, 50, 70)
print(crashtest.getSurface())
print(crashtest.getVolume())
