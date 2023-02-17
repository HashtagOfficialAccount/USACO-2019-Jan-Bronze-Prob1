x = open("shell.in","r")
n = int(x.readline())
start = [1,2,3]
start_1 = 0
start_2 = 0
start_3 = 0
for i in range(n):
    line = x.readline()
    line = [int(i) for i in line.strip().split()]
    switch_1 = line[0]
    switch_2 = line[1]
    index = 0
    for e in start:
        if e == switch_1:
            start[index] = switch_2
        elif e == switch_2:
            start[index] = switch_1
        index += 1
    pos = start.index(line[2])
    if pos == 0:
       start_1 += 1
    elif pos == 1:
        start_2 += 1
    else:
        start_3 += 1

l = [start_1,start_2,start_3]
x.close()      
x = open("shell.out","w")
x.write(str(max(l)))
x.close()
