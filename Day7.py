# def greet():
#     print('hi')
#     return('yrs')
# var=greet()
# print(var)

#----------------------Q1 factorial----------------------

# def fac(n):
#     fact=1
#     for i in range(1,n+1):
#         fact=fact*i
#     return fact
# a=int(input())
# print(fac(a))


#---------------Q2 table------------------------------------
#
# def t(n):
#     for i in range(1,11):
#         print(n*i)
# a=int(input())
# t(a)


#----------------Q3 print list-------------------------------

# def z():
#
#     return [1,2,3]
# print(z())


#-------------Q4 check string is upper or not---------------------------------

# def a(n):
#     if n.isupper():
#         return True
#     return False
# n=input()
# print(a(n))

#---------------@5

# def sk(n):
#     a=0
#     for i in n:
#         c=ord(i)
#         print(c)
#         a+=c
#     return a
# n=input()
# print(sk(n))
# ---------------------------
# def sk(n):
#     return sum(map(ord,n))
# n=input()
# print(sk(n))

# =============== Q6 slicing=========================================================


# def a(q,w):
#     a=q[0:4]+w[-4:]
#     return a
# q=input()
# w=input()
# print(a(q,w))

#====================Q7 check is in alphabetic order or not=======================================

# def a(w):
#     n=len(w)
#     sum_=0
#     for i in range(n-1):
#         if (ord(w[i])+1==ord(w[i+1])):
#             sum_+=1
#     return sum_
# w = input()
# print(a(w))


#=======================@8
def a(lst):
    for i in lst:
        if i%2==0 :
            print(i)
lst=[53245,12344125,432,25,234,523,46,234,62,234,6234]
print(a(lst))
