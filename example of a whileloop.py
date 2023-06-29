# sum = 0
# i = 0
# while i < 10 :
#     sum = sum + i
    
#     print (sum)
    
#     i=i+1
# for i in range (10):
#      sum = sum +i
#      print(sum)

# n=5
# while n> 0:
#     n=n-1
#     if n==2:
#          break
#     print(n)
# print('loop is finished')

# n=100
# while  n >=0:
#     n= n-10
#     if n==20:
#         break
#     print(n)

# '''continue statement using while loop'''
# x=1
# while x<10 :
#     print(x)
#     x= x+1
#     if x==5:
#         continue
    
    
# x=10
# while x<100:
#     print(x)
#     x=x+1
#     if x==20:
#         continue
  

# n=20   #iterating 20 whole table
# i=1
# while i<=10:
#     print(f ' {n} X {i}={n*i}')
    
    # i=i+1

# n=5
# i=1
# while i<=20:
    
#     print (f'{n} x {i} = {n * i}')     
    
#     i=i+1

#*****
# list1=[]
# list2=[]

# for i in range(0,10):
#     if (i%2==0):
#         list1.append(i**2)
#     else:
#         list2.append(i**3)
        
# print(list1)
# print(list2)

# list1=[]
# list2=[]
# for i in range (1,10):
#     if (i%2==0):
#         list1.append(i**2)
#     else:
#         list2.append(i**3)
# print(list1)
# # print(list2)
# ''' while loop'''

# def print_msg(count,msg):
    
#     while count> 0:
#         print(msg)
        
#         count -= 1
        
# print_msg(10,"hello world")

# a=10
# i=5
# while i<= a:
#     a-= 1
#     if a==7:
#         print("a was equal to 7")
        
#         continue
#     print(a)


# i=10
# while i> 0:
#     i = i -1
#     if i ==2:
#         continue
#     print("inside loop",i)
# else:
#     print("inside else")


# '''if else'''
# age = 20

# if age < 18:
#     print("you can not vote")
    
# else:
#     print("you can vote and")
# ''''''
# m=3
# n=8

# while (m<8):
#     print("ïterate_value:",m)
    
#     m= m+1
#     if (m==7):
#         break
#     print("loop will iterated")


# iterate through a list

# colors=['red','yellow','blue','black']

# for x in colors:
#     print(x)

#iterate through a string

# s="vijaya"
# for  x in s:
#     print(x)

#insert at the start

# x= ['a','b','c','d']

# x[ :0] =[1,2,3]
# print(x)

#insert at the end
# x=['a','b','c','d']
# x[len(x): ] =[1,2,3]
# print(x)


for num in range (-2,-5,-1):
    print(num,end=" ,")


num=[10,20]
items =["chair","table"]