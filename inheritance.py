'''single inheritance
 When a child class inherits from only one parent class, it is called single inheritance.'''


# class parent1():
#     def __init__(self):
#         self.name = 'Aditya'
#         self.age = 20

#     def call2(self):
#         print('the name is',self.name,'age is',self.age)

# class child1(parent1):
#     def __init__(self):
#         parent1.__init__(self)

#     def call1(self):
#         print(self.name,self.age)

# c = child1()
# c.call1()
# c.call2()



# class animal():
#     def __init__(self):
#         pass
#     def speak(self):
#         print('animal speaking')

# class dog(animal):
#     def __init__(self):
#         animal.__init__(self) 
#     def bark(self):
#         print('dog barking')

# d = dog()
# d.bark()
# d.speak()



# class first():
#     def __init__(self):
#         self.bikename = 'BMW'
#         self.bikeage = 5

# class second(first):
#     def __init__(self):
#         first. __init__(self)
#     def call1(self):
#         print(self.bikename,self.bikeage)

# c = second()
# c.call1()



# class first():
#     def __init__(self):
#         self.bikename ='BMW'
#         self.bikeage = 5
        
# class second(first):
#     def __init__(self):
#         first. __init__(self)
#     def call1(self):
#         print(self.bikename)

# class third(first):
#     def __init__(self):
#         first. __init__(self)
#     def call2(self):
#         print(self.bikeage)

# c = second()
# c.call1()

# d = third()
# d.call2()
        


'''Multiple Inheritance 
 When a child class inherits from multiple parent classes, it is called multiple inheritance. '''


# class father():
#     def __init__(self):
#         self.fathername = 'Maxgen'

# class mother():
#      def __init__(self):
#         self.mothername = 'Max'


# class child(father,mother):
#     def __init__(self):
#         father.__init__(self)
#         mother.__init__(self)

#     def show(self):
#         print('The father name is',self.fathername)
#         print('the mothername is',self.mothername) 

# c = child()
# c.show()


# class father():
#     def __init__(self):
#         self.fathername = 'Maxgen'

# class mother():
#     def __init__(self):
#         self.mothername = 'Max'

# class child(father,mother):
#     def __init__(self):
#         father.__init__(self)
#         mother.__init__(self)
#         self.gname = 'Python'

#     def show(self):
#         print('The father name is',self.fathername)
#         print('the mothername is',self.mothername) 

#     def fun(self):
#         print(self.gname)
# c = child()
# c.show()
# c.fun()


# class first():
#     def __init__(self):
#         self.bikename = 'BMW'

# class second():
#     def __init__(self):
#         self.bikeage = 5

# class third():
#     def __init__(self):
#         self.model = 'AT-1800'

# class child(first,second,third):
#     def __init__(self):
#         first. __init__(self)
#         second. __init__(self)
#         third. __init__(self)
#     def max(self):
#         print('the bikename is',self.bikename)
#         print('the bikeage is',self.bikeage)
#         print('the bikemodel is',self.model)

# c = child()
# c.max()


'''Multilevel
When we have a child and grandchild relationship. '''

# class Parent:
#     def __init__(self,name):
#         self.name = name
#     def getName(self):
#         return self.name

# class Child(Parent):
#     def __init__(self,name,age):
#         Parent.__init__(self,name)
#         self.age = age
#     def getAge(self):
#         return self.age

# class Grandchild(Child):
#     def __init__(self,name,age,location):
#         Child.__init__(self,name,age)
#         self.location=location
#     def getLocation(self):
#         return self.location
# gc = Grandchild("Srinivas",24,"Hyderabad")
# print(gc.getName(), gc.getAge(), gc.getLocation())



# class Grandfather:
 
#     def __init__(self, grandfathername):
#         self.grandfathername = grandfathername


# class Father(Grandfather):
#     def __init__(self, fathername, grandfathername):
#         self.fathername = fathername
 
#         Grandfather.__init__(self, grandfathername)
 

# class Son(Father):
#     def __init__(self,sonname, fathername, grandfathername):
#         self.sonname = sonname
 
#         Father.__init__(self, fathername, grandfathername)
 
#     def print_name(self):
#         print('Grandfather name :', self.grandfathername)
#         print("Father name :", self.fathername)
#         print("Son name :", self.sonname)
 
# s1 = Son('Prince', 'Rampal', 'Lal mani')
# # print(s1.grandfathername)
# s1.print_name()



# class employee:
#     def __init__(self,employeename):
#         self.employeename = employeename
        
# class father(employee):
#     def __init__(self,age,employeename):
#         self.age = age
#         employee.__init__(self,employeename)
        
# class son(father):
#     def __init__(self,salary,age,employee):
#         self.salary = salary
#         father.__init__(self,age,employee)
        
#     def show(self):
#         print('employee salary is: ',self.salary)
#         print('employee age is: ',self.age)
#         print('employee name is: ',self.employeename)
        
# o = son('10000','25','riya')
# o.show()
