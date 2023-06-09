class Queue:
    def __init__(self, elements):
        self.elements = elements

    def is_empty(self):
        if len(self.elements) == 0:
            return True
        return False

    def put(self,element):
        return self.elements.append(element)

    def get(self):
        if not self.is_empty():
            self.elements.pop(0)
            return self.elements

    def display(self):
        print(self.elements)

def main():
    list = [1,2,3,4,5]
    fifo_queue = Queue(list)

    if fifo_queue.is_empty():
        print("Queue is empty")
    else:
        print('Queue is not empty')
        fifo_queue.display()

    fifo_queue.put(158)
    fifo_queue.display()
    print(fifo_queue.get())


if __name__ == "__main__":
    main()