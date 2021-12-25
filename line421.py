na=0
while True:
    s=input()
    if not s:
        break
    v=s.split(" ")
    operation=v[0]
    am=int(v[1])
    if operation=="d":
        na+=am
    elif operation=="w":
        na-=am

print(na)            