class Line:

    def __init__(self, coor1, coor2):
        self.coor1 = coor1
        self.coor2 = coor2

    def distance(self):
        return sqrt((self.coor1[0]-self.coor2[0])**2 + (self.coor1[1]-self.coor2[1]**2)

# coordinate2=(8, 10)
# li=Line(coordinate1, coordinate2)
# li.distance()

coordinate1= (2, 3)
coordinate2=(8, 10)
li=Line(coordinate1, coordinate2)
