pok, vok = 2.3, 7.41
vok = 7.41
p = input("Enter pressure :")
p = float(p)
v = input("Enter volume :")
v = float(v)

if p > pok and v > vok:
    print("STOP")
elif p > pok:
    print("Increase volume")
elif v > vok:
    print("Increase pressure")
else:
    print("Evething is OK")