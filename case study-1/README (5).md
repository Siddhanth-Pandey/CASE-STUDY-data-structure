# E-commerce Product Sorting and Calendar Scheduling

A menu-driven Python case study demonstrating how **Data Structures and Algorithms (DSA)** can be applied to online shopping and calendar management.

## Project modules

### 1. E-commerce Product Sorting
- Displays a sample product catalogue.
- Sorts products by price (ascending) using Bubble Sort.
- Sorts products by rating (descending) using Selection Sort.
- Sorts products by weekly purchases (descending) using Bubble Sort.
- Searches for products by name using Linear Search.
- Uses sample product records stored in a list of dictionaries.

### 2. Calendar Scheduling
- Displays saved events.
- Sorts events chronologically by date and time using Selection Sort.
- Adds events after validating the date, time, and priority.
- Searches for events by date using Linear Search.
- Detects appointments that have exactly the same date and start time.
- Stores events in a list of dictionaries.

> Conflict detection in this educational version checks for identical start date/time only. It does not check overlapping event durations because event durations are not stored.

## Technologies
- Python 3
- `datetime` standard library
- Lists and dictionaries
- Bubble Sort, Selection Sort, and Linear Search

No third-party packages are required.

## Repository structure

```text
Ecommerce-Product-Sorting-and-Calendar-Scheduling/
├── main.py
├── README.md
└── sample_output/
    └── output.txt
```

## How to run

1. Install Python 3 if it is not already installed.
2. Download or clone this repository.
3. Open a terminal in the project folder.
4. Run:

```bash
python main.py
```

On some systems, use `python3 main.py`.

## Main menu

```text
==============================================
 E-COMMERCE SORTING & CALENDAR SCHEDULING
==============================================
1. E-commerce Product Sorting
2. Calendar Scheduling
0. Exit
Enter choice:
```

Choose `1` for product operations or `2` for calendar operations. Follow the prompts shown in the terminal.

## Data structures and algorithms

| Feature | Data structure / algorithm | Time complexity |
|---|---|---|
| Store products and events | List of dictionaries | — |
| Sort products by price | Bubble Sort | Best: O(n) with early exit; average/worst: O(n²) |
| Sort products by rating | Selection Sort | O(n²) |
| Sort products by weekly purchases | Bubble Sort | Best: O(n) with early exit; average/worst: O(n²) |
| Sort events by date and time | Selection Sort | O(n²) |
| Search products by name | Linear Search | Best: O(1); worst: O(n) |
| Search events by date | Linear Search | O(n) |
| Add event to Python list | `append()` | Amortized O(1) |
| Check exact-time conflicts | Sort then scan | O(n²) overall |

Here, `n` is the number of products or events. The project deliberately implements sorting manually instead of using `sorted()` or `.sort()`, so the algorithms are easier to study.

## Sample data

The program starts with five products and four calendar events. Changes made while the program is running are stored in memory and reset when the program exits.

## Learning objectives
- Understand how sorting algorithms arrange records.
- Compare Bubble Sort and Selection Sort.
- Apply Linear Search to small datasets.
- Validate date and time input with Python's `datetime` module.
- Analyse algorithm time complexity.
- Organize a small project for GitHub.

## Limitations and future improvements
- Save products and events to CSV, JSON, or a database.
- Add product categories and user-selected sort options.
- Store event duration and detect overlapping appointments.
- Add recurring events, reminders, and calendar views.
- Build a graphical user interface or web application.

## Conclusion

This case study connects fundamental DSA concepts to two practical scenarios: organizing e-commerce products and scheduling calendar events. It is intended for learning and demonstration, not as a production shopping or calendar service.
