import matplotlib.pyplot as plt
import random
def partition(arr,low,high):
    pivot = arr[high]
    i = low-1
    for j in range(low,high):
        if arr[j] <= pivot:
            i = i+1
            (arr[i],arr[j]) = (arr[j],arr[i])
    (arr[i+1],arr[high]) = (arr[high],arr[i+1])
    return i+1

def quicksort(arr,low=0,high=None):
    if high is None:
        high = len(arr) - 1
    if low < high:
        p1 = partition(arr,low,high)
        quicksort(arr,low,p1-1)
        quicksort(arr,p1+1,high)
        
    plt.clf()
    plt.bar(range(len(arr)), arr)
    plt.pause(0.001
    )


array = [random.randint(1, 100) for i in range(20)]
plt.ion()
quicksort(array)
plt.ioff()
plt.show()
