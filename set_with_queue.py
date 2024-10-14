from fila_array import FilaArray

class SetWithQueue:
    def __init__(self):
        self._fila_array = FilaArray()

    def add(self, element):
        if not(self.contains(element)):
            self._fila_array.enqueue(element)

    def remove(self, element):
        contains_element = False
        for i in range(self.size()):
            e = self._fila_array.dequeue()
            if e == element:
                contains_element = True
            else:
                self._fila_array.enqueue(e)

        if not(contains_element):
            raise ValueError('Element not found')
           
    def contains(self, element):
        contains_element = False
        for i in range(self.size()):
            e = self._fila_array.dequeue()
            self._fila_array.enqueue(e)
            if e == element:
                contains_element = True
        return contains_element

    def size(self):
        return self._fila_array.__len__()

    def list(self):
        elements = []
        for i in range(self.size()):
            e = self._fila_array.dequeue()
            elements.append(e)
            self._fila_array.enqueue(e)            
        return elements