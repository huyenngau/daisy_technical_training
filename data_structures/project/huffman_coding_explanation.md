1. Why did you use that data structure?
Follow the pseudocode in this problem,
- I have build a class named HeapNode with attributes: char, frequency, left pointer, right pointer
It will be used to save info of nodes in huffman tree 
In HeapNode class, I have create a __lt__ method to compare 2 nodes based on their frequency

- Before build a huffman tree, I need to push all nodes onto a heap queue 
To do this, I used a built-in python is heapq. 
This module provides an implementation of the heap queue algorithm, also known as the priority queue algorithm
There are 2 functions is used in my solution are: 
+ heapq.heappush(heap, item)
Push the value item onto the heap, maintaining the heap invariant.

+ heapq.heappop(heap)
Pop and return the smallest item from the heap, maintaining the heap invariant. 

This algorithm will take the second step in the pseudocode is: 
"Build and sort a list of tuples from lowest to highest frequencies."

- Build a huffman tree: 
Get 2 minimum nodes from Heap by using heappop function 
Create a new internal node with a frequencies equal to the sum of the two nodes frequencies
Make the first extracted node as its left child and the other extracted node as its right child
Add new node to the min heap by using heappush function 

Do these steps above until heap has 1 node only 
Using heappop to get this node, it is a tree
Remove the frequencies from this tree to clean space unnecessary
Finally, return a huffman tree

- Encoded data: 
For the huffman tree, if go to the left node, assign binary code = 0 
if go to the right node, assign binary code = 1

First, init an empty dictionary
Then, using a in-order traversal to traverse until find a leaf, 
get char and binary code in that leaf to save in dictionary 

Using a for loop to go through characters in input string, encoded data will plus binary code for each character
End fo the loop, return encoded data

- Decoded data: 
With encoded data and huffman tree, 
- Start from root and do following until a leaf is found
- Using a loop to go through encoded data 
If current bit is 0, move to left node of the tree
If the bit is 1, move to right node of the tree
- If during traversal, encounter a leaf node, print character of that particular leaf node
- Then again continue the iteration of the encoded data starting from step 1 
- Finally return decoded data, it should be the input string 

2. The efficiency (time and space) of your solution:
- build_a_huffman_tree: 
Make char_frequency dict: O(n) 
Add items in frequencies into Heap: O(n^2), because loop in frequencies dict - O(n) and heappush - O(n)
heappop: O(n * log n)
trim_huffman_tree: O(n)
- make_binary_code: O(n)
- get_encoded_data: O(n)
- get_decoded_data: O(n)


