import numpy as np
from utils import vector, safediv

class Field:
    def __init__(self,fieldsize):
        self.fieldsize = fieldsize
        self.field = np.zeros((fieldsize,fieldsize))

    def setPoint(self,x,y,val):
        self.field[y,x] = val

    def getPoint(self,x,y):
        return self.field[x,y]

    #places a specified value into a trapezoid described by two vectors
    #vectors must have same origin
    def setRect(self,vector1,vector2,value):
        for i in range(int(vector1.length)):
            xv1 = vector1.xorigin + i * safediv(vector1.x,vector1.length)
            yv1 = vector1.yorigin + i * safediv(vector1.y,vector1.length)
            for j in range(int(vector2.length)):
                xv2 = int(xv1 + j * safediv(vector2.x,vector2.length))
                yv2 = int(yv1 + j * safediv(vector2.y,vector2.length))
                if xv2 < self.fieldsize and yv2 < self.fieldsize:
                     self.setPoint(xv2,yv2,value)
    

    # def mapPointsFromSquare(self,square,bottompoint,width,stretch_y,stretch_top):
        
    def read(self):
        #map vision shit into matrix
        #*****************************

    def printfield(self):
        for i,column in enumerate(self.field):
            line = ""
            for j, row in enumerate(self.field[i]):
                if self.field[i][j] == 0:
                    line += ",*"
                else:
                    #colors not implemented yet
                    line += ","+str(int(self.field[i][j]))
            print(line)
            

# f = fieldmodel(20)
# f.setRect(vector(5,9,10,2),vector(5,9,5,5),1)
# f.printfield()

