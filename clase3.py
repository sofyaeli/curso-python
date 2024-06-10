
     

# l= ["a", "b", "c"]

# for i in l:
#     print(i)


l=[]
for i in range(10):
    if i%2!=0:
        l.append(i**2)

print(l)


l2= [i**2 for i in range (10) if i%2!=0]

print(l2)

dict={i:i**2 for i in range(10) if i%2!=0}

print(dict)
print(dict[5])
 
        