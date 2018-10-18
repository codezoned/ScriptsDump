
class Rectangle:
    
    def __init__(self, coord_x,coord_y,largura,altura):
        '''
        Construct
        '''
        self.x=coord_x
        self.y=coord_y
        self.dx=largura
        self.dy=altura
        self.ymax = coord_y + altura
        self.xmax = coord_x + largura

        

    def writer(self):
        '''
        rectangle representation
        '''
        return "Rectangle(%s, %s, %s, %s)" % (self.x, self.y, self.dx, self.dy)

        
        
    def intersect(self, other):
        '''    
        Returns True if object intersects the rectangle
        '''
        
        if (self.ymax<other.y or other.ymax<self.y) or (self.xmax<other.x or other.xmax<self.x):
            return False
        else:
            return True



    def soma(self,other):
        '''
        Return the smaller rectangle that contains both the object and the rectangle
        '''
        xmin = min(self.x,other.x)
        ymin = min(self.y,other.y)
        xmax = max(self.xmax, other.xmax)
        ymax = max(self.ymax, other.ymax)
        h = xmax - xmin
        w = ymax - ymin
        ret3 = Rectangle(xmin,ymin, h, w)
        return ret3



    def multiply(self,other):
        '''
        Returns a new rectangle that contains the intersection
        between the rectangle and the object
    
        if self.interset(rect) = False, writer "There is no intersection"
        and returns null
        '''
        if(self.intersect(other)== True):
            x = max(self.x, other.x)
            y = max(self.y,other.y)
            xmax = min(self.xmax, other.xmax)
            ymax = min(self.ymax, other.ymax)
            h = xmax - x
            w = ymax - y
            r3 = Rectangle(x,y,h,w)
            return r3
        else:
            return 'There is no intersection'
         
         


def main():
    r1 = Rectangle(0,0,10,10)
    r2 = Rectangle(5,2,7,9)
    r1es1 = r1.writer()
    r2es1 = r2.writer()
    t1=r1.soma(r2)
    t1es1 = t1.writer()
    r1intr2 = r1.intersect(r2)
    t2=r1.multiply(r2)
    t2es1 = t2.writer()
    r3=Rectangle(20,20,10,10)
    r1.writer()
    r3es1 = r3.writer()
    r1.intersect(r3)
    t3 = r1.multiply(r3)
    return r1es1, r2es1, t1es1, r1intr2, t2es1, r3es1, t3


if __name__ == '__main__':
    print(main())
    