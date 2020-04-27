1. Why did you use that data structure?
Linked list for both of union and intersection 

For the input of this problem, need to add a remove_duplicates method to remove all items is duplicated in linked list 
and search method as the helpers 

- Union (list1, list2):
Initialize result list as NULL. Traverse list1 and add all of its elements to the result.
Traverse list2. If an element of list2 is already present in list1 then do not insert it to result, 
otherwise insert.

- Intersection (list1, list2)
Initialize result list as NULL. 
Traverse list1 and look for its each element in list2, if the element is present in list2, 
then add the element to result.

2. The efficiency (time and space) of your solution:
- search: O(n)
- append: O(n)
- remove_duplicates: O(n^2) because a while loop contain checking in a list 
- union: O(n^2)
- intersection: O(n^2)
