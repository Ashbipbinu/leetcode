class Solution:
    def reverseList(self, head):
        # Initialize two pointers: 'curr' starts at the head, 'prev' starts as None
        curr = head
        prev = None

        # Traverse the linked list
        while curr:
            # Store the next node before modifying the current node's pointer
            temp = curr.next  
            
            # Reverse the current node's pointer to point to the previous node
            curr.next = prev  
            
            # Move 'prev' one step forward to the current node
            prev = curr  
            
            # Move 'curr' one step forward to the next node
            curr = temp  

        # 'prev' now points to the new head of the reversed linked list
        return prev
