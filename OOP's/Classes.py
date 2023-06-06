# How is class and its object called
class Sample():
    pass            # pass is used to get no error when u want to keep its field empty

my_sample = Sample()    #object of Sample() created ad my_sample
type(my_sample)         #type of this object belongs to or is __main__.Sample

# example 1
class Car():
    
    def __init__(self,price):    #constructor of class   
        self.price = price        #self keyword - to instantiate or call an instance of the class || defined as (The self parameter is a reference to the current instance of the class, and is used to access variables that belongs to the class)

my_car = Car(price  = 10000)
my_car.price

# output : 10000

#example 2

class Car():
    def __init__(self,price,name,rank):
        self.price = price
        self.name = name
        self.rank = rank

my_car = Car(price = '1000', name = 'subaru',rank = 'A')
my_car.name
my_car.price
my_car.rank


# Area of circle using classes and objects
# example 3
class AreaOfCircle():
    pi = 3.14
    
    def __init__(self,r):
        self.r = r
        
    def area(self):
        area = self.pi*self.r*self.r
        return area
    
    def circum(self):
        circumference = 2*self.pi*self.r
        return circumference
    
circ = AreaOfCircle(10)
circ.area()
#o/p 314
circ.circumference()
#o/p 62.8


