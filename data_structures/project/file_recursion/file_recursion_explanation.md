1. Why did you use that data structure?
- I have used recursion to solve this problem. 
- Because I saw this problem is inherently recursive. 
For such a problem, it is preferred to write recursive code. 

For this problem, I am using two lists to hold information
- One is to hold directories to walk through
- Second is to hold a list of paths contain files end with ".c" 
- First, getting all files from a path 
- After that, using a for loop to create new_path: 
If new_path is a directory, back to the first step 
If new_path end with ".c", append new_path into all_paths 
- Finally, return all_paths is a list of paths that contain files end with ".c" 

2. The efficiency (time and space) of your solution: 
Time complexity is O(n) and space complexity is O(n).