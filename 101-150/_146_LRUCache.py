class ListNode:
    def __init__(self, key, val):
        """
        双向链表
        :param key:
        :param val:
        """
        self.key = key
        self.val = val
        self.next = None
        self.prev = None
        

class LRUCache(object):

    def __init__(self, capacity):
        """
        :type capacity: int
        """
        self.hash_map = {}
        self.capacity = capacity
        
        self.head = ListNode(None, None)
        self.tail = ListNode(None, None)
        self.head.next = self.tail
        self.tail.prev = self.head

    def move_to_tail(self, node):
        # 将节点移动到tail之前
        node.next = self.tail
        node.prev = self.tail.prev

        self.tail.prev = node
        node.prev.next = node

    def get(self, key):
        """
        :type key: int
        :rtype: int
        """
        if key in self.hash_map:
            node = self.hash_map[key]
            self.move_to_tail(node)
            return node.val
        return -1

    def put(self, key, value):
        """
        :type key: int
        :type value: int
        :rtype: None
        """
        if key in self.hash_map:
            node = self.hash_map[key]
            node.val = value
            self.move_to_tail(node)
        else:
            if len(self.hash_map) == self.capacity:
                # 移去head的next节点
                remove_node = self.head.next
                self.hash_map.pop(remove_node.key)
                self.head.next = self.head.next.next
                self.head.next.prev = self.head

            # 保存节点， 双向链表节点的key和hashmap的key值相同
            node = ListNode(key, value)
            self.hash_map[key] = node
            self.move_to_tail(node)


if __name__ == '__main__':
    capacity = 2
    obj = LRUCache(capacity)
    param_1 = obj.get(1)
    print(param_1)
    obj.put(1, 2)
    param_1 = obj.get(1)
    print(param_1)
    obj.put(2, 3)
    obj.put(3, 4)
    param_1 = obj.get(1)
    print(param_1)
