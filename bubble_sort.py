import matplotlib.pyplot as plt
import random
def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        for j in range(0,n-i-1):
            if arr[j] > arr[j+1]:
                arr[j] , arr[j+1] = arr[j+1] , arr[j]
            plt.clf()
            plt.bar(range(len(arr)),arr)
            plt.pause(0.01)

array = [random.randint(1,100) for i in range(10)]
plt.ion()
bubble_sort(array)
plt.ioff()
plt.show()
