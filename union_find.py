class Node:
    def __init__(self, x):
        self.parent = self
        self.val = x
        self.size = 1

    @staticmethod
    def find_parent(s):
        p = s
        while p != p.parent:
            p = p.parent
        # path compression
        while s.parent != p:
            t = s.parent
            s.parent = p
            s = t
        return p

    def join(self, s):
        p1 = Node.find_parent(s)
        p2 = Node.find_parent(self)
        if p1.size < p2.size:
            p1, p2 = p2, p1

        print(p1.val, p2.val)
        p1.size += p2.size
        p2.parent = p1

        return p2

    def find_set(self):
        return Node.find_parent(self).val


s1 = Node(1)
s2 = Node(2)
s4 = Node(3)
s3 = s1.join(s2)
s5 = s3.join(s4)
print(s4.find_set())
