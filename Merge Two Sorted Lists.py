class Solution(object):
    def mergeTwoLists(self, list1, list2):
        # Create a dummy node to act as the starting point of the merged list
        dummy = ListNode()
        # 'tail' will be used to build the merged list
        tail = dummy  

        # Traverse both lists while they are not empty
        while list1 is not None and list2 is not None:
            if list1.val <= list2.val:
                # Attach list1's node to the merged list
                tail.next = list1  
                list1 = list1.next  # Move list1 forward
            else:
                # Attach list2's node to the merged list
                tail.next = list2  
                list2 = list2.next  # Move list2 forward
            
            # Move the tail forward
            tail = tail.next  

        # If one list is empty, attach the remaining part of the other list
        if list1 is not None:
            tail.next = list1  
        else:
            tail.next = list2  

        # Return the merged list starting from the first real node
        return dummy.next  
