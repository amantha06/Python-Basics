for x = 0 to 4
    for y = 0 to 4
        A(x,y) = (x+1) ^ 2 + y
    next y
next x
for x = 0 to 4
    for y = 0 to 4
        if A(x,y) % 3 == 0 then
            A(x,y) = A(x,y) / 3
        if A(x,y) % 4 == 0 then
            A(x,y) = A(x,y) / 4
        if A(x,y) % 5 == 0 then
            A(x,y) = A(x,y) / 5
    next y
next x
s = 0
for x = 0 to 4
    for y = 0 to 4
        if A(x,y) % 2 == 0 then
            s = s + A(x,y)
     next y
next x
print(s)
