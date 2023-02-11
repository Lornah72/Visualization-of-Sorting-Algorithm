import matplotlib.pyplot as plt
import numpy as np
import random

def merge(nums):
    if len(nums) > 1:
        mid = (len(nums)) //2
        left = nums[:mid]
        right = nums[mid:]
        merge(left)
        merge(right)
        i = j =k =0
        while i < len(left) and j < len(right):
            if left[i] <= right[j]:
                nums[k] = left[i]
                i+=1
            else:
                nums[k] = right[j]
                j+=1
            k+=1
        
        while i < len(left):
            nums[k] = left[i]
            i+=1
            k+=1
        while j < len(right):
            nums[k] = right[j]
            j+=1
            k+=1
    return nums

def visualizer_sort(nums):
    fig, ax = plt.subplots()
    ax.bar(np.arange(len(nums)),nums)
    plt.pause(0.001)
    plt.clf()


nums = [random.randint(1,100)for i in range(20)]
sorted = merge(nums)    
visualizer_sort(sorted)
plt.show()