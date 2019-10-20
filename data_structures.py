#list
#mutable

saarc= ["ban", "ind", "nep", "afg"]
print (saarc)

saarc.append("pak")
print (saarc)

saarc.sort()
print (saarc)

saarc.reverse()
print (saarc)

saarc.remove("pak")
print (saarc)

li=[1,2,3,4]
li2=[3,4,5,6]

li.extend(li2)
print(li)

#list_comprehension

lim=[1,2,3,4]
new_lim=[]
for x in lim:
    new_lim.append(2*x)

print(new_lim)

#tuple
#not_mutable

tpl=(1,2,3)
print(tpl)

n1,n2,n3=tpl
print(n1, n2, n3)

#set

A={1,2,2,3}
B={2,3,4,5}
print(A&B)

#dictionary

marks={1:77, 2:88, 9:22}
print(marks[9])