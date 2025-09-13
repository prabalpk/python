# print("hello")
# n = int(input("enter a number: "))
# m= int(input("enter a range: "))
# i = 1
# while (i<=m) :
#     print(n,"X",i,"=",n*i)
#     i = i+1

# a1 = [1,2,3,4,5]
# print(a1[0])

# nums = []
# i= 1
# n = int(input("enter a number: "))
# while(i<=n):

#     nums.append((i*i)+1)

#     i = i+1
# print (nums)

# list = [1,4,9,16,25,36,49,64,81,100]
# i = 0
# while(i<len(list) ):
#     print(list[i])
#     i = i+1
    # if(i==len(list)):
    #     break       
    # if(a%2==0):
    #     print(a)

# tuple = (1,4,9,16,25,36,49,64,81,100)

# x = int(input("enter a number to search: "))
# i = 0
# while(i<len(tuple) ):
#     if(x==tuple[i]):
#         print(x,"found at index",i)
#         break
    
    # else : 
    #     print("finding...")
  #  i = i+1
# else : 
#     print("not found")  
    # if(i==len(tuple)):
    #     print("not found")
   
# prime or not prime
# n = int(input("enter a number: "))  
# i = 2
# while(i<=(n/2)):
#     if(n%i==0):
#         print(n,"is not a prime number")
#         break
#     i = i+1
# else :  
#     print(n,"is a prime number")    


# n = int(input("enter a number : "))
# i = 2
# while (i<=n/2):
#     if(n%i==0):
#         print(n,"is not a prime number")
#         break
#     i+=1
# else:
#     print(n,"is a prime number")

# list = [1,4,9,16,25,36,49,64,81,100]
# x = 81 
# index = 0
# ok_2 = 0
# for i in list :   
#     if(x==i) :
#         print (x,"found at index",index,ok_2)
#     index +=1
#     ok_2 += 2
# tuple = (1,4,9,16,25,36,49,64,81,100,16)
# x = int (input("enter a number to search: "))
# i = 0
# for i in range(len(tuple)) :
#     if(x==tuple[i]):
#         print(x,"found at index",i)
#         # break
#     i =i+1
# # else : 
# #     print("not found")  

# n = int(input(("enter a number : ")))
# for i in range(1,11) :
#     print (n,"X",i,"=",n*i)

# n = int(input ("Enter a number: "))
# sum = 0
# i = 0
# while i<=n :
#     sum = sum+i
#     i += 1
# print(sum)

# sum = 0
# for i in range(n+1) :
#     sum = sum + i
# print(sum)

# fact = 1
# for i in range(1,n+1) :
#     fact = fact * i   
# print(fact)

# i = 1
# while i<=n : 
#     fact *=  i
#     i += 1  
# print(fact)


# def sum (a,b) :
#     sum = a+b
#     return sum

# a = sum(10,20) 
# print(a)
# b = sum(100,200)
# print (b)

# def avg(a,b,c) :
#     avg = (a+b+c)/3
#     return avg

# print (avg(10,20,30))

# print("hello",end="_" )
# print("world")
# len()
# range()

# def practice(a,b="python"): 
#     print(a)
#     print("world")
# practice('hello')



# def fun (list) :
#     print(len(list))
#     print(type(list))
#     for i in list :
#         print(i,end=" ")

# list = [1,2,3,4,5,6,7]

# fun(list)

# def fun(experment):
#     type = type(experment)
#     print(type)

# # list = [1,2,3,4,5,6,7]
# # tuple = (1,2,3,4,5,6,7) 
# # set = {1,2,3,4,5,6,7}
# # fun(list)
# # fun(tuple)  
# # fun(set)
 



# def fact (n) :
#     f = 1
#     i = 1
#     while (i<=n) :
#         f = f*i
#         i += 1
#     print(f)


# n = int(input("enter a number: "))  
# fact(n)

# def function(n) : 
#     rs = 83*n
#     print (n,"usd =",rs,"INR")

# n = int(input("enter usd : "))
# function(n)


# def function(n) :
#     if (n%2==0) :
#         print (n,"is eeven")
#     else : 
#         print(n,"is odd")

# n = int(input("enter a number: "))
# function(n)
  

# def fun (n) : 
#     if (n==0) :
#         return
#     print(n)
#     fun(n-1)
    
# def fun (n) :
#     if (n==0 | n==0) : 
#         return 1
    
#     fact = n *fun (n-1)
#     return(fact)
# print(fun(5))


def fun2(n) :
    if (n==0 ):
        return 0
    sum = n + fun2(n-1)
    return sum
    
s = fun2(5)
print(s)
         


def fun(list,index=0) :
    if (index==len(list)) :
        return
    print(list[index],end=" ")
    fun(list,index+1)

    


list = [1,2,3,4,5,6,7]
fun(list)

























