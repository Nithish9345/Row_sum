class RowSum:
    def sum(self, array):
        x = len(array)
        for i in range(x):
            sum = 0
            for j in range(len(column)):
                sum += array[i][j]

            print(sum, end =" ")

        return ""

row = int(input("Enter no of rows"))

array = []
for i in range(row):
    column = list(map(int, input().split()))
    array.append(column)

object = RowSum()
print(object.sum(array))



