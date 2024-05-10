import linked_list

ll = linked_list.LinkedList()
ll.insert_values([9,8,3,5,2,1])
ll = ll.head

def del_at_k(node=None, curr=None, k=None, idx = 1):

    if idx == 1:
        if k == idx:
            return node.next
        curr = node

    if curr and curr.next:
        if idx + 1 == k and not curr.next.next:
            curr.next = None
            return node

        elif idx + 1 == k:
            dummy = curr.next.next
            curr.next = dummy
            return node

        else:
            return del_at_k(node=node, curr=curr.next, k = k, idx = idx + 1)

    if not curr.next:
        return node

res = del_at_k(node=ll, k=4)

while res:
    print(res.data)
    res = res.next