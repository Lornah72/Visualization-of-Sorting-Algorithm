# Visualization-of-Sorting-Algorithm
Explore the magic of sorting algorithms with this visually stunning Github repository! Get a chance to see different sorting algorithms in action, as they sort through an array of numbers in real-time. With a user-friendly interface, you can interact with each algorithm, adjusting the speed and size of the data set to your preference. 
# What is a sorting algorithm?

A sorting algorithm is a method used to arrange data elements in a specific order, such as ascending or descending. It is a fundamental concept in computer science, and is used in many different applications, such as data processing, database management, and more. Sorting algorithms come in a variety of types, including bubble sort, insertion sort, selection sort, merge sort, quick sort, and more. Each algorithm has its own strengths and weaknesses, and the choice of which one to use depends on the specific needs of the task at hand. Overall, sorting algorithms are an important tool for organizing data and making it easier to work with.

# Brief description of some sorting algorithms
## 1. Quick sort

QuickSort is a divide-and-conquer algorithm that works by selecting a "pivot" element from the array and partitioning the other elements into two sub-arrays, according to whether they are less than or greater than the pivot. The sub-arrays are then sorted recursively. This process continues until all elements are sorted.
QuickSort is one of the most widely used sorting algorithms and is known for its efficiency, with a best-case time complexity of O(n log n) and an average-case time complexity of O(n log n). This makes it well-suited for large data sets. In addition, QuickSort is also highly adaptive, meaning that it works well even when the data is already partially sorted or when there are duplicate values in the array.
QuickSort has a few disadvantages, such as its poor performance in the worst case and its high memory requirements, as it uses an O(log n) amount of extra memory due to the recursion. However, these issues can often be addressed through various optimizations and modifications to the basic algorithm.
### VISUALIZATION
https://user-images.githubusercontent.com/68066226/218258578-41e2d605-43eb-430b-8f30-1cb89ef2da6a.mov


## 2. Bubble sort

Bubble Sort is a sorting algorithm that repeatedly steps through the list, compares adjacent elements and swaps them if they are in the wrong order.The process is repeated until the list is sorted in the desired order.
Bubble sort has a worst-case and average-case time complexity of O(n^2), where n is the number of items being sorted. This makes it inefficient for large data sets and it is generally not used in practice for that reason. However, it is still a good algorithm for small data sets and for educational purposes, as it is easy to understand and implement.

## 3. Merge sort
Merge Sort is a sorting algorithm that uses a divide-and-conquer approach to sort an array. It divides the unsorted list into n sub-lists, each containing one element, and then repeatedly merges sub-lists to produce new, sorted sub-lists until there is only one sub-list remaining.
The key advantage of Merge Sort is its guaranteed O(n log n) time complexity, making it an efficient sorting algorithm for large data sets. It is also a stable sorting algorithm, meaning that the relative order of equal elements is preserved in the sorted output.
Merge Sort is often implemented using a recursive approach, but can also be implemented iteratively. Its primary disadvantage is its high memory requirement, as it requires additional memory proportional to the size of the input data to perform the merging of sub-lists. Despite this, Merge Sort is widely used due to its guaranteed performance and ease of implementation.


## Installation

If you already have python and pip installed, run the following command [pip](https://pip.pypa.io/en/stable/) to install matplotlib.

```bash
pip install matplotlib
```


## License

@LornahSanga
