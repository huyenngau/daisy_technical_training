I set up a double linked list with: 
- the most-recently used item at the head of the list
- and the least-recently used item at the tail

In general, in a double linked list:
- deleting/removing an item is O(1) time, 
- inserting an item is O(1) time
- finding/getting an item is O(n) time, since need to walk the whole list, 

So I use a hash map that maps items to linked list nodes.
That lets me find an element in my cache's linked list in O(1) time, instead of O(n).

* Look up the item in hash map.
- If the item is in the hash table, then it’s already in the cache, this is called a “cache hit”
  + Use the hash table to quickly find the corresponding linked list node
- If the item isn’t in the hash table, this is a "cache miss", need to add the item into the cache:
  + if cache is full, need to remove something to make room:
  -> Get the least-recently used cache item — it’ll be at the tail of the linked list.
  -> Evict that item from the cache by removing it from the linked list and the hash map.
  -> Create a new linked list node for the item. Insert it at the head of the linked list.
  -> Add the item to hash map, storing the newly-created linked list node as the value.
  All of those steps are O(1)
  

