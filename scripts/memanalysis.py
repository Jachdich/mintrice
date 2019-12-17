x = "asd"
while x != "":
    try:
        x = [i for i in input().split(" ") if i != ""]
        if "RSS" in x: continue
        print(x[0] + " " * (20 - len(x[0])) + x[1] + "        " + str(round(int(x[2]) / 1024, 2)) + "M")
    except EOFError:
        x = ""
