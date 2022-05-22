# Given two library versions of an executable: for example,
#  “10.1.1.3” and “10.1.1.9” or “10” and “10.1”. 
# Find out which one is more recent? Strings can be empty also.


s1 = input()
s2 = input()

t1 = [int(i) for i in s1.split(".")]
t2 = [int(i) for i in s2.split(".")]
while len(t1)<len(t2):
    t1.append(0)
while len(t2)<len(t1):
    t2.append(0)
    
# print(t1,t2)
flag  = False
for i in range(len(t1)):
    if t1[i]>t2[i]:
        flag = True
        break
if flag:
    print(s1)
else:
    print(s2)