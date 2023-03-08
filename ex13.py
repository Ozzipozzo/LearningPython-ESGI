# n = 30
# i = 0
# count = 0

# while count < n:
#     if i % 2 == 0:
#         print(i)
#         count += 1
#     i += 1

n = 20 
count = 0
for i in range(0, n, 2):
    if i % 2 == 0:
        print(i)
        count += 1
    else:
        break