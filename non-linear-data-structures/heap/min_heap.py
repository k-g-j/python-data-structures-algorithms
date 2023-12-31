"""
MinHeap tracks the minimum element as the element at index 1 within an internal Python list.

When adding elements, use .heapify_up() to compare the new element with its parent, making swaps if it violates the heap property: children must be greater than their parents.

When removing the minimum element, swap it with the last element in the list. Then use .heapify_down() to compare the new root with its children, swapping with the smaller child if necessary.

Heaps are useful because they are efficient in maintaining their heap properties. 
"""


class MinHeap:
    def __init__(self):
        self.heap_list = [None]
        self.count = 0

    def parent_idx(self, idx):
        return idx // 2

    def left_child_idx(self, idx):
        return idx * 2

    def right_child_idx(self, idx):
        return idx * 2 + 1

    def child_present(self, idx):
        return self.left_child_idx(idx) <= self.count

    def retrieve_min(self):
        if self.count == 0:
            print("No items in heap")
            return None

        min = self.heap_list[1]
        self.heap_list[1] = self.heap_list[self.count]
        self.count -= 1
        self.heap_list.pop()
        self.heapify_down()
        return min

    def add(self, element):
        self.count += 1
        self.heap_list.append(element)
        self.heapify_up()

    def get_smaller_child_idx(self, idx):
        if self.right_child_idx(idx) > self.count:
            return self.left_child_idx(idx)
        else:
            left_child = self.heap_list[self.left_child_idx(idx)]
            right_child = self.heap_list[self.right_child_idx(idx)]
            if left_child < right_child:
                return self.left_child_idx(idx)
            else:
                return self.right_child_idx(idx)

    def heapify_up(self):
        idx = self.count
        swap_count = 0
        while self.parent_idx(idx) > 0:
            if self.heap_list[self.parent_idx(idx)] > self.heap_list[idx]:
                swap_count += 1
                tmp = self.heap_list[self.parent_idx(idx)]
                self.heap_list[self.parent_idx(idx)] = self.heap_list[idx]
                self.heap_list[idx] = tmp
            idx = self.parent_idx(idx)

        element_count = len(self.heap_list)
        if element_count > 10000:
            print("Heap of {0} elements restored with {1} swaps"
                  .format(element_count, swap_count))
            print("")

    def heapify_down(self):
        idx = 1
        # starts at 1 because we swapped first and last elements
        swap_count = 1
        while self.child_present(idx):
            smaller_child_idx = self.get_smaller_child_idx(idx)
            if self.heap_list[idx] > self.heap_list[smaller_child_idx]:
                swap_count += 1
                tmp = self.heap_list[smaller_child_idx]
                self.heap_list[smaller_child_idx] = self.heap_list[idx]
                self.heap_list[idx] = tmp
            idx = smaller_child_idx

        element_count = len(self.heap_list)
        if element_count >= 10000:
            print("Heap of {0} elements restored with {1} swaps"
                  .format(element_count, swap_count))
            print("")
