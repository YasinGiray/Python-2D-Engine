import math


class Canvas():
    def __init__(self, width, height, background=" "):
        """Constructor for the Canvas class

        In case you don't have a constructor from the last exercise you may use the following default:
        self.data = [[background for col in range(height)] for row in range(width)]
        self.origin = [math.floor(width/2), math.floor(height/2)]
        self.ox = math.floor(width/2)
        self.oy = math.floor(height/2)

        """
        self.x = width
        self.y = height
        self.bg = background
        self.field = [[self.bg for x in range(width)] for y in range(height)]
        self.origin = [width // 2, height // 2]

    def display(self):
        """
        Printing method for the canvas. When triggered outputs the canvas as characters.
        Example outputs are given in the test cases. White spaces may be used as you prefer,
        but you must have *at least* one whitespace between every character.
        """
        bild = ''
        for i in range(self.y):
            for j in range(self.x):
                bild += self.field[i][j] + ' '
            bild += '\n'

        print(bild)
        pass

    def code(self, p):
        code = ''
        if p[0] < -self.origin[0]:
            code += 'l'
        elif p[0] > self.origin[0]:
            code += 'r'

        if p[1] < -self.origin[1]:
            code += 'u'
        elif p[1] > self.origin[1]:
            code += 'o'
        return code

    def cohen(self, line):
        c1 = self.code(line.p1)
        c2 = self.code(line.p2)
        # print('c1 ist: ', c1)
        # print('c2 ist: ', c2)
        if c1 == '' and c2 == '':
            return line
        elif (c1 == c2) and c1 != '' and c2 != '':
            return line

        else:
            x1 = line.p1[0]
            y1 = line.p1[1]
            x2 = line.p2[0]
            y2 = line.p2[1]
            if y1 == y2:
                return line
            if abs(x2 - x1) == 0:
                return line

            while c1 != '':
                if 'o' in c1:
                    x1 = line.p1[0] + (line.p2[0] - line.p1[0]) * (self.origin[1] - line.p1[1]) / (
                                line.p2[1] - line.p1[1])
                    y1 = self.origin[1]
                    c1 = c1.replace('o', '')
                elif 'u' in c1:
                    x1 = line.p1[0] + (line.p2[0] - line.p1[0]) * (-self.origin[1] - line.p1[1]) / (
                                line.p2[1] - line.p1[1])
                    y1 = -self.origin[1]
                    c1 = c1.replace('u', '')


                elif 'r' in c1:
                    x1 = self.origin[0]
                    y1 = line.p1[1] + (line.p2[1] - line.p1[1]) * (self.origin[0] - line.p1[0]) / (
                                line.p2[0] - line.p1[0])
                    c1 = c1.replace('r', '')
                elif 'l' in c1:
                    x1 = -self.origin[0]
                    y1 = line.p1[1] + (line.p2[1] - line.p1[1]) * (-self.origin[0] - line.p1[0]) / (
                                line.p2[0] - line.p1[0])
                    c1 = c1.replace('l', '')

            while c2 != '':
                if 'o' in c2:
                    x2 = line.p2[0] + (line.p1[0] - line.p2[0]) * (self.origin[1] - line.p2[1]) / (
                                line.p1[1] - line.p2[1])
                    y2 = self.origin[1]
                    c2 = c2.replace('o', '')
                elif 'u' in c2:
                    x2 = line.p2[0] + (line.p1[0] - line.p2[0]) * (-self.origin[1] - line.p2[1]) / (
                                line.p1[1] - line.p2[1])
                    y2 = -self.origin[1]
                    c2 = c2.replace('u', '')


                elif 'r' in c2:
                    x2 = self.origin[0]
                    y2 = line.p2[1] + (line.p1[1] - line.p2[1]) * (self.origin[0] - line.p2[0]) / (
                                line.p1[0] - line.p2[0])
                    c2 = c2.replace('r', '')
                elif 'l' in c2:
                    x2 = -self.origin[0]
                    y2 = line.p2[1] + (line.p1[1] - line.p2[1]) * (-self.origin[0] - line.p2[0]) / (
                                line.p1[0] - line.p2[0])
                    c2 = c2.replace('l', '')
            return Line(math.floor(x1), math.floor(y1), math.floor(x2), math.floor(y2))

    def draw(self, toDraw, color="A"):
        """Drawing method for the canvas class. May be given a Line, a Rect or a Cavalier.
        When given a Rect draw all Points on the Rectangle.
        When given a Line draw all points on the Line. We are currently working with an approximation. Any point with an
        euclidian distance to the line of less than or equal 0.7 is drawn.
        Make sure to clip your lines using the Cohen-Sutherland algortihm. After clipping, floor the coordinates of the endpoints
        Draw the cavalier perspective with alpha = 120°(the angle between the projection of the x- and z-axis) and shorten the depth to half dim.
        Floor the coordinates of the offset points, draw the basic square as you would draw a rectangle
        The given color determines the character to be drawn.
        """
        if isinstance(toDraw, Line):
            """
            #if toDraw.p1[0] <= toDraw.p2[0]:

                #while x <= toDraw.p2[0] and x <= self.origin[0]:
                    #tmp = [x+1, y+m]

            #if math.sqrt((tmp[0] - tmp[0]) ** 2 + (math.floor(tmp[1]) - tmp[1]) ** 2) <= 0.7:
            #    newx = self.origin[0] + x + 1
            #    newy = self.origin[1] - int(math.floor(y + m))
            #    self.field[newy][newx] = color

            #elif math.sqrt((tmp[0] - tmp[0]) ** 2 + (math.ceil(tmp[1]) - tmp[1]) ** 2) <= 0.7:
            #    newx = self.origin[0] + x + 1
            #    newy = self.origin[1] - int(math.floor(y + m))
            #    self.field[newy][newx] = color
            if toDraw.p2[0] == 0 and toDraw.p2[1] == 0 and toDraw.p1[0] == 0 and toDraw.p1[1] == 0:
                return
            """
            if toDraw.p1[0] <= toDraw.p2[0]:
                toDraw = self.cohen(toDraw)
                x = (toDraw.p1[0] - toDraw.p2[0])
                y = (toDraw.p1[1] - toDraw.p2[1])
                for i in range(min(toDraw.p1[1], toDraw.p2[1]), max(toDraw.p1[1], toDraw.p2[1]) + 1):  # y index
                    for j in range(min(toDraw.p1[0], toDraw.p2[0]), max(toDraw.p1[0], toDraw.p2[0]) + 1):  # x index
                        a = x * j + y * i
                        s = (x * toDraw.p1[0] + y * toDraw.p1[1] - a) / (-x ** 2 - y ** 2)
                        p = [toDraw.p1[0] + s * x, toDraw.p1[1] + s * y]
                        dist = math.sqrt((j - p[0]) ** 2 + (i - p[1]) ** 2)
                        # print('x,y: ', j, i, 'dist: ', dist)
                        if dist <= 0.7:
                            newx = self.origin[0] + j
                            newy = self.origin[1] - i
                            if self.x > newx >= 0 and self.y > newy >= 0:
                                # print('x,y: ', j, i, 'dist: ', dist)
                                self.field[newy][newx] = color

            else:
                self.draw(Line(toDraw.p2[0], toDraw.p2[1], toDraw.p1[0], toDraw.p1[1]), color)

        elif isinstance(toDraw, Rect):
            x = vars(toDraw)
            for line in x:
                self.draw(x.get(line), color)

        elif isinstance(toDraw, Cavalier):
            x = vars(toDraw)
            for line in x:
                self.draw(x.get(line), color)

    def help(self, pc, og, color):
        # pc = (y,x) als Python Koords.
        pl = (pc[0], pc[1] - 1)
        pr = (pc[0], pc[1] + 1)
        po = (pc[0] - 1, pc[1])
        pu = (pc[0] + 1, pc[1])

        if pc[0] == self.y - 1:
            return

        if pc[1] == self.x - 1:
            return

        if self.field[pr[0]][pr[1]] == og:
            self.field[pc[0]][pc[1]] = color
            self.field[pr[0]][pr[1]] = color
            self.help(pr, og, color)

        if self.field[pl[0]][pl[1]] == og:
            self.field[pc[0]][pc[1]] = color
            self.field[pl[0]][pl[1]] = color
            self.help(pl, og, color)

        if self.field[po[0]][po[1]] == og:
            self.field[pc[0]][pc[1]] = color
            self.field[po[0]][po[1]] = color
            self.help(po, og, color)

        if self.field[pu[0]][pu[1]] == og:
            self.field[pc[0]][pc[1]] = color
            self.field[pu[0]][pu[1]] = color
            self.help(pu, og, color)
        return

    def fill(self, x, y, color='F'):
        '''
        Fills all adjacent points(use a manhattan neighborhood) starting at (x,y)
        that have the same color as the point at (x,y).
        The given color determines the character to be drawn.
        '''
        """
        try:
            if self.field[p[1]][p[0]] == self.field[p[1]-1][p[0]]:
                self.field[p[1]][p[0]] = color
                self.fill(p[1]-1,p[0], color)

            if self.field[p[1]][p[0]] == self.field[p[1]+1][p[0]]:
                self.field[p[1]][p[0]] = color
                self.fill(p[1]+1,p[0], color)

            if self.field[p[1]][p[0]] == self.field[p[1]][p[0]-1]:
                self.field[p[1]][p[0]] = color
                self.fill(p[1],p[0]-1, color)

            if self.field[p[1]][p[0]] == self.field[p[1]][p[0]+1]:
                self.field[p[1]][p[0]] = color
                self.fill(p[1], p[0]+1, color)

        except IndexError:
            return
            
                res = set()
        print(p)
        if self.x > p[0] >= 0 and self.y > p[1] >= 0:
            print(p)
            if self.field[p[1]-1][p[0]] == self.field[p[1]][p[0]]:
                self.field[p[1]-1][p[0]] = color
                self.fill(x, y+1, color)

            if self.field[p[1] + 1][p[0]] == self.field[p[1]][p[0]]:
                self.field[p[1]+1][p[0]] = color
                self.fill(x, y - 1, color)

            if self.field[p[1]][p[0]-1] == self.field[p[1]][p[0]]:
                self.field[p[1]][p[0]-1] = color
                self.fill(x-1, y, color)

            if self.field[p[1]][p[0]+1] == self.field[p[1]][p[0]]:
                self.field[p[1]][p[0]+1] = color
                self.fill(x+1, y, color)

        
        test = str(self.field[x+self.origin[0]][y+self.origin[1]])

        for i in range(y, self.origin[1]):
            for j in range(x, self.origin[0]):
                res = []
                pc = (j+self.origin[0], i+self.origin[1])
                pl = (j+self.origin[0]-1, i+self.origin[1])
                pr = (j+self.origin[0]+1, i+self.origin[1])
                po = (j+self.origin[0], i+self.origin[1]-1)
                pu = (j+self.origin[0], i+self.origin[1]+1)


                if test == self.field[pr[0]][pr[1]]:
                    self.field[pc[0]][pc[1]] = color

                if self.field[pc[0]][pc[1]] == self.field[pu[0]][pu[1]]:
                    res.append(pu)
                else:
                    break

                if self.field[pc[0]][pc[1]] == self.field[pl[0]][pl[1]]:
                    res.append(pl)

                if self.field[pc[0]][pc[1]] == self.field[po[0]][po[1]]:
                    res.append(po)
                if self.field[pc[0]][pc[1]] == self.field[pu[0]][pu[1]]:
                    res.append(pu)

        self.field[pc[0]][pc[1]] = color

        for item in res:
            self.fill(item[0]-self.origin[0],item[1]-self.origin[1])
        """

        og = str(self.field[self.origin[0] - y][self.origin[1] + x])
        if og == color:
            return
        pc = (self.origin[0] - y, self.origin[1] + x)
        self.help(pc, og, color)


class Line():
    def __init__(self, x1, y1, x2, y2):
        """Constructor for Line
        The first point is (x1, y1), the second point is (x2, y2).
        All coordinates are given as cartesian coordinates.
        """
        self.p1 = (x1, y1)
        self.p2 = (x2, y2)


class Rect():

    def __init__(self, x, y, width, height):
        """Constructor for Rect
        Expects a rectangle whose lower left hand corner is at (x,y).
        With the given width and height.
        All coordinates are given as cartesian coordinates.
        """
        self.l1 = Line(x, y, x + width, y)
        self.l2 = Line(x + width, y, x + width, y + height)
        self.l3 = Line(x, y, x, y + height)
        self.l4 = Line(x, y + height, x + width, y + height)


class Cavalier():

    def __init__(self, x, y, dim):
        """Constructor for cavalier
        Expects a square whose lower left hand corner is at (x,y).
        This square is used to draw an isometric cube in cavalier perspective (see testcase)
        Dim is the parameter defining the width, height and depth of the cube
        All coordinates are given as cartesian coordinates.
        """

        # p = Vec4(-9,-9,1)

        # we = Vec4(-9+dim/2, -9+dim/2, 1)
        # t1 = Matrix4(Vec4(1,0,-x), Vec4(0,1,-y), Vec4(0,0,1))
        # rot= Matrix4(Vec4(math.cos(tmp),-math.sin(tmp),p.values[0]*(1-math.cos(tmp)) + p.values[1]*math.sin(tmp)),
        #             Vec4(math.sin(tmp), math.cos(tmp),p.values[1]*(1-math.cos(tmp)) - p.values[0]*math.sin(tmp)),
        #             Vec4(0,0,1))
        # t2 = Matrix4(Vec4(1,0,x), Vec4(0,1,x), Vec4(0,0,1))
        # p_new = t2.mulV(rot.mulV(t1.mulV(p)))
        # p_new = rot.mulV(we)
        # print(p_new)
        """
        tmp = math.radians(120)
        newx = (dim) * math.cos(tmp) - (dim) * math.sin(tmp)
        newy = (dim) * math.sin(tmp) + (dim) * math.cos(tmp)
        print(newx, newy)

        rotp = (int(round((newx+x)/2, 10)), int(round((newy+y)/2 +y, 10)))
        print(rotp)
        self.rect1 = Rect(x,y,dim,dim)
        self.rect2 = Rect(rotp[0], rotp[1], dim,dim)

        self.l1 = Line(x,y, int(round(x+(dim/2))), int(round(y+(dim/2))))
        self.l2 = Line(x+dim,y, int(round(x+(dim/2)+dim)), int(round(y+(dim/2))))
        self.l3 = Line(x,y+dim, int(round(x+(dim/2))), int(round(y+(dim/2)+dim)))
        self.l4 = Line(x+dim,y+dim, int(round(x+(dim/2)+dim)), int(round(y+(dim/2)+dim)))
        """
        self.rect1 = Rect(x, y, dim, dim)

        p2 = (dim / 2, 0)
        tmp = math.radians(60)
        p_rot = (p2[0] * math.cos(tmp) - p2[1] * math.sin(tmp),
                 p2[0] * math.sin(tmp) + p2[1] * math.cos(tmp))
        newx = int(math.floor(p_rot[0])) + x
        newy = int(math.floor(p_rot[1])) + y
        p_new = (newx, newy)
        self.rect2 = Rect(p_new[0], p_new[1], dim, dim)

        self.l1 = Line(x, y, newx, newy)
        self.l2 = Line(x + dim, y, newx + dim, newy)
        self.l3 = Line(x, y + dim, newx, newy + dim)
        self.l4 = Line(x + dim, y + dim, newx + dim, newy + dim)


if __name__ == '__main__':
    print('Fall 1')
    can = Canvas(21, 31, "+")
    can.display()

    print('Fall 2')
    can = Canvas(31, 11, "+")
    l = Line(0, 5, 0, -5)
    can.draw(l, "L")
    can.display()

    print('Fall 3')
    can = Canvas(11, 11, "+")
    r = Rect(-2, -2, 5, 5)
    can.draw(r, "R")
    can.display()

    print('Fall 4')
    can = Canvas(11, 11, "+")
    r = Rect(-2, -2, 15, 15)
    can.draw(r, "R")
    can.display()

    print('Fall 5')
    can = Canvas(11, 11, "+")
    r = Rect(-2, -2, 5, 5)
    can.draw(r, "R")
    can.fill(0, 0, "F")
    can.display()

    print('Fall 6')
    can = Canvas(21, 21, "+")
    r = Cavalier(-9, -9, 12)  # -4,-6
    can.draw(r, "C")
    can.display()

    print('Fall 7')
    can = Canvas(21, 21, "+")
    r = Cavalier(-4, -4, 6)
    can.fill(-4, -4, "-")
    can.draw(r, "C")
    can.fill(-4, -4, "F")
    can.display()

    print('Fall 8')
    can = Canvas(21, 21, "+")
    r = Cavalier(-4, -4, 15)
    can.draw(r, "C")
    can.fill(0, 0, "C")
    can.fill(0, 0, "C")
    can.display()

    # print('Eigentest Linien')
    # can = Canvas(31, 11, "+")
    # l = Line(0, 0, 0, 0)
    # can.draw(l, "L")
    # can.display()

    print('Neuer Test')
    can = Canvas(11, 11, "+")
    l = Line(20, -4, 0, 1)
    can.draw(l, "L")
    can.display()

    c = Canvas(11, 11, "+")
    l = Line(6, -14, 4, 14)
    c.draw(l, 'L')
    c.display()
