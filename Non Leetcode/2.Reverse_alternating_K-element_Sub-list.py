Given the head of a LinkedList and a number ‘k’, reverse every alternating ‘k’ sized sub-list starting from the head.
If, in the end, you are left with a sub-list with less than ‘k’ elements, reverse it too.

# 1->2->3->4->5->6->7->8->null
# output: 2->1->3->4->6->5->7->8->null

def reverse_alternate_k_elements(head, k):
  # TODO: Write your code here
  if k<=1 or head is None:
    return head

  prev, curr = None, head
  while True:

    last_node_prev_list = prev
    last_node_sub_list = curr

    count=0
    while curr is not None and count<k:
      nextn = curr.next
      curr.next = prev
      prev = curr
      curr = nextn
      count+=1

    if last_node_prev_list is not None:
      last_node_prev_list.next = prev
    else:
      head=prev  

    last_node_sub_list.next = curr

    i = 0
    while curr is not None and i<k:
      prev = curr
      curr = curr.next
      i+=1

    if curr is None:
      break

  return head