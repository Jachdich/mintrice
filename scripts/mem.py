ln1 = input()
ln2 = input()
ln3 = input()
x = [int(i) for i in ln2.split(" ")[1:] if i != ""]
total = x[0]
used  = x[1]
free = x[2]
avail = x[5]

if used < 1024:
    useds = str(used) + "M"
else:
    useds = str(round(used / 1024, 2)) + "G"

totals = str(round(total / 1024, 1)) + "G"

print(useds + "/" + totals + " ({}%)".format(str(round(used / total * 100, 0))))
