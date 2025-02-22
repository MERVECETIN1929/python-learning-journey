# Enter your code here. Read input from STDIN. Print output to STDOUT
input_count = int(input())
input_list = list()
for i in range(input_count):
    input_list.append(input())
for i in range(len(input_list)):
    print(input_list[i][0::2], input_list[i][1::2])
