"""
    Dieter de Wit 15146
    Tarea3 - BitmapWriter
    Utilizar la Funcion de Linea para
"""

# Interpretar Strings como datos Binarios
import struct


def char(c):
    return struct.pack("=c", c.encode('ascii'))


def word(c):
    return struct.pack("=h", c)


def dword(c):
    return struct.pack("=l", c)


def glColor(r, g, b):
    r = r * 255
    g = g * 255
    b = b * 255
    color = bytes([r, g, b])
    return color


class Bitmap(object):
    def __init__(self, width, height, x, y):
        self.width = width
        self.height = height
        self.x = x
        self.y = y
        self.framebuffer = []
        self.glClear()

    def glClear(self):
        self.framebuffer = [
            [
                glColor(0, 0, 0)
                for x in range(self.width)
            ]
            for y in range(self.height)
        ]

    def write(self, filename):
        f = open(filename, "bw")

        # file header
        f.write(char('B'))
        f.write(char('M'))
        f.write(dword(14 * 40 * self.width * self.height * 3))
        f.write(dword(0))
        f.write(dword(14 + 40))

        # image header 40
        f.write(dword(40))
        f.write(dword(self.width))
        f.write(dword(self.height))
        f.write(word(1))
        f.write(word(24))
        f.write(dword(0))
        f.write(dword(self.width * self.height * 3))
        f.write(dword(0))
        f.write(dword(0))
        f.write(dword(0))
        f.write(dword(0))

        for x in range(self.height):
            for y in range(self.width):
                f.write(self.framebuffer[x][y])

        f.close()

    def glViewPort(self, x, y, width, height):
        self.x = x
        self.y = y
        self.width = width - 1
        self.height = height - 1

    def glVertex(self, y, x, color):
        # x = ((((x + 1)/2) * (self.width)) + self.x)
        # y = ((((y + 1)/2) * (self.height)) + self.y)
        self.framebuffer[x][y] = color

    # La funcion de Linea es una funcion que puede dar problemas con ciertas condiciones. Por ejemplo, con la pendiente x0 != x1
    # Por esta razon estaremos utilizando la funcionalidad de Exceptions de Python
    def glLine(self, Xi, Yi, Xf, Yf):

        # Primer Cuadrante
        if Xf >= Xi & Yf >= Yi:
            try:
                print("C1")
                dY = abs(Yf - Yi)
                dX = abs(Xf - Xi)
                M = dY / dX

                steep = dY > dX

                if steep:
                    Xi, Yi = Yi, Xi
                    Xf, Yf = Yf, Xf

                    dY = abs(Yf - Yi)
                    dX = abs(Xf - Xi)
                    M = dY / dX

                offset = 0
                threshhold = 0.5

                for x in range(Xi, Xf + 1):
                    y = Yi - M * (Xi - x)
                    if steep:
                        print("Steep1")
                        r.glVertex(round(y), round(x), glColor(1, 1, 1))
                    else:
                        r.glVertex(round(x), round(y), glColor(1, 1, 1))
                    offset += M
                    if offset >= threshhold:
                        y += 1 if Yi < Yf else -1
                        threshhold += 1

            except ZeroDivisionError:
                print("ZERO1")
                for y in range(Yi, Yf + 1):
                    r.glVertex(Xf, y, glColor(1, 1, 1))

        # Segundo Cuadrante
        elif Xf < Xi & Yf > Yi:
            try:
                Xinicial = Xf
                Xfinal = Xi
                Yinicial = Yf

                print("C2")
                dY = abs(Yf - Yi)
                dX = abs(Xf - Xi)
                M = -(dY / dX)

                steep = dY > dX

                if steep:
                    Xi, Yi = Yi, Xi
                    Xf, Yf = Yf, Xf

                    dY = abs(Yf - Yi)
                    dX = abs(Xf - Xi)
                    M = dY / dX

                offset = 0
                threshhold = 0.5

                for x in range(Xinicial, Xfinal + 1):
                    y = Yinicial - M * (Xinicial - x)
                    if steep:
                        r.glVertex(round(y), round(x), glColor(1, 1, 1))
                        print("Steep2")
                    else:
                        r.glVertex(round(x), round(y), glColor(1, 1, 1))
                    offset += M
                    if offset >= threshhold:
                        y += 1 if Yi < Yf else -1
                        threshhold += 1

            except ZeroDivisionError:
                print("ZERO2")
                for y in range(Yi, Yf + 1):
                    r.glVertex(Xf, y, glColor(1, 1, 1))

        # Tercer Cuadrante
        elif Xf < Xi & Yf < Yi:
            try:
                Xinicial = Xf
                Xfinal = Xi
                Yinicial = Yf

                print("C3")
                dY = abs(Yf - Yi)
                dX = abs(Xf - Xi)
                M = dY / dX

                steep = dY > dX

                if steep:
                    Xi, Yi = Yi, Xi
                    Xf, Yf = Yf, Xf

                    dY = abs(Yf - Yi)
                    dX = abs(Xf - Xi)
                    M = dY / dX

                offset = 0
                threshhold = 0.5

                for x in range(Xinicial, Xfinal + 1):
                    y = Yinicial - M * (Xinicial - x)
                    if steep:
                        print("Steep3")
                        r.glVertex(round(y), round(x), glColor(1, 1, 1))
                    else:
                        r.glVertex(round(x), round(y), glColor(1, 1, 1))
                    offset += M
                    if offset >= threshhold:
                        y += 1 if Yi < Yf else -1
                        threshhold += 1

            except ZeroDivisionError:
                print("ZERO3")
                for y in range(Yi, Yf + 1):
                    r.glVertex(Xf, y, glColor(1, 1, 1))

        # Cuarto Cuadrante
        elif Xf > Xi & Yf < Yi:
            try:
                print("C4")
                dY = abs(Yf - Yi)
                dX = abs(Xf - Xi)
                M = -(dY / dX)

                steep = dY > dX

                if steep:
                    Xi, Yi = Yi, Xi
                    Xf, Yf = Yf, Xf

                    dY = abs(Yf - Yi)
                    dX = abs(Xf - Xi)
                    M = -(dY / dX)

                offset = 0
                threshhold = 0.5

                for x in range(Xi, Xf + 1):
                    y = Yi - M * (Xi - x)
                    if steep:
                        print("Steep4")
                        r.glVertex(round(y), round(x), glColor(1, 1, 1))
                    else:
                        r.glVertex(round(x), round(y), glColor(1, 1, 1))
                    offset += M
                    if offset >= threshhold:
                        y += 1 if Yi < Yf else -1
                        threshhold += 1

            except ZeroDivisionError:
                print("ZERO4")
                for y in range(Yi, Yf + 1):
                    r.glVertex(Xf, y, glColor(1, 1, 1))

'''
        try:
            if primero:
                print("1")
                dY = abs(Yf - Yi)
                dX = abs(Xf - Xi)
                M = dY / dX

                steep = dY > dX

                if steep:
                    Xi, Yi = Yi, Xi
                    Xf, Yf = Yf, Xf

                    dY = abs(Yf - Yi)
                    dX = abs(Xf - Xi)
                    M = dY / dX

            elif segundo:
                print("1")
                Xi = Xf
                Xf = Xi
                Yi = Yf

                dY = abs(Yf - Yi)
                dX = abs(Xf - Xi)
                M = -(dY / dX)

            elif tercero:
                print("1")
                Xi = Xf
                Xf = Xi
                Yi = Yf

                dY = abs(Yf - Yi)
                dX = abs(Xf - Xi)
                M = dY / dX

            elif cuarto:
                print("2")
                Xi = Xf
                Xf = Xi
                Yi = Yf

                dY = abs(Yf - Yi)
                dX = abs(Xf - Xi)
                M = -(dY / dX)

            offset = 0
            threshhold = 0.5

            for x in range(Xi, Xf + 1):
                y = Yi - M * (Xi - x)
                if steep:
                    print("Steep1")
                    r.glVertex(round(y), round(x), glColor(1, 1, 1))
                elif segundo:
                    print("C2")
                    r.glVertex(round(x), round(y), glColor(1, 1, 1))
                elif tercero:
                    print("C3")
                    r.glVertex(round(x), round(y), glColor(1, 1, 1))
                elif cuarto:
                    print("C4")
                    r.glVertex(round(x), round(y), glColor(1, 1, 1))
                else:
                    print("C1")
                    r.glVertex(round(x), round(y), glColor(1, 1, 1))
                offset += M
                if offset >= threshhold:
                    y += 1 if Yi < Yf else -1
                    threshhold += 1

        except ZeroDivisionError:
            print("ZERO1")
            for y in range(Yi, Yf + 1):
                r.glVertex(Xf, y, glColor(1, 1, 1))
'''

'''
        # Tercer Cuadrante
        try:
            Xinicial = Xf
            Xfinal = Xi
            Yinicial = Yf

            print("C1")
            dY = abs(Yf - Yi)
            dX = abs(Xf - Xi)
            M = dY / dX

            steep = dY > dX

            if steep:
                Xi, Yi = Yi, Xi
                Xf, Yf = Yf, Xf

                dY = abs(Yf - Yi)
                dX = abs(Xf - Xi)
                M = dY / dX

            offset = 0
            threshhold = 0.5

            for x in range(Xinicial, Xfinal + 1):
                y = Yinicial - M * (Xinicial - x)
                if steep:
                    print("Steep")
                    r.glVertex(round(y), round(x), glColor(1, 1, 1))
                else:
                    r.glVertex(round(x), round(y), glColor(1, 1, 1))
                offset += M
                if offset >= threshhold:
                    y += 1 if Yi < Yf else -1
                    threshhold += 1

        except ZeroDivisionError:
            print("ZERO")
            for y in range(Yi, Yf + 1):
                r.glVertex(Xf, y, glColor(1, 1, 1))

        # Segundo Cuadrante
        try:
            Xinicial = Xf
            Xfinal = Xi
            Yinicial = Yf

            print("C1")
            dY = abs(Yf - Yi)
            dX = abs(Xf - Xi)
            M = -(dY / dX)

            steep = dY > dX

            if steep:
                Xi, Yi = Yi, Xi
                Xf, Yf = Yf, Xf

                dY = abs(Yf - Yi)
                dX = abs(Xf - Xi)
                M = dY / dX

            offset = 0
            threshhold = 0.5

            for x in range(Xinicial, Xfinal + 1):
                y = Yinicial - M * (Xinicial - x)
                if steep:
                    r.glVertex(round(y), round(x), glColor(1, 1, 1))
                    print("Steep")
                else:
                    r.glVertex(round(x), round(y), glColor(1, 1, 1))
                offset += M
                if offset >= threshhold:
                    y += 1 if Yi < Yf else -1
                    threshhold += 1

        except ZeroDivisionError:
            print("ZERO")
            for y in range(Yi, Yf + 1):
                r.glVertex(Xf, y, glColor(1, 1, 1))
        
        
        # Primer Cuadrante
        while Yf >= Yi:
            try:
                print("C1")
                dY = abs(Yf - Yi)
                dX = abs(Xf - Xi)
                M = dY / dX

                steep = dY > dX

                if steep:
                    Xi, Yi = Yi, Xi
                    Xf, Yf = Yf, Xf

                    dY = abs(Yf - Yi)
                    dX = abs(Xf - Xi)
                    M = dY / dX

                offset = 0
                threshhold = 0.5

                for x in range(Xi, Xf + 1):
                    y = Yi - M * (Xi - x)
                    if steep:
                        print("Steep")
                        r.glVertex(round(y), round(x), glColor(1, 1, 1))
                    else:
                        r.glVertex(round(x), round(y), glColor(1, 1, 1))
                    offset += M
                    if offset >= threshhold:
                        y += 1 if Yi < Yf else -1
                        threshhold += 1

            except ZeroDivisionError:
                print("ZERO")
                for y in range(Yi, Yf + 1):
                    r.glVertex(Xf, y, glColor(1, 1, 1))

            break

        # Cuarto Cudrante
        while Xf > Xi & Yf < Yi:
            try:
                print("C2")
                dY = abs(Yf - Yi)
                dX = abs(Xf - Xi)
                M = -(dY / dX)

                steep = dY > dX

                if steep:
                    Xi, Yi = Yi, Xi
                    Xf, Yf = Yf, Xf

                    dY = abs(Yf - Yi)
                    dX = abs(Xf - Xi)
                    M = -(dY / dX)

                offset = 0
                threshhold = 0.5

                for x in range(Xi, Xf + 1):
                    y = Yi - M * (Xi - x)
                    if steep:
                        print("Steep2")
                        r.glVertex(round(y), round(x), glColor(1, 1, 1))
                    else:
                        r.glVertex(round(x), round(y), glColor(1, 1, 1))
                    offset += M
                    if offset >= threshhold:
                        y += 1 if Yi < Yf else -1
                        threshhold += 1

            except ZeroDivisionError:
                print("ZERO2")
                for y in range(Yi, Yf + 1):
                    r.glVertex(Xf, y, glColor(1, 1, 1))


            break
'''

r = Line(800, 600, 0, 0)

r.KRyuLine(165, 380, 185, 360)
r.KRyuLine(180, 330, 207, 345)
'''
r.KRyuLine(233, 330, 230, 360)
r.KRyuLine(250, 380, 220, 385)
r.KRyuLine(205, 410, 193, 383)
'''

r.glVertex(165, 380, glColor(1,1,1))
r.glVertex(185, 360, glColor(1,1,1))
r.glVertex(180, 330, glColor(1,1,1))
r.glVertex(207, 345, glColor(1,1,1))
"""
r.glVertex(233, 330, glColor(1,1,1))
r.glVertex(230, 360, glColor(1,1,1))
r.glVertex(250, 380, glColor(1,1,1))
r.glVertex(220, 385, glColor(1,1,1))
r.glVertex(205, 410, glColor(1,1,1))
r.glVertex(193, 383, glColor(1,1,1))
"""

r.write("Plygon.bmp")