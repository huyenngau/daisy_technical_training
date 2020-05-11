1. Using the Trie data structure

The solution has three classes defined - RouteTrie, RouteTrieNode and Router. 

RouteTrieNode initializes the Route handler, inserts. 
It has a handler and reference to the children node. 
There are no loops. 
Hence, the time complexity for this class is O(1) and 
space complexity is also O(1) since it inserts a single element. 

RouteTrie initializes the root node, inserts node and finds node. 
Insert method adds recursively. 
Find method navigates the Trie and returns a handler if a match is found. 
There is looping in this class. 
Hence, time complexity is O(n) where n is the number of paths the method loops through. 
Space complexity is O(n)

Router initializes the root handler, adds handler, has a lookup method to find the handler. 
Time complexity is O(n) and space complexity is also O(n).

split_path splits the path into parts for both add handler and lookup functions. 
Hence, time complexity is O(n) where n is the string length.
Space complexity is O(1).

2.
Time Complexity for RouteTrieNode is O(1) and Space Complexity is O(1)
Time Complexity for RouteTrie is O(n) and Space Complexity is O(n).
Time Complexity for Router is O(n) and Space Complexity is O(n).

Hence, overall Time Complexity is O(n) and Space Complexity is O(n).
