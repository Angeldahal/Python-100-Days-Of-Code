with open("file1.txt") as f1:
    file1_data = f1.readlines()

with open("file2.txt") as f2:
    file2_data = f2.readlines()

result = [int(num) for num in file1_data if num in file2_data]
print(result)
 