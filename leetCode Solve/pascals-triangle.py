
numRows = int(input("Enter number"))
list1 = []
for i in range(numRows):
    temp_list = []
    for j in range(i + 1):
        if j == 0 or j == i:
            temp_list.append(i)
        else:
            temp_list.append(list1[i - 1][j - 1] + list1[i - 1][j])
    list1.append(temp_list)
for i in range(numRows):
    for j in range(numRows - i - 1):
        print(end=" ")
    for j in range(i + 1):
        print(list1[i][j],end=" ")

# print(.............................................)
class Solution:
    def generate(self, numRows: int) -> List[List[int]]:

        list1 = [[1]]
        for i in range(numRows-1):
            temp = [0]+ list1[-1]+[0]
            row = []
            for j in range(len(list1[-1])+1):
                row.append(temp[j]+temp[j+1])
            list1.append(row)
        return list1
