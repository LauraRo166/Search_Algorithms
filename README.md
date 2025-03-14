# Search Algorithms

The following search algorithms are implemented: 
 + Linear
 + Binary
 + Ternary

## Complexities Analysis
### Linear
+ Best Case (O(1)): If the element is the first in the list, the search stops immediately.
+ Worst Case (O(N)): If the element is at the end or not present, all elements must be checked.
+ Average Case (O(N/2)): On average, about half of the elements are checked before finding the element.

### Binary
+ Best Case (O(1)): If the element is at the middle, it is found instantly.
+ Worst Case (O(log N)): Since the search space is halved at each step, the maximum number of iterations is log2(N).
+ Average Case (O(log N)): The number of steps required on average is still logarithmic.

### Ternary
+ Best Case (O(1)): If the element is found at one of the division points, it is found instantly.
+ Worst Case (O(log3 N)): The search space is reduced by a factor of 3 at each step, meaning the number of iterations is log3(N).
+ Average Case (O(log3 N)): The number of comparisons needed is approximately log3(N).

## Unit and coverage testing

![image](https://github.com/user-attachments/assets/37809c32-9b87-4d27-befe-4f8633224044)

## Test and visualization
Binary and Ternary search:
![image](https://github.com/user-attachments/assets/4acdf5b3-8a00-43a6-855f-ac11da6b9377)
![image](https://github.com/user-attachments/assets/fa480d26-d6d1-4d04-93de-bc173325932a)



