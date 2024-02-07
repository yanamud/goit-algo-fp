class Node:
  def __init__(self, data=None):
    self.data = data
    self.next = None

class LinkedList:
  def __init__(self):
    self.head = None

  def insert_at_beginning(self, data):
    new_node = Node(data)
    new_node.next = self.head
    self.head = new_node

  def insert_at_end(self, data):
    new_node = Node(data)
    if self.head is None:
      self.head = new_node
    else:
      cur = self.head
      while cur.next:
        cur = cur.next
      cur.next = new_node

  def reverse_list(self, data):
    prev = None
    cur = data.head
    while cur:
      next = cur.next
      cur.next = prev
      prev = cur
      cur = next
    data.head = prev

    print(data.print_list())

  def print_list(self):
    lst = []
    current = self.head
    while current:
      #print(current.data)
      lst.append(current.data)
      current = current.next
    return lst

  def insertion_sort(self, data):
    cur = data.head
    while cur:
        next = cur.next
        while next:
            if cur.data > next.data:
                cur.data, next.data = next.data, cur.data
            next = next.next
        cur = cur.next
    print(data.print_list())
        
#Сортування злиттям
  def merge(self, data, data1):
    merged = []
    cur1 = data.head
    cur2 = data1.head
    while cur1 and cur2:
        if cur1.data < cur2.data:
            merged.append(cur1.data)
            cur1 = cur1.next
        else:
            merged.append(cur2.data)
            cur2 = cur2.next
    while cur1:
        merged.append(cur1.data)
        cur1 = cur1.next
    while cur2:
        merged.append(cur2.data)
        cur2 = cur2.next
    return merged
###################### TASK 1.1 ###########################################
# реверсування зв'язного списку

llist = LinkedList()

# Вставляємо вузли в початок та кінець
llist.insert_at_beginning(5)
llist.insert_at_end(18)
llist.insert_at_beginning(7)
llist.insert_at_end(9)
llist.insert_at_beginning(10)
llist.insert_at_end(15)

# Друк зв'язного списку
print("\nЗв'язний список 'list_1':")
print(llist.print_list())

# Перевернути зв'язний список
print("\nРеверсований зв'язний список 'list_1':")
llist.reverse_list(llist)

###################### TASK 1.2 ###########################################
# сортування вставками зв'язного списку

print("\nСортування зв'язного списку 'list_1' вставками:")
llist.insertion_sort(llist)

###################### TASK 1.3 ###########################################
# об'єднання двох відсортованих зв'язних списків

llist_1 = LinkedList()

# Вставляємо вузли в початок та кінець
llist_1.insert_at_beginning(14)
llist_1.insert_at_end(1)
llist_1.insert_at_beginning(17)
llist_1.insert_at_end(8)
llist_1.insert_at_beginning(11)
llist_1.insert_at_end(4)

# Друк зв'язного списку
print("\nЗв'язний список 'list_2':")
print(llist_1.print_list())

print("\nВідсортований зв'язний список 'list_2':")
llist_1.insertion_sort(llist_1)

print("\nЗлиття зв'язних списків 'list_1' та 'list_2':")
res = llist.merge(llist,llist_1)
print(res)
print("\n")



