class Solution(object):
    def hasCycle(self, head):
        visited = {}  # Dictionary to store visited nodes
        
        itr = head  # Start from the given head node
        counter = 0  # Counter to track the position of the node
        
        while itr:
            if itr in visited:  # If the node itself was seen before, a cycle exists
                return True  # Found cycle

            counter += 1
            visited[itr] = counter  # Store node reference in dictionary
            
            itr = itr.next  # Move to the next node

        return False # No cycle detected