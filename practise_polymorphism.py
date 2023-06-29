'''polymorphism :::::::::
means two words contain poly means many and morphs means many
by polymorphism we understand that one task can be performed by many form or different ways
FOR EXAMPLE::::YOU HAVE CLASS ANIMAL AND ALL ANIMAL ARE SPEAK  but they speak diferently ....here the speak behaviour is polymorphic in a sense and depend on the animal so the obstract animal 
  does not actually "speak" but specific animals like(cat and dogs) have a concrete implementation of the action speak'''
  
  
#polymorphism with for loop

# class Car():
#     def bmw(self):  # when function pass sekf argument then this we called method()
#         print("This is a German company ")
#     def audi(self): 
#         print("This is a England company ")
#     def polo(self):
#         print("This is a British company ")
# #here we create next truck class and
# class Truck():
#     def bmw(self): 
#         print("This is a Indian company ")
#     def audi(self):
#         print("This is a italian company ")
#     def polo(self):
#         print("This is a Japnese company")
        
# #create a class objectt
# c=Car()
# t= Truck()

# #here we use for loop
# for i in (c,t):   # in a place i we also use another word means if in this ex we information about country so we use here country word
#     i.bmw()
#     i.audi()
#     i.polo()

##*****polymorphism with inheritance******#### -*- coding=utf-8 -*-

#firstly we create class 
# class Car():
#     def gear(self):
#         print("every car has 5 gears")
#     def wheel(self):
#         print("every car has 4 wheels")
# #now we create two class inherit parent base class "car"

# class Bmw(Car):
#     def wheel(self):
#         print("every Bmw bike  has 2 wheels")
        
# class Audi(Car):
#     def wheel(self):
#         print("every Audio has 4 wheels")
        
# #noe we create object of a every class inherit parent base class

# c=Car()
# b=Bmw()
# a= Audi()

# #now we call the object::
# a.wheel()
# a.gear()

# b.wheel()
# b.gear()

# c.wheel()
# c.gear()

# ####poly with functions
# class Car():
#     def bmw(self):
#         print('The german company')
#     def audi(self):
#         print('The French Company')
#     def Polo(self):
#         print('The UK company')

# class Truck():
#     def bmw(self):
#         print('The american company')
#     def audi(self):
#         print('The Italian company')
#     def Polo(self):
#         print('The Indian company')

# # def fun(car):
# #    Car.audi()
# #    Car.polo()
# #    Car.bmw()
   
   


# def fun(car):
#     car.bmw()
#     car.audi()
#     car.Polo()

# c = Car()  #we create the object
# t = Truck()

# fun(c)   ##we call the fun
# fun(t) 


'''poly morphism ssignment'''

#1) polymorphism with class method we create for loop that iterate through a tuuple of obj then call the method without being concerned about which class tape each obj is this method actually exist in each class?

# # now we create India class
# class India():
#     def Capital(self):
#         print("New Delhi is the capital of India")
        
#     def Langauge(self):
#         print("Hindi is the most widely spoken langauge in india")
#     def Type(self):
#         print("India is a devloping country")
        
# class USA():
#     def Capital(self):
#         print("Washington is the capital of USA")
#     def Langauge(self):
#         print(" English is the primary langauge of USA ")
        
#     def Type(self):
#         print("USA is the developed country of the world")
        
# #now we create object india and usa

# obj_india = India()
# obj_usa= USA()

# # here we for loop use
# for i in (obj_india, obj_usa):
#     i.Capital()
#     i.Langauge()
#     i.Type()
    
    
#2)Take a bird and class and inherit their properties by through polymorphism with ineritance?

# class Bird():
#     def introduction(self):
#         print(" Ther are many types od birds: ")
#     def flight(self):
#         print("most of the birds can fly but somr cannot fly: ")
        
# class Sparrow(Bird):
#     def flight(self):
#         print("Sparrow can fly")
# class Ostrich(Bird):
#     def flight(self):
#         print("Sparrow can  not fly")
        
# #now we create obj above all classes:
# bird = Bird()
# sparrow= Sparrow()
# ostrich = Ostrich()

# # after creatioon of the object we call the object::

# bird.introduction()
# bird.flight()

# sparrow.introduction()
# sparrow.flight()

# ostrich.introduction()
# ostrich.flight()
    
    
    
    
#3)Create a two class India and USA and create instantation of both the india and   USA classes if we do not have them already
#  with those we can call their action using the same fun() here we polymorphism with fubnctions and object?

# class India():
#     def Capital(self):
#         print("New Delhi is the capital of India")
        
#     def Langauge(self):
#         print("Hindi is the most widely spoken langauge in india")
#     def Type(self):
#         print("India is a devloping country")
        
# class USA():
#     def Capital(self):
#         print("Washington is the capital of USA")
#     def Langauge(self):
#         print(" English is the primary langauge of USA ")
        
#     def Type(self):
#         print("USA is the developed country of the world")
        
# # we create a function 
# def func(obj):
#     obj.Capital()
#     obj.Langauge()
#     obj.Type()
    
# obj_ind = India()
# obj_usa =USA()

# func(obj_ind)
# func(obj_usa)


#4) Explain the polymorphism with for loop cat and dog their information and make a sound properties displya through method?

#firstly we create a class cat:
class cat():
    def info(self):
        print(" I am a Cat and my name is kitty")
    def make_sound(self):
        print(" Cat sound like Meow-meow")
        
#secodly we create dog class info about dog:
class Dog():
    def info(self):
        print(" I am a Dog and my name is puppy")
    def make_sound(self):
        print(" Dog sound like Bark")
        
#create object:
c= cat()
d = Dog()

for animals in (c,d):
    c.info()
    c.make_sound()
    
    d.info()
    d.make_sound()