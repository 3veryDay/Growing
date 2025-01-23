# 팰린드롬 연결 리스트

# 연결 리스트가 팰린드롬 구조인지 판별하라.


class Node :
    def __init__ (self, data) :
        self.data = data
        self.next = None
        
class LinkedList :
    def __init__(self) : 
        self.head = None
        self.length = 0

    
def isPalindrome(head : LinkedList) -> bool :
    q = []
    
    if not head :
        return True
    
    node = head
    
    while node is not None :
        q.append(node.data)
        node = node.next
        
    while len(q) > 1 :
        if q.pop(0) != q.pop() :
            return False
        
    return True

head = Node(1)
head.next = Node(4)
# head.next.next = Node(5)
head.next.next = Node(4)
head.next.next.next= Node(1)

print(isPalindrome(head))


from collections import deque


def usingDeque(head : LinkedList ) -> bool :
    q = deque()
    
    node = head 
    while node :
        q.append(node.data)
        node = node.next
        
    while len(q) > 1 :
        if q.popleft() != q.pop()  :
            return False
        
    return True

print(usingDeque(head))


def usingRunner(head : LinkedList ) -> bool :
    if not head :
        return True
    rev = None
    slow, fast = head, head
    
    while fast and fast.next :
        
        fast = fast.next.next
        rev, rev.next, slow = slow, rev, slow.next
        
    if fast :
        slow = slow.next
        
    while rev and rev.data == slow.data :
        slow, rev = slow.next, rev.next
        
    return not rev
        
    
    

print(usingRunner(head))