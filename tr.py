import time
# s=0
# ns=6
#
# for i in range(10**(ns-1),10**ns):
#     sss=str(i)
#     if sss==sss[::-1]:
#         s+=1
#         print(sss)
# print('->',s)
#
# s1=0
# for n in range(ns,ns+1):
#     if n%2==0:
#         s1+=10**((n)//2)-10**(n//2-1)
#     else:
#         s1+=10**((n+1)//2)-10**((n+1)//2-1)
#
#1026376
# print(s1)


# s=0
# timer = time.perf_counter()
# for i in range(10**6,1026376):
#     sss=str(i)
#     if sss==sss[::-1]:
#         s+=1
#         print(sss)
# print('->',s)
timer2 = time.perf_counter()
# for n in range(8,15+1):
#     if n%2==0:
#         s+=10**(n//2)-10**(n//2-1)
#     else:
#         s+=10**((n+1)//2)-10**((n+1)//2-1)
#     print(s)
#
# print(s)
# print(time.perf_counter())


print((9000-(10+10+7))+sum([9*10**((n-1)//2) for n in range(8,15+1)]))