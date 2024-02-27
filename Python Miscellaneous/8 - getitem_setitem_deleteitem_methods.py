import operator

del_value = None
set_value = None

l = [4,39,45,23,5,100]

for i in range(0, len(l)):
    if i == 3:
        set_value = operator.setitem(l, i, "new_value") # Returns Nothing
    if l[i] == 100:
        del_value = operator.delitem(l, i) # Returns Nothing

print(a := operator.getitem(l, 3))
print(f"deleted value = {del_value}")
print(f"set value = {set_value}")
print(l)