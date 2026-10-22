"""
Case Study: Implementation of Stack and Queue Operations Using Linked Lists
Language: Python 3

This program implements:
1. Stack using a singly linked list (push, pop, peek, display)
2. Queue using a singly linked list (enqueue, dequeue, peek, display)
"""

class Node:
    """A node in a singly linked list."""
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedListStack:
    """Stack implementation using a linked list (LIFO)."""
    def __init__(self):
        self.top = None

    def is_empty(self):
        return self.top is None

    def push(self, data):
        new_node = Node(data)
        new_node.next = self.top
        self.top = new_node
        print(f"{data} pushed onto the stack.")

    def pop(self):
        if self.is_empty():
            print("Stack underflow! The stack is empty.")
            return None
        data = self.top.data
        self.top = self.top.next
        print(f"Popped element: {data}")
        return data

    def peek(self):
        if self.is_empty():
            print("Stack is empty.")
            return None
        print(f"Top element: {self.top.data}")
        return self.top.data

    def display(self):
        if self.is_empty():
            print("Stack is empty.")
            return
        current = self.top
        print("Stack (top to bottom):", end=" ")
        while current:
            print(current.data, end=" ")
            current = current.next
        print()


class LinkedListQueue:
    """Queue implementation using a linked list (FIFO)."""
    def __init__(self):
        self.front = None
        self.rear = None

    def is_empty(self):
        return self.front is None

    def enqueue(self, data):
        new_node = Node(data)
        if self.is_empty():
            self.front = self.rear = new_node
        else:
            self.rear.next = new_node
            self.rear = new_node
        print(f"{data} added to the queue.")

    def dequeue(self):
        if self.is_empty():
            print("Queue underflow! The queue is empty.")
            return None
        data = self.front.data
        self.front = self.front.next
        if self.front is None:
            self.rear = None
        print(f"Removed element: {data}")
        return data

    def peek(self):
        if self.is_empty():
            print("Queue is empty.")
            return None
        print(f"Front element: {self.front.data}")
        return self.front.data

    def display(self):
        if self.is_empty():
            print("Queue is empty.")
            return
        current = self.front
        print("Queue (front to rear):", end=" ")
        while current:
            print(current.data, end=" ")
            current = current.next
        print()


def stack_menu(stack):
    while True:
        print("\\n--- STACK OPERATIONS ---")
        print("1. Push")
        print("2. Pop")
        print("3. Peek")
        print("4. Display")
        print("5. Back to main menu")
        choice = input("Enter your choice: ").strip()

        if choice == "1":
            value = input("Enter value to push: ")
            stack.push(value)
        elif choice == "2":
            stack.pop()
        elif choice == "3":
            stack.peek()
        elif choice == "4":
            stack.display()
        elif choice == "5":
            break
        else:
            print("Invalid choice. Please enter 1 to 5.")


def queue_menu(queue):
    while True:
        print("\\n--- QUEUE OPERATIONS ---")
        print("1. Enqueue")
        print("2. Dequeue")
        print("3. Peek")
        print("4. Display")
        print("5. Back to main menu")
        choice = input("Enter your choice: ").strip()

        if choice == "1":
            value = input("Enter value to enqueue: ")
            queue.enqueue(value)
        elif choice == "2":
            queue.dequeue()
        elif choice == "3":
            queue.peek()
        elif choice == "4":
            queue.display()
        elif choice == "5":
            break
        else:
            print("Invalid choice. Please enter 1 to 5.")


def main():
    stack = LinkedListStack()
    queue = LinkedListQueue()

    while True:
        print("\\n===== STACK AND QUEUE USING LINKED LISTS =====")
        print("1. Stack operations")
        print("2. Queue operations")
        print("3. Exit")
        choice = input("Enter your choice: ").strip()

        if choice == "1":
            stack_menu(stack)
        elif choice == "2":
            queue_menu(queue)
        elif choice == "3":
            print("Thank you! Program ended.")
            break
        else:
            print("Invalid choice. Please enter 1, 2, or 3.")


if __name__ == "__main__":
    main()
