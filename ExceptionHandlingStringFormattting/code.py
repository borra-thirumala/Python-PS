#l=[12,13]
#print(l[2])

#if True:
#print("Hii")  #indentation error

#print(10/0)  #zero division error

# Exception Handling methods in Python:
# try
# except
# else
# finally

# try:
#     print(10/0)
# except:
#     print("not possible") #op:not possible

# try:
#     l=[1,2,3]
#     print(l[4])
# except:
#     print("code not executed")  #op:code not executed

# try:
#     l=[1,2,3]
#     print(l[2])               op:3
#     print("try")               try
# except:
#     print("code not executed")  
#     print("except")              

# try:
#     l=[1,2,3]
#     print(l[4])
#     print(l[2])
#     print("try")
# except:
#     print("code not executed")  #op:code not executed
#     print("except")             #except

#Exception
# try:
#     l=[1,2,3]
#     print(l[4])
# except Exception as e:    we're getting exception using alias name
#     print("code not executed")     code not executed
#     print("except",e)               except list index out of range


# try:
#     l=[1,2,3]
#     print(l[4])
#     print("try")
# except IndexError as err:  #except Exception as error
#     print("code not executed")
#     print(err)
# finally:
#     print("always executed")

# try:
#     str="123456"
#     vowels="aeiouAEIOU"
#     count=0
#     for i in str:
#         if i in vowels:
#             count+=1
#     if count==0:
#         raise Exception("no vowels found") #custom exception "raise"
#     else:
#         print(count)

# except Exception as e:
#     print("error occured",e)

# try:
#     age=int(input("enter the age: "))
#     if age<0:
#         raise Exception ("invalid age given")
#     else:
#         print(age)
# except Exception as e:
#     print(e)


# try:
#     name="thirumala"
#     mob=1234567890
#     sum=name+mob
# except Exception as e:
#     print(e)        #can only concatenate str (not "int") to str


# try:
#     name="thirumala"
#     mob="1234567890"
#     sum=name+mob
#     print(sum)     #thirumala1234567890
# except Exception as e:
#     print(e) 


# try:
#     age=int(input("enter the age: "))
#     if age<0:
#         raise Exception("invalid age")
# except Exception as error:
#     print({"error:error"})
# else:
#     print(age)
# print("hello")


# enter the age: 20
# 20
# hello


# enter the age: -5
# {'error:error'}
# hello




#String formatting

# def show_name(n):
#     #print("hi my name is ",n)
#     print(f"hi my name is {n}",) #string formatting
# show_name("thirumala")
# show_name("python")



# def add(a,b):     #string formatting:before string we should declare f
#     print(f"the sum is {a+b}")
# add(3,4)

# print(f"{20+30}")
# print(f"{"hi"+"20"}")

# age=int(input("enter the age: "))
# print(f"the age is: {age}")


# try:
#     print(10/0)
# except Exception as error:
#     print({"error":error})  op:will come in dict {'error': ZeroDivisionError('division by zero')}
# print("hello")              hello