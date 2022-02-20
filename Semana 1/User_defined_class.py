class Point:
   
   def __init__(self,x,y):
       self.x = x
       self.y = y       
       
   
   def getx(self):
        return self.x
        # This is a method. One difference between a
        # method and a function is that methods alwaysways hace at least one argument.
        

point1 = Point(4,10)  # this is an instace of the point class
point2 = Point(2,6) 

#point1.x = 5  # this is an instance variable
#point2.x = 10

print("\npoint1", point1.getx())

# ¿Qué significa el self? ¿Por que regreso 5?
# Digamos quee l self hace que una instancia se pase  sí misma por el método.
# en este caso la intanica 'point1.x' se pasa al metodo 'getX()'
#  

