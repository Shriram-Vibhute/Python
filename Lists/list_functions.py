l = [int(input("Enter the number: ")) for i in range(0, 5)]
m = [i for i in range(0, 5)]

l.append(10) # updates the original array
print(l)

l.sort()
l.sort(reverse=True) # sort in dereasing order

print(l.index(40)) # error -> index out of bound

print(l.count(2)) # Count all the occurances of 2

# Referance binding
k = l
k[0] = "Dexter"
print(l) # -> Both arrays get updated here

k = l.copy()
print(k)

k = l + m
print(k)

l.extend(m)
print(l)