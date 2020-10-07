import math


class Canvas():
    def __init__(self, width, height, background=" "):
        """Initialisation method for the Canvas class"""
        self.x = width
        self.y = height
        self.zmin, self.zmax = -10, -1
        self.bg = background
        self.field = [[[] for x in range(width)] for y in range(height)]
        self.origin = [width // 2, height // 2]
        self.buffer = []
        self.cam = (0.0, 0.0, -10.0)

    def pq(self, a, b, c):

        r = b ** 2 - 4 * a * c
        if a != 0 and b != 0 and c != 0:
            if r > 0:
                print('2 Punkte')
                x1 = (-b + math.sqrt((b ** 2) - (4 * (a * c)))) / (2 * a)
                x2 = (-b - math.sqrt((b ** 2) - (4 * (a * c)))) / (2 * a)
                res = (x1, x2)
                return res

            elif r == 0:
                print('1 Punkt')
                x = (-b + math.sqrt(b ** 2 - 4 * a * c)) / 2 * a
                res = (x,)
                return res

            else:
                print('keine Punkte')
                return tuple()

        elif a == 0 and b != 0 and c != 0:
            x = -c / b
            res = (x,)
            print('1 Punkt ohne PQ')
            return res

        elif a != 0 and b == 0 and c != 0:
            x = math.sqrt(abs(c))
            res = (-x, x)
            print('2 Punkte ohne PQ')
            return res

        elif a != 0 and b != 0 and c == 0:
            x1 = 0
            x2 = -b
            res = (x1, x2)
            print('2 Punkte ohne PQ')
            return res

    def render(self):
        """
        Rendering method for the raytracer. Renders all objects attached to the canvas.
        Everything is drawn using raycasting. The canvas is positioned at (0.0, 0.0, -1.0) and
        has the endpoints(-1.0, -1.0, -1.0), (-1.0, 1.0, -1.0), (1.0, 1.0, -1.0), (1.0, -1.0, -1.0).

        The camera is positioned at (0.0, 0.0 , -10.0).

        Rays are send from the camera to the sampling points on the canvas.

        You do not need to implement clipping, backface culling or similar methods.

        Make sure to send one ray per entry in the canvas.

        In addition make sure that only the nearest collision is drawn per ray, i.e. implement z-occlusion.

        The color returned by a given ray is the color of the nearest collison's hit object.

        When no attached object is hit, the color returned for that ray is the background of the canvas.

        Returns the content of the canvas as a string and does *not* print it.

        for item in self.buffer:
            for p in item:
                self.field[self.origin[1]-p[1]][self.origin[0]+p[0]] = p[3]

        bild = ''
        for i in range(self.y):
            for j in range(self.x):
                bild += self.field[i][j] + ' '
            bild += '\n'

        return bild
        """
        test = ''
        y = 1 - (2 / self.y) / 2
        y_py = 0
        y_step = 2 / self.y
        counter = 1
        while y > -1:
            x = -1 + (2 / self.x) / 2
            x_py = 0
            x_step = 2 / self.x
            while x < 1:
                for item in self.buffer:
                    if isinstance(item, Sphere):
                        try:
                            a = (x ** 2 + y ** 2) / (x ** 2 + y ** 2)
                            b = (2 * (self.cam[0] * x + self.cam[1] * y + self.cam[2] * (-1) - self.cam[0] * x *
                                      item.origin[0] - self.cam[1] * y * item.origin[1] - self.cam[2] * (-1) *
                                      item.origin[2])) / (x ** 2 + y ** 2)
                            c = (self.cam[0] ** 2 + self.cam[1] ** 2 + self.cam[2] ** 2 + item.origin[0] ** 2 +
                                 item.origin[1] ** 2 + item.origin[2] ** 2) / (x ** 2 + y ** 2)
                            tmp = self.pq(a, b, c)
                            print('das ist tmp ', tmp)
                            if len(tmp) == 0:
                                test += self.bg + ' '
                                continue

                            elif len(tmp) == 1:
                                point = [self.cam[0] + tmp[0] * item.origin[0], self.cam[1] + tmp[0] * item.origin[1],
                                         self.cam[2] + tmp[0] * item.origin[2]]
                                buffer_tmp = (str(item.get_color()), point[2])
                                self.field[y_py][x_py].append(buffer_tmp)
                                test += item.get_color() + ' '


                            elif len(tmp) == 2:
                                point1 = [self.cam[0] + tmp[0] * item.origin[0], self.cam[1] + tmp[0] * item.origin[1],
                                          self.cam[2] + tmp[0] * item.origin[2]]
                                buffer_tmp = (str(item.get_color()), point1[2])
                                self.field[y_py][x_py].append(buffer_tmp)
                                test += item.get_color() + ' '

                                point2 = [self.cam[0] + tmp[0] * item.origin[0], self.cam[1] + tmp[0] * item.origin[1],
                                          self.cam[2] + tmp[0] * item.origin[2]]
                                buffer_tmp = (str(item.get_color()), point2[2])
                                self.field[y_py][x_py].append(buffer_tmp)
                                # test += item.get_color() + ' '

                        except ZeroDivisionError:
                            '''
                            a = 0
                            b = (self.cam[0] * x + self.cam[1] * y + self.cam[2] * (-1) - self.cam[0] * x * item.origin[0] - self.cam[1] * y * item.origin[1] - self.cam[2] * (-1) * item.origin[2])
                            c = (self.cam[0] ** 2 + self.cam[1] ** 2 + self.cam[2] ** 2 + item.origin[0] ** 2 + item.origin[1] ** 2 + item.origin[2] ** 2)
                            tmp = self.pq(round(a, 5), round(b, 5), round(c, 5))

                            if len(tmp) == 0:
                                pass

                            elif len(tmp) == 1:
                                point = [self.cam[0] + tmp[0] * item.origin[0], self.cam[1] + tmp[0] * item.origin[1], self.cam[2] + tmp[0] * item.origin[2]]
                                buffer_tmp = (str(item.get_color()), point[2])
                                self.field[y_py][x_py].append(buffer_tmp)

                            elif len(tmp) == 2:
                                point1 = [self.cam[0] + tmp[0] * item.origin[0], self.cam[1] + tmp[0] * item.origin[1], self.cam[2] + tmp[0] * item.origin[2]]
                                buffer_tmp = (str(item.get_color()), point1[2])
                                self.field[y_py][x_py].append(buffer_tmp)

                                point2 = [self.cam[0] + tmp[0] * item.origin[0], self.cam[1] + tmp[0] * item.origin[1], self.cam[2] + tmp[0] * item.origin[2]]
                                buffer_tmp = (str(item.get_color()), point2[2])
                                self.field[y_py][x_py].append(buffer_tmp)
                                
                            a = 0
                            b = 2*(self.cam[0]*x + self.cam[1]*y + self.cam[2]*(-1) - self.cam[0]*x*item.origin[0] - self.cam[1]*y*item.origin[1] - self.cam[2]*(-1)*item.origin[2])
                            c = (self.cam[0]**2 + self.cam[1]**2 + self.cam[2]**2 + item.origin[0]**2 + item.origin[1]**2 + item.origin[2]**2)
                            tmp = self.pq(a, b, c)

                            if len(tmp) == 0:
                                test += self.bg + ' '
                                continue

                            elif len(tmp) == 1:
                                point = [self.cam[0] + tmp[0] * item.origin[0] ,self.cam[1] + tmp[0] * item.origin[1], self.cam[2] + tmp[0] * item.origin[2]]
                                buffer_tmp = (str(item.get_color()), point[2])
                                self.field[y_py][x_py].append(buffer_tmp)
                                test += item.get_color() + ' '


                            elif len(tmp) == 2:
                                point1 = [self.cam[0] + tmp[0] * item.origin[0], self.cam[1] + tmp[0] * item.origin[1], self.cam[2] + tmp[0] * item.origin[2]]
                                buffer_tmp = (str(item.get_color()), point1[2])
                                self.field[y_py][x_py].append(buffer_tmp)
                                test += item.get_color() + ' '

                                point2 = [self.cam[0] + tmp[0] * item.origin[0] ,self.cam[1] + tmp[0] * item.origin[1], self.cam[2] + tmp[0] * item.origin[2]]
                                buffer_tmp = (str(item.get_color()), point2[2])
                                self.field[y_py][x_py].append(buffer_tmp)
                            '''
                x += x_step
                x_py += 1
                print('Ray ', counter, ': x,y ist: ', x, y)
                counter += 1
            y -= y_step
            y_py += 1
            # test += '\n'

        bild = ''
        for i in range(self.y):
            for j in range(self.x):
                print(self.field[i][j])
                if len(self.field[i][j]) == 0:
                    bild += self.bg + ' '
                elif len(self.field[i][j]) == 1:
                    color = min(self.field[i][j], key=lambda o: o[1])
                    bild += color[0] + ' '
                else:
                    color = min(self.field[i][j], key=lambda o: o[1])
                    bild += color[0] + ' '
            bild += '\n'

        return bild
        # return test

    def attach(self, toAttach):
        """Method for attaching an object to the scene. Only models attached to the canvas are drawn.
        Vllt Ergebnisse umwandeln von Skala 0-1.0 auf Koordinatenskala.
        Fehler bei 2,2 gespiegelt, Kugel zu breit.
        was passiert überlappung von kugel und dreieck? schneiden sich
        skalieren der größe, je nach entfernung
        ist -1,1 Skalierung das Einnahmekoeffizient des Canvas?
        schräglage von Dreiecken. 90° zu Z achse nur ein Strich?
        Wenn schräg, können wir einfach mit x,y Koords arbeiten zur Glättung?


        lm = []
        if isinstance(toAttach, Sphere):
            #xmin, xmax = int(round(toAttach.origin[0]*self.origin[0] - toAttach.radius*self.origin[0])), int(round(toAttach.origin[0]*self.origin[0] + toAttach.radius*self.origin[0]))
            #ymin, ymax = int(round(toAttach.origin[1]*self.origin[0] - toAttach.radius*self.origin[0])), int(round(toAttach.origin[1]*self.origin[0] + toAttach.radius*self.origin[0]))
            radius = toAttach.radius*self.origin[0]
            for z in range(self.zmin, self.zmax):
                for y in range(-self.origin[1], self.origin[1]):
                    for x in range(-self.origin[0], self.origin[0]):
                        sphere = math.sqrt((x - toAttach.origin[0]*self.origin[0]) ** 2 + (y - toAttach.origin[1]*self.origin[1]) ** 2 + (z - toAttach.origin[2]) ** 2)
                        if radius*1.05 >= sphere >= radius*0.95:
                            lm.append([x,y,z, toAttach.color])
        self.buffer.append(lm)
        #print(lm)
        """
        self.buffer.append(toAttach)


class Sphere():
    def __init__(self, origin, radius, color):
        """
        Initialisation method for Sphere class
        Expects the origin as an arrays in the form of [x, y, z].
        Radius is the radius of the sphere.
        Color is the color the triangle is drawn in.
        """
        self.origin = origin
        self.radius = radius
        self.color = color

    def check_sphere(self, p):
        """p is a point in canvas, is expected to be [x, y, z]"""
        sphere = math.sqrt((p[0] - self.origin[0]) ** 2 + (p[1] - self.origin[1]) ** 2 + (p[2] - self.origin[2]) ** 2)
        if round(sphere, 5) == self.radius:
            return True
        else:
            return False

    def get_color(self):
        return self.color


class Triangle():
    def __init__(self, a, b, c, color):
        """
        Initialisation method for the Triangle class
        Expects points as arrays in the form of [x, y, z]. Color is the color the triangle is drawn in.
        """
        self.p1 = a
        self.p2 = b
        self.p3 = c
        self.color = color


'''
if __name__ == '__main__':
    print('Test 1:')
    C = Canvas(21, 21, "+")
    S = Sphere([0, 0, 0], 0.8, "S")
    C.attach(S)
    print(C.render())
'''
