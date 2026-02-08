# Dictionary Methods
a={"Name":"Yash"}
b={"Age":"22"}
print(a.keys())
print(a.values())
print(a.items())
print(a.update(b))

# String Methods
s="Welcome to my world"
p="WELCOME TO MY WORLD"
print(s)
print(s.upper())
print(p.lower())
print(s.strip())
print(s.replace("world","duniya"))
print(len(s))
print("duniya" in s)
print("world" in s)

# List Methods
l=["Yash",22,"Btech",77]
m=[12,45,89,47,34]
l.append(45)
print(l)
l.insert(1,"Rana")
print(l)
l.remove(77)
print(l)
l.pop(3)
print(l)
m.sort()
print(m)

#Tuple Methods
t=(12,45,78,34,23,45,89)
print(t.count(45))
print(t.index(89))
print(len(t))

# Set Methods
s={12,45,78,34,23,45,89}
s.add(90)
print(s)

s.remove(34)
print(s)

s.pop()
print(s)

s.clear()
print(s)

s1={100,200,300}
s2={200,300,400}
print(s1.union(s2))
print(s1.intersection(s2))
print(s1.difference(s2))
print(s1.issubset(s2))
print(s1.issuperset(s2))
print(s1.isdisjoint(s2))
print(s1.symmetric_difference(s2))
print(s1.copy())

s3={1,2,3}
s4={3,4,5}

s3.update(s4)
print(s3)

s3.intersection_update(s4)
print(s3)

s3.difference_update(s4)
print(s3)

s3.symmetric_difference_update(s4)
print(s3)
