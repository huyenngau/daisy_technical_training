1. Why did you use that data structure?
- I have used recursion to solve this problem. 
- Reason same as file recursion

For this problem: 
- First, I use get_users to get list of items from group
- Second, if user is in list of items, return True
- Third, if not, I use get_groups to get all child groups in the original group
- Using a for loop to go through child groups to find user in child group
- If user is in child group, return True
- If not, back to the third step 
- Finally, if can not find user in group, return False 

2. The efficiency (time and space) of your solution:
Time complexity is O(n) and space complexity is O(n).
