N, X, Y, Z = map(int, input().split())

joken = False
if X < Y:
    if X < Z and Z < Y:
        joken = True
else:
    if Y < Z and Z < X:
        joken = True
        
print('Yes' if joken else 'No')
