import random
class Minheap:
    def __init__(self):
        self.data = [None]

    def pop(self):
        if len(self.data) == 2:
            return self.data.pop(1)
        answer = self.data[1]
        self.data[1] = self.data.pop(len(self.data) - 1)
        parent_index = 1
        self.sift_down()
        return answer

    def sift_down(self):
        parent_index = 1
        while True:
            left_child = 2 * parent_index
            right_child = left_child + 1
            heap_size = len(self.data)
            if right_child >= heap_size:
                break
            if self.data[left_child] < self.data[right_child]:
                min_child_index = left_child
            else:
                min_child_index = right_child
            if self.data[parent_index] <= self.data[min_child_index]:
                break
            self.data[parent_index], self.data[min_child_index] = self.data[min_child_index], self.data[parent_index]
            parent_index = min_child_index


    def push(self, value):
        child_index = len(self.data)
        self.data.append(value)
        while child_index > 1:
            parent_index = child_index // 2
            if self.data[parent_index] <= value:
                break
            self.data[parent_index], self.data[child_index] = \
            self.data[child_index], self.data[parent_index]
            child_index = parent_index

    def index_for_swap(self, left_child):
        right_child = left_child + 1

    def __repr__(self):
        return "Minheap(" + str(self.data) + ")"

m = Minheap()
m.push(8)
m.push(7)
m.push(3)
m.push(5)
print(m)