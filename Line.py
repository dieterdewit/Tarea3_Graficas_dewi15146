import struct
from random import randint

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
    color = bytes ([r, g, b])
    return color

class Line(object):
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
            for x in range(self.height)
        ]   
        
    def write(self, filename):
        f = open(filename, "bw")

		#file header
        f.write(char('B'))
        f.write(char('M'))
        f.write(dword(14 * 40 * self.width * self.height * 3))
        f.write(dword(0))
        f.write(dword(14 + 40))

		#image header 40
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

    def glVertex(self, x, y, color):
        #x = ((((x + 1)/2) * (self.width)) + self.x)
        #y = ((((y + 1)/2) * (self.height)) + self.y)
        self.framebuffer[x][y] = color

# La funcion de Linea es una funcion que puede dar problemas con ciertas condiciones. Por ejemplo, con la pendiente x0 != x1
# Por esta razon estaremos utilizando la funcionalidad de Exceptions de Python 
    def KRyuLine(self, Xi, Yi, Xf, Yf):

        try: 
            dY = abs(Yf - Yi)
            dX = abs(Xf - Xi)
            M = dY / dX

            for x in range (Xi, Xf + 1):
                y = Yi - M * (Xi - x)
                r.glVertex(round(x), round(y), glColor(1, 1, 1))
        
        except ZeroDivisionError:
            for x in range (Xi, Xf + 1):
                r.glVertex(x, Yf, glColor(1, 1, 1))


    '''            
    def glLine(self, x0, y0, x1, y1):
        dy = abs(y1 -y0)
        dx = abs(x1 -x0)
        m = dy/dx

        steep = dy > dx

        if steep:
            x0, y0 = y0, x0
            x0, y0 = y0, x0

            dy = abs(y1 - y0)
            dx = abs(x1 - x0)
            m = dy/dx

        offset = 0
        threshold = 0.5

        y = y0

        for x in range (x0, x1 + 1):
            y = y0 - m * (x0 - x)
            if steep:
                r.glVertex(round(y), round(x), glColor(1,1,1))
            else: 
                r.glVertex(round(x), round(y), glColor(1,1,1))
            offset += m
            if offset >= threshold:
                y += 1 if y0 < y1 else - 1
                threshold += 1
        '''

r = Line(800, 600, 0, 0)

r.KRyuLine(10, 10, 510, 10)
'''
r.KRyuLine(10, 10, 462, 191)
r.KRyuLine(10, 10, 354, 354)
r.KRyuLine(10, 10, 191, 462)
r.KRyuLine(10, 10, 10, 510)
'''

r.write("Line.bmp")