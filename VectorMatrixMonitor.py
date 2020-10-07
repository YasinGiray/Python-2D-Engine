class Vec3():
    def __init__(self, x=0.0, y=0.0, z=0.0):
        """Quelle: https://github.com/YasinGiray/Vec3-Matrix3.git"""
        self.values = [x, y, z]

    def mul(self, v):
        """Element wise multiplication of self by vector v
        Returns the result as a new vector"""
        new = []
        for i in range(len(self.values)):
            new.append(self.values[i] * v.values[i])
        return Vec3(new[0], new[1], new[2])

    def mulc(self, c):
        """Element wise multiplication of vec3 by constant c
        Returns the result as a new vector"""
        new = []
        for i in range(len(self.values)):
            new.append(self.values[i] * c)
        return Vec3(new[0], new[1], new[2])

    def add(self, v):
        """Element wise addition of vec3 by vector v
        Returns the result as a new vector"""
        new = []
        for i in range(len(self.values)):
            new.append(self.values[i] + v.values[i])
        return Vec3(new[0], new[1], new[2])

    def addc(self, c):
        """Element wise addition of vec3 by constant c
        Returns the result as a new vector"""
        new = []
        for i in range(len(self.values)):
            new.append(self.values[i] + c)
        return Vec3(new[0], new[1], new[2])

    def sub(self, v):
        """Element wise subtraction of vec3 by vector v
        Returns the result as a new vector"""
        new = []
        for i in range(len(self.values)):
            new.append(self.values[i] - v.values[i])
        return Vec3(new[0], new[1], new[2])

    def subc(self, c):
        """Element wise subtraction of vec3 by constant
        Returns the result as a new vector"""
        new = []
        for i in range(len(self.values)):
            new.append(self.values[i] - c)
        return Vec3(new[0], new[1], new[2])

    def cross(self, v):
        """Returns the cross product of self and vector v."""
        a = self.values
        new = [a[1] * v.values[2] - a[2] * v.values[1],
               a[2] * v.values[0] - a[0] * v.values[2],
               a[0] * v.values[1] - a[1] * v.values[0]]
        return Vec3(new[0], new[1], new[2])

    def dot(self, v):
        """Returns the dot product of self and vector v"""
        new = 0
        for i in range(len(self.values)):
            new += self.values[i] * v.values[i]
        return new


class Matrix3():
    def __init__(self, row1=None, row2=None, row3=None):
        """Constructor for Matrix3
            Quelle: https://github.com/YasinGiray/Vec3-Matrix3.git"""
        if row1 is None: row1 = Vec3()
        if row2 is None: row2 = Vec3()
        if row3 is None: row3 = Vec3()
        self.m_values = [row1, row2, row3]

    def setIdentity(self):
        """Sets the current Matrix to an identity matrix
        self is an identity matrix after calling this method"""
        self.m_values[0] = Vec3(1, 0, 0)
        self.m_values[1] = Vec3(0, 1, 0)
        self.m_values[2] = Vec3(0, 0, 1)

    def mulV(self, vector):
        """Multiplication: Matrix times vector.
            'vector' is the vector with which to multiply.
            Return the result as a new Vec3.
            Make sure that you do not change self or the vector.
            return self * v"""
        new = []
        for i in range(len(self.m_values)):
            new.append(self.m_values[i].dot(vector))
        return Vec3(new[0], new[1], new[2])

    def roundM(self):
        """Rounds every entry in the matrix"""
        for i in range(len(self.m_values)):
            for j in range(len(self.m_values[i].values)):
                self.m_values[i].values[j] = round(self.m_values[i].values[j])

    def mulM(self, m):
        """Multiplication: Matrix times Matrix.
            m is the matrix with which to multiply.
            Return the result as a new Matrix3.
            Make sure that you do not change self or the other matrix.
            return this * m"""
        new = []
        tmp = [[], [], []]
        for row in m.m_values:
            tmp[0].append(row.values[0])
            tmp[1].append(row.values[1])
            tmp[2].append(row.values[2])

        for i in range(len(self.m_values)):
            item = Vec3(tmp[i][0], tmp[i][1], tmp[i][2])
            new.append(self.mulV(item))

        trans = [[], [], []]
        for i in new:
            trans[0].append(i.values[0])
            trans[1].append(i.values[1])
            trans[2].append(i.values[2])

        result = []
        for i in range(len(trans)):
            result.append(Vec3(trans[i][0], trans[i][1], trans[i][2]))

        return Matrix3(result[0], result[1], result[2])

    def detA(self):
        """Quelle: https://github.com/YasinGiray/Vec3-Matrix3.git"""
        det = self.m_values[0].values[0] * self.m_values[1].values[1] * self.m_values[2].values[2] + \
              self.m_values[0].values[1] * self.m_values[1].values[2] * self.m_values[2].values[0] + \
              self.m_values[0].values[2] * self.m_values[1].values[0] * self.m_values[2].values[1] - \
              self.m_values[0].values[2] * self.m_values[1].values[1] * self.m_values[2].values[0] - \
              self.m_values[0].values[1] * self.m_values[1].values[0] * self.m_values[2].values[2] - \
              self.m_values[0].values[0] * self.m_values[1].values[2] * self.m_values[2].values[1]
        return det

    def get_inverse(self):
        """Quelle: https://github.com/YasinGiray/Vec3-Matrix3.git
        Komplett übernommen weil es mein Code ist"""
        det = self.detA()
        if round(det, 5) != 0:
            inverse = Matrix3(Vec3(
                self.m_values[1].values[1] * self.m_values[2].values[2] - self.m_values[1].values[2] *
                self.m_values[2].values[1],
                self.m_values[0].values[2] * self.m_values[2].values[1] - self.m_values[0].values[1] *
                self.m_values[2].values[2],
                self.m_values[0].values[1] * self.m_values[1].values[2] - self.m_values[0].values[2] *
                self.m_values[1].values[1]).mulc(1 / det),
                              Vec3(
                                  self.m_values[1].values[2] * self.m_values[2].values[0] - self.m_values[1].values[0] *
                                  self.m_values[2].values[2],
                                  self.m_values[0].values[0] * self.m_values[2].values[2] - self.m_values[0].values[2] *
                                  self.m_values[2].values[0],
                                  self.m_values[0].values[2] * self.m_values[1].values[0] - self.m_values[0].values[0] *
                                  self.m_values[1].values[2]).mulc(1 / det),
                              Vec3(
                                  self.m_values[1].values[0] * self.m_values[2].values[1] - self.m_values[1].values[1] *
                                  self.m_values[2].values[0],
                                  self.m_values[0].values[1] * self.m_values[2].values[0] - self.m_values[0].values[0] *
                                  self.m_values[2].values[1],
                                  self.m_values[0].values[0] * self.m_values[1].values[1] - self.m_values[0].values[1] *
                                  self.m_values[1].values[0]).mulc(1 / det))
            return inverse
        else:
            return False


class Monitor():
    def __init__(self):
        """Initialisation of the monitor class.
        This is a research question. Make sure to read the Adobe RGB (1998) Color Image Encoding specification beforehand.
        In addition you need to research how to convert between CIE XYZ tristimulus colors and RGB colors for other primary valences.
        The monitor is calibrated using a reference white(CIE XYZ values) and
        primary valences red (rx, ry), green (gx, gy) and blue (bx, by), given in CIE xyY.

        The default setting for the monitor is the Adobe RGB (1998) color space.

        Make sure to return floats unless otherwise noted.
        The XYZ values for D65 are given as X = 0.95047
                                            Y = 1.00
                                            Z = 1.08883

        All RGB values are in the range [0, 1].
        self.ref_w = [0.95047, 1.00, 1.08883]
        self.ref_b = [0.5282, 0.5557, 0.6052]
        self.gamma = 1

        self.white_xyz = [152.07, 160.0, 174.25] # ref white
        self.black_xyz = [0.5282, 0.5557, 0.6052] # black k

        x = ((self.lum[0]-self.black_xyz[0])*self.white_xyz[0])/((self.white_xyz[0]-self.black_xyz[0])*self.white_xyz[0])
        y = (self.lum[1]-self.black_xyz[1])/(self.white_xyz[1]-self.black_xyz[1])
        z = ((self.lum[2]-self.black_xyz[2])*self.white_xyz[2])/((self.white_xyz[2]-self.black_xyz[2])*self.white_xyz[2])

        self.red =      [0.64**self.gamma, 0.33**self.gamma]
        self.green =    [0.21**self.gamma, 0.71**self.gamma]
        self.blue =     [0.15**self.gamma, 0.06**self.gamma]
        self.white =    [0.3127**self.gamma, 0.3290**self.gamma]
        """
        self.gamma = 2.19921875
        self.red = [0.64, 0.33]
        self.green = [0.21, 0.71]
        self.blue = [0.15, 0.06]
        self.white = [0.3127, 0.3290]
        self.ref_white = Vec3(0.95047, 1.00, 1.08883)

    def setWhite(self, wx, wy, wz):
        """Sets the monitors reference white to the given X, Y and Z"""
        self.ref_white = Vec3(wx, wy, wz)

    def setGamma(self, gamma):
        """Sets the gamma correction of the monitor to the given gamma"""
        self.gamma = gamma
        # self.setPrimaries(self.red[0], self.red[1], self.green[0], self.green[1], self.blue[0], self.blue[1])

    def setPrimaries(self, rx, ry, gx, gy, bx, by):
        """Sets the primary valences of the monitor to the given primaries red(rx, ry), green(gx, gy) and blue(bx, by)"""
        self.red = [rx, ry]
        self.green = [gx, gy]
        self.blue = [bx, by]

    def setAdobe(self):
        """Sets the monitor to its default setting, the Adobe 1998 RGB color space."""
        self.gamma = 2.19921875
        self.ref_white = Vec3(0.9505, 1.0000, 1.0891)
        self.red = [0.64, 0.33]
        self.green = [0.21, 0.71]
        self.blue = [0.15, 0.06]
        self.white = [0.3127, 0.3290]

    def XYZToRGB(self, x, y, z):
        """Converts the given XYZ tristimulus values to the monitors RGB color space.
        Returns the RGB color as an array of floats [r, g, b]
        If the conversion is not possible, returns the string: "conversion not possible" """
        try:
            xyz = Vec3(x, y, z)
            s1 = Vec3(self.red[0] / self.red[1], self.green[0] / self.green[1], self.blue[0] / self.blue[1])
            s2 = Vec3(1, 1, 1)
            s3 = Vec3((1 - self.red[0] - self.red[1]) / self.red[1],
                      (1 - self.green[0] - self.green[1]) / self.green[1],
                      (1 - self.blue[0] - self.blue[1]) / self.blue[1])

            matrix = Matrix3(s1, s2, s3)
            inverse = matrix.get_inverse()
            if inverse is False:
                return 'conversion not possible'
            if x > 1 or y > 1 or z > 1:
                return 'conversion not possible'

            srgb = inverse.mulV(self.ref_white)
            tmp_m = Matrix3(
                Vec3(s1.values[0] * srgb.values[0], s1.values[1] * srgb.values[1], s1.values[2] * srgb.values[2]),
                Vec3(s2.values[0] * srgb.values[0], s2.values[1] * srgb.values[1], s2.values[2] * srgb.values[2]),
                Vec3(s3.values[0] * srgb.values[0], s3.values[1] * srgb.values[1], s3.values[2] * srgb.values[2]))

            final_m = tmp_m.get_inverse()
            result = final_m.mulV(xyz)
            tmp = [result.values[0] ** (1 / self.gamma), result.values[1] ** (1 / self.gamma),
                   result.values[2] ** (1 / self.gamma)]
            res = []

            for item in tmp:
                if type(item) is complex:
                    item = round(item.real, 2)
                    res.append(item)
                else:
                    item = round(item, 2)
                    res.append(item)

            return res
        except ZeroDivisionError:
            return 'conversion not possible'

    def RGBToXYZ(self, r, g, b):
        """Converts the given RGB color to the monitors corresponding XYZ tristimulus values.
        Returns the XYZ tristimulus values as an array of floats [x, y, z]"""
        R = r ** self.gamma
        G = g ** self.gamma
        B = b ** self.gamma

        # Xr,Xg, Xb
        s1 = Vec3(self.red[0] / self.red[1], self.green[0] / self.green[1], self.blue[0] / self.blue[1])
        s2 = Vec3(1, 1, 1)
        s3 = Vec3((1 - self.red[0] - self.red[1]) / self.red[1], (1 - self.green[0] - self.green[1]) / self.green[1],
                  (1 - self.blue[0] - self.blue[1]) / self.blue[1])
        # print('Vektor: ', s1.values)
        matrix = Matrix3(s1, s2, s3)
        inverse = matrix.get_inverse()

        srgb = inverse.mulV(self.ref_white)

        finalm = Matrix3(
            Vec3(s1.values[0] * srgb.values[0], s1.values[1] * srgb.values[1], s1.values[2] * srgb.values[2]),
            Vec3(s2.values[0] * srgb.values[0], s2.values[1] * srgb.values[1], s2.values[2] * srgb.values[2]),
            Vec3(s3.values[0] * srgb.values[0], s3.values[1] * srgb.values[1], s3.values[2] * srgb.values[2]))

        result = finalm.mulV(Vec3(R, G, B))

        return [round(result.values[0], 2), round(result.values[1], 2), round(result.values[2], 2)]


'''
if __name__ == '__main__':
    print('Test 1 RGB --> XYZ')
    A = Monitor()
    print('Erwartet: ', [0.1882, 0.0753, 0.9911], '\n', 'Bekommen: ', A.RGBToXYZ(0, 0, 1))

    print('Test 3 setWhite')
    A = Monitor()
    A.setWhite(0.96421, 1.0000, 0.82518)
    print('Erwartet: ', [0.6453, 0.3327, 0.0302], '\n', 'Bekommen: ', A.RGBToXYZ(1, 0, 0))

    print('Test 4 Gamma')
    B = Monitor()
    B.setGamma(1.8)
    print('Erwartet: ', [0.1882, 0.0753, 0.9911], '\n', 'Bekommen: ', B.RGBToXYZ(0, 0, 1))

    print('Test 5')
    C = Monitor()
    C.setPrimaries(0.6250, 0.3400, 0.2800, 0.5950, 0.1550, 0.0700)
    print('Erwartet: ', [0.7031, 0.4743, 0.9784], '\n', 'Bekommen: ', C.RGBToXYZ(1, 0.5, 1))

    print('Test XYZ --> RGB')
    print('Test 2')
    B = Monitor()
    print('Erwartet: ', [0, 0, 1], 'Bekommen: ',
          B.XYZToRGB(0.18818516209063835, 0.07527406483625534, 0.9911085203440287))

    #
    # Self-testing
    print('RGB --> XYZ')
    Z = Monitor()
    print('Test 1 RGB=0.5,0,0.5: \n', 'Erwartet: ', [0.1666, 0.0811, 0.2217], '\n', 'Bekommen: ',
          Z.RGBToXYZ(0.5, 0, 0.5))
    print('Test 2 RGB=0.5,0.5,0.5: \n', 'Erwartet: ', [0.207, 0.2178, 0.2371], '\n', 'Bekommen: ',
          Z.RGBToXYZ(0.5, 0.5, 0.5))
    print('Test 3 RGB=0,0,0: \n', 'Erwartet: ', [0.0, 0.0, 0.0], '\n', 'Bekommen: ', Z.RGBToXYZ(0, 0, 0))
    print('Test 4 RGB=1,1,1: \n', 'Erwartet: ', [0.9505, 1.0, 1.0888], '\n', 'Bekommen: ', Z.RGBToXYZ(1, 1, 1))

    print('Gamma Correction')
    Y = Monitor()
    Y.setGamma(1.8)
    print('Gammatest 1 g=1.8: \n', 'Erwartet: ', [0.1872, 0.094, 0.1212], '\n', 'Bekommen: ', Y.RGBToXYZ(0.5, 0, 0.3))
    Y.setGamma(1.0)
    print('Gammatest 2 g=1.0: \n', 'Erwartet: ', [0.3448, 0.1713, 0.3108], '\n', 'Bekommen: ', Y.RGBToXYZ(0.5, 0, 0.3))
    Y.setGamma(2.2)
    print('Gammatest 2 g=2.2: \n', 'Erwartet: ', [0.1388, 0.07, 0.076], '\n', 'Bekommen: ', Y.RGBToXYZ(0.5, 0, 0.3))

    print('XYZ --> RGB')
    X = Monitor()
    print('Test 1 XYZ=0.1666, 0.0811, 0.2217: \n', 'Erwartet: ', [0.5, 0, 0.5], '\n', 'Bekommen: ',
          X.XYZToRGB(0.1666, 0.0811, 0.2217))
    print('Test 2 XYZ=0.207, 0.2178, 0.2371: \n', 'Erwartet: ', [0.5, 0.5, 0.5], '\n', 'Bekommen: ',
          X.XYZToRGB(0.207, 0.2178, 0.2371))
    print('Test 3 XYZ=0.0, 0.0, 0.0: \n', 'Erwartet: ', [0, 0, 0], '\n', 'Bekommen: ', X.XYZToRGB(0.0, 0.0, 0.0))
    print('Test 4 XYZ=0.9505, 1.0, 1.0888: \n', 'Erwartet: ', [1, 1, 1], '\n', 'Bekommen: ',
          X.XYZToRGB(0.9505, 1.0, 1.0888))

    # Sonderfall
    # S = Monitor()
    # S.setPrimaries(0,0,0.2800, 0.5950, 0.1550, 0.0700)
    # print('Sonderfall RGB=0.5,0,0.5: \n', 'Erwartet: ', [0.1666, 0.0811, 0.2217], '\n','Bekommen: ',S.RGBToXYZ(0.5,0,0.5))

    # failed test
    D = Monitor()
    print("conversion not possible", D.XYZToRGB(1.182, 1.000, 1.329))
'''