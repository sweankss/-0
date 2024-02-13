class LinkedList:
    class Item:
        value = None
        next = None

        def __init__(self, value):
            self.value = value

    def __init__(self):
        self.head = None

    def append_begin(self, value):
        item = LinkedList.Item(value)
        item.next = self.head
        self.head = item

    def append_end(self, value):
        current = self.head
        if current is None:
            self.head = LinkedList.Item(value)
            self.head.value = value
            return

        while current.next:
            current = current.next

        item = LinkedList.Item(value)
        current.next = item

    def append_by_index(self, value, index):
        if index < 0 or index > len(self):
            raise ValueError("Invalid index.")

        if index == 0:
            self.append_begin(value)
        else:
            current = self.head
            for _ in range(index - 1):
                current = current.next

            item = LinkedList.Item(value)
            item.next = current.next
            current.next = item

    def __len__(self):
        count = 0
        current = self.head
        while current:
            count += 1
            current = current.next
        return count

    def remove_first(self):
        if self.head:
            self.head = self.head.next
        else:
            raise ValueError("List is empty, cannot remove the first element.")

    def remove_last(self):
        if self.head:
            if self.head.next is None:
                self.head = None
            else:
                current = self.head
                while current.next.next:
                    current = current.next
                current.next = None
        else:
            raise ValueError("List is empty, cannot remove the last element.")

    def remove_at(self, index):
        if index < 0 or index >= len(self):
            raise ValueError("Invalid index.")

        if index == 0:
            self.remove_first()
        else:
            current = self.head
            for _ in range(index - 1):
                current = current.next
            current.next = current.next.next

    def remove_first_value(self, value):
        if self.head:
            if self.head.value == value:
                self.head = self.head.next
            else:
                current = self.head
                while current.next and current.next.value != value:
                    current = current.next
                if current.next and current.next.value == value:
                    current.next = current.next.next
                else:
                    raise ValueError(f"Value '{value}' not found in the list.")
        else:
            raise ValueError("List is empty, value cannot be removed.")

    def remove_last_value(self, value):
        if self.head:
            previous = None
            current = self.head
            while current.next:
                if current.next.value == value:
                    previous = current
                current = current.next
            if previous:
                previous.next = previous.next.next
            else:
                raise ValueError(f"Value '{value}' not found in the list.")
        else:
            raise ValueError("List is empty, value cannot be removed.")
        
        
    def get_item(self): 
        current = self.head 
        while current != None: 
            yield current.value 
            current = current.next 
 
my_list = LinkedList() 
my_list.append_end(1) 
my_list.append_end(0) 
my_list.append_end(2) 
my_list.append_end(0) 
my_list.append_end(3) 
my_list.append_end(0) 
my_list.append_end(4) 
 
try:
    my_list.remove_first()
    # my_list.remove_last() 
    # my_list.remove_at(8)
    # my_list.remove_first_value(0) 
    # my_list.remove_last_value(0)
except ValueError as e:
    print(e) 
 
for value in my_list.get_item(): 
    print(value)