for i in range(4,16,4): #4, 8, 12
    for j in range(i,0,-2): # 12, 10, 8, 6, 4, 2 
        a = i - j
        print(a, end="")
    print()
print("Bye!") 