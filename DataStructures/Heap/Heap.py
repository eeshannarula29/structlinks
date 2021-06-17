from __future__ import annotations
from typing import Optional, Callable, Any 

from math import floor, ceil, log2

class PriorityFunction:
    def __init__(self, comaprison_function: Callable) -> None:
        self._function = comaprison_function
    
    def compare(self, parent, child) -> bool:
        return self._function(parent, child)
            
MAXPRIORITY = PriorityFunction(lambda compare_to, compare_from : compare_to >= compare_from)
MINPRIORITY = PriorityFunction(lambda compare_to, compare_from : compare_to <= compare_from)

class Heap:
    
    def __init__(self, prioritizer: PriorityFunction, inital_heep: Optional[list[Any]] = []) -> None:
        self._tree = inital_heep
        self.compare_function = prioritizer
        
        self._heapify()
        
    def _get_children(self, index) -> list[dict]:
        children = []
        
        if 2 * index + 1 < len(self._tree):
            children.append({
                'index': 2 * index + 1,
                'value': self._tree[2 * index + 1]
            })
        
        if 2 * index + 2 < len(self._tree):
            children.append({
                'index': 2 * index + 2,
                'value': self._tree[2 * index + 2]
            })    
        
        return children
    
    @property
    def size(self) -> int:
        return len(self._tree)
    
    @property
    def height(self) -> int:
        return ceil(log2(self.size + 1)) - 1
    
    def to_list(self) -> list:
        return self._tree.copy()
    
    def _is_leaf(self, index) -> bool:
        return  2 * index + 1 >= len(self._tree) and 2 * index + 2 >= len(self._tree)
    
    def _is_root(self, index) -> bool:
        return floor((index - 1)/2) < 0
    
    def _get_parent(self, index) -> dict:
        return {
            'index': floor((index - 1)/2),
            'value': self._tree[floor((index - 1)/2)] if not self._is_root(index) else None
        } 
        
    def _heapify_update(self, root_index) -> None:
        
        largest = root_index
        
        for child in self._get_children(root_index):
            if not self.compare_function.compare(self._tree[largest], child['value']): 
                largest = child['index']
        
        if not largest == root_index:
            self._tree[root_index], self._tree[largest] = self._tree[largest], self._tree[root_index]
            self._heapify_update(largest)   
    
    def _heapify(self) -> None:
        
        for index in range(len(self._tree) - 1, -1, -1):
            self._heapify_update(index)    
    
    def push(self, element) -> None:
        self._tree.append(element)
        
        child_index = len(self._tree) - 1
        parent_index = self._get_parent(child_index)
        
        while parent_index['value'] and not self.compare_function.compare(parent_index['value'], self._tree[child_index]):
            
            self._tree[child_index], self._tree[parent_index['index']] = self._tree[parent_index['index']], self._tree[child_index]
            child_index, parent_index = parent_index['index'], self._get_parent(parent_index['index'])

    def _pop_update(self, root_index) -> None:
            largest = root_index
            
            for child in self._get_children(root_index):
                if not self.compare_function.compare(self._tree[largest], child['value']): 
                    largest = child['index']
            
            if not largest == root_index:
                self._tree[root_index], self._tree[largest] = self._tree[largest], self._tree[root_index]
                self._pop_update(largest)   
            
    def pop(self) -> Any:
            self._tree[0], self._tree[len(self._tree) -1] = self._tree[len(self._tree) -1], self._tree[0]
            popped_element = self._tree.pop()
            self._pop_update(0)
            
            return popped_element
            
    def __str__(self) -> str:
        return str(self.display() if self.size > 0 else 'Empty Heap')
    
    def __repr__(self) -> str:
        return str(f'Heep(\n{self.display() if self.size > 0 else "Empty Heap"}\n)')     
    
    def display(self, listed: bool = False):
        return self._display_branched() if not listed else self._display_listed()
    
    def _display_listed(self) -> str:
        return str(self._tree)
    
    def _display_branched(self) -> str:
        string_so_far = ''
        lines, *_ = self._display_aux(0)
        for line in lines:
            string_so_far += line + '\n'

        return string_so_far

    def _display_aux(self, root_index) -> Any:
        
            children = self._get_children(root_index)
            
            if children == []:
                line = '%s' % self._tree[root_index]
                width = len(line)
                height = 1
                middle = width // 2
                
                return [line], width, height, middle

            if len(children) == 1:
                lines, n, p, x = self._display_aux(children[0]['index'])

                s = '%s' % self._tree[root_index]
                u = len(s)
                first_line = (x + 1) * ' ' + (n - x - 1) * '_' + s
                second_line = x * ' ' + '/' + (n - x - 1 + u) * ' '
                shifted_lines = [line + u * ' ' for line in lines]

                return [first_line, second_line] + shifted_lines, n + u, p + 2, n + u // 2  

            if len(children) == 2:
                left, n, p, x = self._display_aux(children[0]['index'])
                right, m, q, y = self._display_aux(children[1]['index'])

                s = '%s' % self._tree[root_index]
                u = len(s)
                first_line = (x + 1) * ' ' + (n - x - 1) * '_' + s + y * '_' + (m - y) * ' '
                second_line = x * ' ' + '/' + (n - x - 1 + u + y) * ' ' + '\\' + (m - y - 1) * ' '
                if p < q:
                    left += [n * ' '] * (q - p)
                elif q < p:
                    right += [m * ' '] * (p - q)
                zipped_lines = zip(left, right)
                lines = [first_line, second_line] + [a + u * ' ' + b for a, b in zipped_lines]

                return lines, n + m + u, max(p, q) + 2, n + u // 2                         

class MinHeap(Heap):
    def __init__(self, inital_heep: Optional[list[Any]] = []) -> None:
        super().__init__(inital_heep=inital_heep, prioritizer=MINPRIORITY)    

class MaxHeap(Heap):
    def __init__(self, inital_heep: Optional[list[Any]] = []) -> None:
        super().__init__(inital_heep=inital_heep, prioritizer=MAXPRIORITY)                