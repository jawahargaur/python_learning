#
# a = input('Enter the string: ')
#
# if len(a) >= 16:
#     for i in a:
#         if i in range(ord(a)):
#             lower = True
#         elif i.isupper():
#             upper = True
#         elif i.isdigit():
#             digit = True
#
# if length and lower and upper and digit:
#     print('That is a valid string.')
# else:
#     print('That string is not valid.')


# a=str.lower(input())
# dct = {}
# for i in a:
#                            # if i.isupper():
#                            #     i=i.lower()
#                            #     dct[i]=1
#     if i in dct:
#         dct[i]+=1
#     else:
#         dct[i]=1
# print(dct)




# lst=[]
# while(True):
#     s=input()
#     a,b = s.split()
#     if a=='stop':
#         break
#     elif a=='push':
#         lst.append(b)
# print(lst)
#
# dct={}
# while (True):
#     a=input()
#     a=a.split()
#     if a[0]=="stop":
#         break
#     elif a[i] in dct:
#             dct[a[0]].add(a[1])
#     else:
#         dct[a[0]]={a[1]}
#
#
# print(dct)



#----------code---------------
#1

# for i in n:
# if i in map_:
#         map_[i]+=1
#     else:
#         map_[i] =1
# print(map_)
#
#
# n = n.lower()
# map_ = {}
# for i in n:
#     if i in map_:
#         map_[i] += 1
#     else:
#         map_[i] = 1
# print(map_)

#2


# lst = []
# while True:
#     p = input()
#     p = p.split()
#     if p[0] == 'stop':
#         break
#     elif p[0] == 'push':
#         lst.append(p[1])
#     elif p[0] == 'pop':
#         index_of_value = lst.index(p[1])
#         lst.pop(index_of_value)
#     else:
#         print('invalid')
# print(lst)


#3


map_={}
while True:
    stud = input()
    stud = stud.split()
    if stud[0] == 'stop':
        break
    else:
        if stud[0] in map_:
            map_[stud[0]].add(stud[1])
        else:
            map_[stud[0]]={stud[1]}
            # map_[stud[0]].add(stud[1])
print(map_)









