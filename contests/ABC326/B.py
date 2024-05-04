n = int(input())
while True:
    s = str(n)
    if int(s[0])*int(s[1]) == int(s[2]):
        print(n)
        exit()
    else:
        n += 1
        