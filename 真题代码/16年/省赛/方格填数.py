# import itertools as it
# a=[i for i in range(10)]
# m = it.permutations(a,10)
# num = 0
# for a in m:
#     list(a)
#     if a[0]+1!=a[1] and a[0]+1!=a[3] and a[0]+1!=a[4] and a[0]+1!=a[5]:
#         if a[1]+1!=a[0] and a[1]+1!=a[2] and a[1]+1!=a[4] and a[1]+1!=a[5] and a[1]+1!=a[6]:
#             if a[2]+1!=a[1] and a[2]+1!=a[5] and a[2]+1!=a[6]:
#                 if a[3]+1!=a[0] and a[3]+1!=a[4] and a[3]+1!=a[7] and a[3]+1!=a[8]:
#                     if a[4]+1!=a[0] and a[4]+1!=a[1] and a[4]+1!=a[3] and a[4]+1!=a[5] and a[4]+1!=a[7] and a[4]+1!=a[8] and a[4]+1!=a[9]:
#                         if a[5]+1!=a[0] and a[5]+1!=a[1] and a[5]+1!=a[2] and a[5]+1!=a[4] and a[5]+1!=a[6] and a[5]+1!=a[8] and a[5]+1!=a[9]:
#                             if a[6]+1!=a[1] and a[6]+1!=a[2] and a[6]+1!=a[5] and a[6]+1!=a[9]:
#                                 if a[7]+1!=a[3] and a[7]+1!=a[4] and a[7]+1!=a[8]:
#                                     if a[8]+1!=a[3] and a[8]+1!=a[4] and a[8]+1!=a[5] and a[8]+1!=a[7] and a[8]+1!=a[9]:
#                                         if a[9]+1!=a[4] and a[9]+1!=a[5] and a[9]+1!=a[6] and a[9]+1!=a[8]:
#                                             num+=1
# print(num)
print(1580)