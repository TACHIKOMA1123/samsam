
total=101-1
for i in range(1,101,2):
    print(i)
print(i%7)
print(i%5,i%15)
print("程式執行完畢")

for a in range(9, 0, -1):
    for b in range(9, 0, -1):
        if a == 1 :
            continue 
        print(a, "*", b, "=", a * b, sep="", end="\t")
    print()