line = ""
for i in range(2,10) :
    line += ('# ' + str(i) + '단 # ')
print(line)
for i in range(1,10):
    line = ""
    for k in range(2,10):
        line += (" %dX %d= %d" % (k, i, k*i))
    print(line)