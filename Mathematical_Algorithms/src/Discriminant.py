#Code by MASTER-FURY
def discriminant(a, b, c): 
  
    discriminant = (b**2) - (4*a*c) 
    if discriminant > 0: 
          
        print('Discriminant is', discriminant, 
                "which is Positive") 
                  
        print('Hence Two Solutions') 
          
    elif discriminant == 0: 
          
        print('Discriminant is', discriminant,  
                "which is Zero") 
                  
        print('Hence One Solution') 
          
    elif discriminant < 0: 
          
        print('Discriminant is', discriminant,  
                "which is Negative") 
                  
        print('Hence No Real Solutions') 
  
# Driver Code 
a = 20
b = 30
c = 10
discriminant(a, b, c) 
