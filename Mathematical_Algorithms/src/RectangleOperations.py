
class Rectangle:
    
    def __init__(self, coord_x,coord_y,width,height):
        '''
        Construct
        Define the coordenates of the rectangle
        '''
        self.x=coord_x
        self.y=coord_y
        self.dx=width
        self.dy=height
        self.ymax = coord_y + width
        self.xmax = coord_x + height

        

    def writer(self):
        '''
        rectangle representation
        returns the starting coordenates of the rectangle and also its width and height
        '''
        return "Rectangle(%s, %s, %s, %s)" % (self.x, self.y, self.dx, self.dy)

        
        
    def intersect(self, other):
        ''' 
        Returns True if object intersects the rectangle
        '''
        
        # Checks if the coordinates of the first rectangle intersect with the coordinates of the new object
        if (self.ymax<other.y or other.ymax<self.y) or (self.xmax<other.x or other.xmax<self.x):
            return False
        else:
            return True



    def soma(self,other):
        '''
        Return the smaller rectangle that contains both the object and the rectangle
        '''
        #Defines the minimal x and y coordinate between both objects, does the same to the max coordinate
        xmin = min(self.x,other.x)
        ymin = min(self.y,other.y)
        xmax = max(self.xmax, other.xmax)
        ymax = max(self.ymax, other.ymax)
        #Defines the width and height of the new rectangle
        w = xmax - xmin
        h = ymax - ymin
        #Defines the new rectangle
        ret3 = Rectangle(xmin,ymin, w, h)
        return ret3



    def multiply(self,other):
        '''
        Returns a new rectangle that contains the intersection
        between the rectangle and the object
    
        if self.interset(rect) = False, writer "There is no intersection"
        and returns null
        '''
        
        #Checks if the intersection between both rectangles happens
        if(self.intersect(other)== True):
            #if true, then finds the maximum x and y coordinate between both objects, and the minimal ymax and xmax
            x = max(self.x, other.x)
            y = max(self.y,other.y)
            xmax = min(self.xmax, other.xmax)
            ymax = min(self.ymax, other.ymax)
            #calculates the width and height
            w = xmax - x
            h = ymax - y
            #defines new rectangle
            r3 = Rectangle(x,y,w,h)
            return r3
        else:
            return 'There is no intersection'
         
         


def main():
    '''
    tests
    '''
    
    #two rectangles
    r1 = Rectangle(0,0,10,10)
    r2 = Rectangle(5,2,7,9)
    #see their representation
    r1es1 = r1.writer()
    r2es1 = r2.writer()
    #know the smaller rectangle between 
    t1=r1.soma(r2)
    #write new rectangle
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
    
