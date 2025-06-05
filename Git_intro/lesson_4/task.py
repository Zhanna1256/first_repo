
# for i in range(1, 6):
#     for j in range(1, i+1):
#         print(j, end="")
#     print()


# brick = "*"
# size = 5
# for i in range(size, 0, -1):
#     for j in range(i):
#         print(brick, end="")
#     print("")


for row in range(5):
    for col in range(7):
        if row==0 or row==4 or col==0 or col==6:
            print("#", end="")
        else:
            print(" ", end="")
    print()
        