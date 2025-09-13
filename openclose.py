# f = open("demo.txt","a+")
# print (f.read())
# f.close()

# f= open("demo.txt","r")
# data = f.readline()

# print(data)
# print(type(data))
# f.close()


# print(f.read() )
# f.write("abc")
# f.close()


# with open("demo.txt","r") as f :
#     data = f.read()
#     print(data)

# with open("demo.txt","w") as f :
#     data = f.write("new data_1")
#     print(data)


# import os

# os.remove("importent.txt")

# with open ("demo.txt","w+") as f :
#     f.write("")

# with open ("ques.txt","w") as f :
#     f.write("Hi everyone\nwe are learning\n")
#     f.write("using java\nI like programming in java")

with open("ques.txt","r") as f :
    str  = f.read()
    pk = str.replace("java","python")
    print(pk)
with open("ques.txt","w+") as f :
    f.write(pk)


# def function(word) :
#     with open("ques.txt","r") as f :
#         str = f.read()

#         if word in str :
#             print("found")
#         else :
#             print("not found")
        
# function("learning")







