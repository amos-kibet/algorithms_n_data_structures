"""
You are given the heads of two sorted linked lists list1 and list2.

Merge the two lists in a one sorted list. The list should be made by splicing together the nodes of the first two lists.

Return the head of the merged linked list.

Example 1:

Input: list1 = [1,2,4], list2 = [1,3,4]
Output: [1,1,2,3,4,4]

Example 2:

Input: list1 = [], list2 = []
Output: []

Example 3:

Input: list1 = [], list2 = [0]
Output: [0]

"""



class ListNode:
  def __init__(self, val=0, next_node=None):
    self.val = val
    self.next = next_node

#   def merge_two_lists_1(l1: ListNode, l2: ListNode) -> ListNode:
#     # Check if either of the lists is null
#     if l1 is None:
#       return l2
#     if l2 is None:
#       return l1

#     # Choose head of which is smaller of the two lists
#     if l1.val < l2.val:
#       temp = head = ListNode(l1.val)
#       l1 = l1.next
#     else:
#       temp = head = ListNode(l2.val)
#       l2 = l2.next
# s
#     # Loop untill any of the lists becomes null
#     while l1 and l2:
#       if l1.val < l2.val:
#         temp.next = ListNode(l1.val)
#         l1 = l1.next
#       else:
#         temp.next = ListNode(l2.val)
#         l2 = l2.next
#       temp = temp.next

#     # Add all nodes in l1, if remaining
#     while l1:
#       temp.next = ListNode(l1.val)
#       l1 = l1.next
#       temp = temp.next

#     # Add all nodes in l2, if remaining
#     while l2:
#       temp.next = ListNode(l2.val)
#       l2 = l2.next
#       temp = temp.next
#     return head


  # def merge_two_lists_2(l1: ListNode, l2: ListNode) -> ListNode:
  #    dummy = ListNode()
  #    temp = dummy

  #    while l1 and l2:
  #     if l1.val < l2.val:
  #       temp.next = l1
  #       l1 = l1.next
  #     else:
  #       temp.next = l2
  #       l2 = l2.next
  #     temp = temp.next

  #   if l1:
  #     tail.next = l1
  #   elif l2:
  #     tail.next = l2
    
  #   return dummy.next

  # Eddie's Solution
  def mergeTwoLists(self, list1, list2):
    temporary = None
    if list1 == None:
        return list2
    
    if list2 == None:
        return list1
    
    if list1.val < list2.val:
        temporary = list1
        temporary.next = self.mergeTwoLists(list1.next, list2)
    else:
        temporary = list2
        temporary.next = self.mergeTwoLists(list1, list2.next)
        
    return temporary

  print([1,2,3,3], [2,2,3,4])