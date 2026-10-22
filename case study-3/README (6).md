# Case Study: Implementation of Stack and Queue Operations Using Linked Lists

## Aim
To implement stack and queue data structures using a singly linked list in Python.

## Overview
A linked list stores data in nodes. Each node contains a value and a reference to the next node. Unlike arrays, a linked list can grow or shrink dynamically as nodes are added or removed.

- **Stack (LIFO):** Last In, First Out. The most recently inserted element is removed first.
- **Queue (FIFO):** First In, First Out. The earliest inserted element is removed first.

## Operations Implemented

### Stack
- `push(value)` — adds an element to the top.
- `pop()` — removes the top element.
- `peek()` — shows the top element without removing it.
- `display()` — displays elements from top to bottom.

### Queue
- `enqueue(value)` — adds an element at the rear.
- `dequeue()` — removes an element from the front.
- `peek()` — shows the front element without removing it.
- `display()` — displays elements from front to rear.

The program also handles attempts to remove or view elements when a structure is empty.

## Requirements
- Python 3.x
- No external libraries are required.

## How to Run
1. Download or clone this repository.
2. Open a terminal in the project folder.
3. Run:

   ```bash
   python stack_queue_linked_list.py
   ```

4. Select Stack or Queue operations from the main menu and follow the prompts.

## Sample Run
A sample session is provided in [`sample_output.txt`](sample_output.txt). The program is interactive, so your exact output will depend on the choices and values entered.

## Time Complexity
| Operation | Time Complexity |
|---|---|
| Stack push | O(1) |
| Stack pop | O(1) |
| Stack peek | O(1) |
| Stack display | O(n) |
| Queue enqueue | O(1) |
| Queue dequeue | O(1) |
| Queue peek | O(1) |
| Queue display | O(n) |

## Conclusion
Stack and queue operations can be implemented efficiently with a linked list. Insertion and deletion at the stack top, and queue front/rear, take constant time, O(1). Linked lists also allow the structures to grow dynamically without requiring a fixed capacity.

## Repository Files
- `stack_queue_linked_list.py` — source code
- `sample_output.txt` — example program output
- `README.md` — project documentation
