def bubbleSort (array):
    n = len(array)


    for i in range(n):


        for j in range(0, n-i-1):


            if array[j] > array[j+1]:
                array[j], array[j+1] = array[j+1], array[j]





if __name__ == "__main__":
    array = [5, 1, 4, 2, 8]

    bubbleSort (array)

    print("Sorted array is:")
    for i in range(len(array)):
        print("%d" % array[i], end=" ")