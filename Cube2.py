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

        try:
            pendiente = ((Yf - Yi)/(Xf - Xi))
        except:
            pendiente = 0

        # Primer Cuadrante
        if (Xi <= Xf) and (Yi <= Yf):
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
        elif (Xi > Xf) and (Yi <= Yf):
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
        if (Xi > Xf) and (Yi > Yf):
            Xi, Xf = Xf, Xi
            Yi, Yf = Yf, Yi
            try:
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

                for x in range(Xi, Xf + 1):
                    y = Yi - M * (Xi - x)
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
        if (Xi <= Xf) and (Yi > Yf):
            #Yi, Yf = Yf, Yi
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
                for y in range(Yf, Yi + 1):
                    r.glVertex(Xf, y, glColor(1, 1, 1))

r = Bitmap(800, 800, 0, 0)

r.glLine(200, 200, 287, 250)
r.glLine(200, 200, 113, 250)
r.glLine(200, 200, 200, 300)
r.glLine(287, 250, 287, 350)
r.glLine(113, 250, 113, 350)
r.glLine(200, 300, 287, 350)
r.glLine(200, 300, 113, 350)
r.glLine(287, 350, 200, 400)
r.glLine(113, 350, 200, 400)

r.write("Cube2.bmp")