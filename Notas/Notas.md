# Notas

## Sobre Clases
If the first line after the class header is a string, it becomes the docstring of the class, and will be recognized by various tools. (This is also the way docstrings work in functions.)

    class Point:
        """ Point class for representing and manipulating x,y coordinates. """

        def __init__(self):
            """ Create a new point at the origin """
            self.x = 0
            self.y = 0 

Nota: *pass* statement : In Python programming, the pass statement is a null statement. The difference between a comment and a pass statement in Python is that while the interpreter ignores a comment entirely, pass is not ignored.

`pass`

We generally use it as a placeholder.
Suppose we have a loop or a function that is not implemented yet, but we want to implement it in the future. They cannot have an empty body. The interpreter would give an error. So, we use the pass statement to construct a body that does nothing.

    '''pass is just a placeholder for
    functionality to be added later.'''
    sequence = {'p', 'a', 's', 's'}
    for val in sequence:
        pass

We can do the same thing in an empty function or class as well.

    def function(args):
        pass

    class Example:
        pass


Every class should have a method with the special name __init__. This initializer method, often referred to as the **constructor**, is automatically called whenever a new instance of Point is created. It gives the programmer the opportunity to set up the attributes required within the new instance by giving them their initial state values. The self parameter (you could choose any other name, but nobody ever does!) is automatically set to reference the newly created object that needs to be initialized.

During the initialization of the objects, we created two attributes called x and y for each object, and gave them both the value 0. You will note that when you run the program, nothing happens. It turns out that this is not quite the case. In fact, two Points have been created, each having an x and y coordinate with value 0. However, because we have not asked the program to do anything with the points, we don’t see any other result.

    class Point: 
    """Point class for representing and manipulating x,y coordinates. """
    def __init__(self):
            self.x = 0
            self.y = 0
    p = Point()         # Instantiate an object of type Point
    q = Point()         # and make a second point
    print(p)
    print(q)
    print (p is q)
`<__main__.Point object>`

`<__main__.Point object>`

`False`

A function like Point that creates a new object instance is called a constructor. Every class automatically uses the name of the class as the name of the constructor function. The definition of the constructor function is done when you write the __init__ function (method) inside the class definition

The combined process of “make me a new object” and “get its settings initialized to the factory default settings” is called ***instantiation***.

### Adding Paramters to the constructor
We can make our class constructor more generally usable by putting extra parameters into the __init__ method, as shown in this example.
    class Point:
    """ Point class for representing and manipulating x,y coordinates. """

    def __init__(self, initX, initY):

        self.x = initX
        self.y = initY
    p = Point(7,6)

Now when we create new points, we supply the x and y coordinates as parameters. When the point is created, the values of initX and initY are assigned to the state of the object, in the instance variables x and y.

This is a common thing to do in the __init__ method for a class: take in some parameters and save them as instance variables. Why is this useful? Keep in mind that the parameter variables will go away when the method is finished executing. The instance variables, however, will still be accessible anywhere that you have a handle on the object instance. This is a way of saving those initial values that are provided when the class constructor is invoked.

1. Create a class called NumberSet that accepts 2 integers as input, and defines two instance variables: num1 and num2, which hold each of the input integers. Then, create an instance of NumberSet where its num1 is 6 and its num2 is Save this instance to a variable t.

        class NumberSet:
        def __init__(self,a:int,b:int):
            self.num1=a
            self.num2=b
            
        def sum(self):
            t=self.num1 + self.num2
            
        t=NumberSet(6,10)
        print(t.sum())

### Adding other methods to a class
The key advantage of using a class like Point rather than something like a simple tuple (7, 6) now becomes apparent. We can add methods to the Point class that are sensible operations for points. Had we chosen to use a tuple to represent the point, we would not have this capability. Creating a class like Point brings an exceptional amount of “organizational power” to our programs, and to our thinking. We can group together the sensible operations, and the kinds of data they apply to, and each instance of the class can have its own state.

A method behaves like a function but it is invoked on a specific instance. For example, with a list bound to variable L, L.append(7) calls the function append, with the list itself as the first parameter and 7 as the second parameter. Methods are accessed using dot notation. This is why L.append(7) has 2 parameters even though you may think it only has one: the list stored in the variable L is the first parameter value and 7 is the second.

    class Point:
    """ Point class for representing and manipulating x,y coordinates. """

    def __init__(self, initX, initY):

        self.x = initX
        self.y = initY

    def getX(self):
        return self.x

    def getY(self):
        return self.y
    p = Point(7,6)
    print(p.getX())
    print(p.getY())

### Instance Variable Search Order

### Example: Creating Instances from Data

poemdo hacer un instance method  
    def __str(self) __:

no puede ayudar a que en vez de imrpirmir a clase del objeto puede devolver información sobre el instance method creado.
 Esto es convertir el objeto a un string.s

    class Cereal:
    def __init__(self,str1:str,str2:str,num1:int):
        self.name = str1
        self.brand = str2
        self.fiber = num1
        
    def __str__(self):
        return ("{} cereal is produced by {} and has {} grams of fiber in every serving!".format(self.name,self.brand,self.fiber))
    
    c1 = Cereal("Corn Flakes","Kellogg's",2)
    c2 = Cereal("Honey Nut Cheerios","General Mills",3)
    print (c1)
    print(c2)

### Objects as Arguments and Parameters
You can pass an object as an argument to a function, in the usual way.

Here is a simple function called distance involving our new Point objects. The job of this function is to figure out the distance between two points.

    import math

    class Point:
    """ Point class for representing and manipulating x,y coordinates. """

    def __init__(self, initX, initY):

        self.x = initX
        self.y = initY

    def getX(self):
        return self.x

    def getY(self):
        return self.y

    def distanceFromOrigin(self):
        return ((self.x ** 2) + (self.y ** 2)) ** 0.5

    def distance(point1, point2):
        xdiff = point2.getX()-point1.getX()
        ydiff = point2.getY()-point1.getY()

        dist = math.sqrt(xdiff**2 + ydiff**2)
        return dist

        p = Point(4,3)
        q = Point(0,0)
        print(distance(p,q))

`distance` takes two points and returns the distance between them. Note that distance is not a method of the Point class.

____
## Makefile

## Pytest

What is Pytest?
pytest is framework that makes buildin simple and scalable test esay.

**¿Qué es un framework?**
    
    Un framework es un esquema o marco de trabajo que ofrece una estructura base para elaborar un proyecto con objetivos específicos, una especie de plantilla que sirve como punto de partida para la organización y desarrollo de software.
Ver más [aquí](https://docs.pytest.org/en/6.2.x/usage.html)

In general, pytest is invoked with the command pytest (see below for other ways to invoke pytest). This will execute all tests in all files whose names follow the form test_*.py or \*_test.py in the current directory and its subdirectories. More generally, pytest follows standard test discovery rules.

## pytest commands

[Ver esto](https://programmerclick.com/article/3366908761/)

**Uso básico**

    py.test [options] [file_or_dir] [file_or_dir] [...]

_____
pyest is for runnin test
mypy for check type hints
flake8 for cehcking style

src: "source" 

En el minuto 14:00 habla sobre 'fixture' -no me queda claro que es un fixture
ni el scope

tox: otra herramienta de testing

FitHub actiosn corre tox automáticamente

____
## Mutantes

[Mutation testing](https://searchitoperations.techtarget.com/definition/mutation-testing#:~:text=Mutation%20testing%2C%20also%20known%20as,cause%20errors%20in%20the%20program.)

- ¿Qué son los mutantes?

- ¿Cómo los cazamos?

- ¿Por qué son importantes?






Mutation testing, also known as code mutation testing, is a form of white box testing in which testers change specific components of an application's source code to ensure a software test suite will be able to detect the changes. Changes introduced to the software are intended to cause errors in the program. Mutation testing is directed to ensure the quality of a software testing suite, not the applications the suite will go on to test.

**Unit Test:** 
> UNIT TESTING is a type of software testing where individual units or components of a software are tested. The purpose is to validate that each unit of the software code performs as expected. Unit Testing is done during the development (coding phase) of an application by the developers


____

## Radian

Ver [esto](https://github.com/REditorSupport/vscode-R/wiki/Installation%3A-Windows)
 y [esto](https://www.infoworld.com/article/3625488/how-to-run-r-in-visual-studio-code.html)

radian version: 0.5.13
r executable: C:\Program Files\R\R-4.1.2\bin\R
r version: 4.1.2
python executable: C:\Users\Fernando\anaconda3\python.exe
python version: 3.9.7

To locate the path to radian.exe, run the following command:

> where.exe radian