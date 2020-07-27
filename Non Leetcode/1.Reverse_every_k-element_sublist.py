Given the head of a LinkedList and a number ‘k’, reverse every ‘k’ sized sub-list starting from the head.
If, in the end, you are left with a sub-list with less than ‘k’ elements, reverse it too.

# 1->2->3->4->5->6->7->8->null, k = 3
# output: 3->2->1->6->5->4->8->7->null 

def reverse_every_k_elements(head, k):
  # TODO: Write your code here
  if k<=1 and head is not None:
    return head

  prev, curr = None, head

  while True:
    last_node_prev_list = prev
    last_node_sub_list = curr

    i=0
    while curr is not None and i<k:
      nextn = curr.next
      curr.next = prev
      prev = curr
      curr = nextn
      i+=1

    if last_node_prev_list is not None:
      last_node_prev_list.next = prev
    else:
      head = prev

    last_node_sub_list.next = curr

    prev = last_node_sub_list

    if curr is None:
      break

  return head