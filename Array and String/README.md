# Arrays and Strings

Welcome to the **Arrays and Strings** module of the DSA with Python project! This directory contains various algorithms related to arrays and strings, which are fundamental data structures in programming.


### `1.min_and_max_in_array.py`

This script implements methods to find the minimum and maximum elements in an array. Each method showcases a different approach, providing insight into various algorithmic strategies.

#### Problem Statement

Given an array, determine the minimum and maximum values contained within it.

#### Methods Implemented

1. **Method 1: Convert Array to List and Sort**
   - **Description:** This method converts the NumPy array to a Python list and sorts it to find the minimum and maximum values.
   - **Complexity:** O(n log n) due to sorting.

2. **Method 2: Sorting Using Nested Loops**
    **Description:** This method sorts the array using a bubble sort approach and retrieves the first and last elements as the minimum and maximum.
    **Complexity:** O(n²) due to nested loops.

3. **Method 3: Direct Min and Max Retrieval**
    **Description:** This method uses Python's built-in min() and max() functions to find the minimum and maximum values directly.
    **Complexity:** O(n) as it traverses the array once.

4. **Method 4: Using Built-in Sort Function**

    **Description:** This method sorts the array in place using the built-in sort function and retrieves the minimum and maximum values.
    **Complexity:** O(n log n) due to sorting.