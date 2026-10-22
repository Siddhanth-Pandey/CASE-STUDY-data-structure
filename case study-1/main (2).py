"""
E-commerce Product Sorting and Calendar Scheduling
Data Structures and Algorithms Case Study
Language: Python 3

Sorting is implemented manually (no sorted() or list.sort()).
"""

from datetime import datetime

PRODUCTS = [
    {"id": 101, "name": "T-Shirt", "price": 499.0, "rating": 4.2, "weekly_purchases": 120},
    {"id": 102, "name": "Running Shoes", "price": 1999.0, "rating": 4.7, "weekly_purchases": 85},
    {"id": 103, "name": "Backpack", "price": 899.0, "rating": 4.4, "weekly_purchases": 150},
    {"id": 104, "name": "Headphones", "price": 1499.0, "rating": 4.6, "weekly_purchases": 210},
    {"id": 105, "name": "Water Bottle", "price": 299.0, "rating": 4.0, "weekly_purchases": 95},
]

EVENTS = [
    {"id": 1, "title": "DSA Assignment", "date": "2026-10-23", "time": "10:00", "priority": 2},
    {"id": 2, "title": "Project Meeting", "date": "2026-10-22", "time": "14:30", "priority": 1},
    {"id": 3, "title": "Python Practice", "date": "2026-10-22", "time": "09:00", "priority": 3},
    {"id": 4, "title": "Case Study Submission", "date": "2026-10-25", "time": "12:00", "priority": 1},
]


def bubble_sort(items, key, descending=False):
    """Return a sorted copy using Bubble Sort."""
    result = [item.copy() for item in items]
    n = len(result)
    for i in range(n - 1):
        swapped = False
        for j in range(n - i - 1):
            left, right = result[j][key], result[j + 1][key]
            should_swap = left < right if descending else left > right
            if should_swap:
                result[j], result[j + 1] = result[j + 1], result[j]
                swapped = True
        if not swapped:
            break
    return result


def selection_sort(items, key, descending=False):
    """Return a sorted copy using Selection Sort."""
    result = [item.copy() for item in items]
    n = len(result)
    for i in range(n - 1):
        selected = i
        for j in range(i + 1, n):
            left, right = result[j][key], result[selected][key]
            if (left > right if descending else left < right):
                selected = j
        if selected != i:
            result[i], result[selected] = result[selected], result[i]
    return result


def display_products(products):
    print("\nID   Product              Price (INR)   Rating   Weekly Purchases")
    print("-" * 69)
    for p in products:
        print(f"{p['id']:<4} {p['name']:<20} {p['price']:>10.2f}   "
              f"{p['rating']:>5.1f}   {p['weekly_purchases']:>8}")


def find_product(products, query):
    """Linear search by product name (case-insensitive)."""
    query = query.strip().lower()
    for product in products:
        if query in product["name"].lower():
            return product
    return None


def product_menu():
    while True:
        print("\n--- E-COMMERCE PRODUCT SORTING ---")
        print("1. Display products")
        print("2. Sort by price (low to high) - Bubble Sort")
        print("3. Sort by rating (high to low) - Selection Sort")
        print("4. Sort by weekly purchases (high to low) - Bubble Sort")
        print("5. Search product by name - Linear Search")
        print("0. Back to main menu")
        choice = input("Enter choice: ").strip()

        if choice == "1":
            display_products(PRODUCTS)
        elif choice == "2":
            display_products(bubble_sort(PRODUCTS, "price"))
        elif choice == "3":
            display_products(selection_sort(PRODUCTS, "rating", descending=True))
        elif choice == "4":
            display_products(bubble_sort(PRODUCTS, "weekly_purchases", descending=True))
        elif choice == "5":
            query = input("Enter product name (or part of it): ")
            result = find_product(PRODUCTS, query)
            if result:
                display_products([result])
            else:
                print("Product not found.")
        elif choice == "0":
            break
        else:
            print("Invalid choice. Please try again.")


def event_datetime(event):
    return datetime.strptime(event["date"] + " " + event["time"], "%Y-%m-%d %H:%M")


def sort_events_by_datetime(events):
    """Selection Sort events chronologically using a comparable datetime key."""
    result = [event.copy() for event in events]
    n = len(result)
    for i in range(n - 1):
        earliest = i
        for j in range(i + 1, n):
            if event_datetime(result[j]) < event_datetime(result[earliest]):
                earliest = j
        if earliest != i:
            result[i], result[earliest] = result[earliest], result[i]
    return result


def display_events(events):
    print("\nID   Event                    Date         Time    Priority")
    print("-" * 61)
    for event in events:
        print(f"{event['id']:<4} {event['title']:<24} {event['date']:<12} "
              f"{event['time']:<7} {event['priority']}")


def add_event(events):
    title = input("Event title: ").strip()
    if not title:
        print("Title cannot be empty.")
        return
    date_text = input("Date (YYYY-MM-DD): ").strip()
    time_text = input("Time (HH:MM, 24-hour): ").strip()
    priority_text = input("Priority (1 = high, 2 = medium, 3 = low): ").strip()

    try:
        datetime.strptime(date_text, "%Y-%m-%d")
        datetime.strptime(time_text, "%H:%M")
        priority = int(priority_text)
        if priority not in (1, 2, 3):
            raise ValueError
    except ValueError:
        print("Invalid input. Use a valid date, time, and priority 1, 2, or 3.")
        return

    next_id = max((event["id"] for event in events), default=0) + 1
    events.append({
        "id": next_id, "title": title, "date": date_text,
        "time": time_text, "priority": priority
    })
    print("Event added successfully.")


def search_event_by_date(events, date_text):
    """Linear search for events on a specified date."""
    matches = []
    for event in events:
        if event["date"] == date_text:
            matches.append(event)
    return matches


def find_conflicts(events):
    """Find appointments with exactly the same date and start time."""
    ordered = sort_events_by_datetime(events)
    conflicts = []
    for i in range(len(ordered) - 1):
        if event_datetime(ordered[i]) == event_datetime(ordered[i + 1]):
            conflicts.append((ordered[i], ordered[i + 1]))
    return conflicts


def calendar_menu():
    while True:
        print("\n--- CALENDAR SCHEDULING ---")
        print("1. Display all events")
        print("2. Display events in chronological order")
        print("3. Add event")
        print("4. Search events by date")
        print("5. Check appointment conflicts (same date and time)")
        print("0. Back to main menu")
        choice = input("Enter choice: ").strip()

        if choice == "1":
            display_events(EVENTS)
        elif choice == "2":
            display_events(sort_events_by_datetime(EVENTS))
        elif choice == "3":
            add_event(EVENTS)
        elif choice == "4":
            date_text = input("Enter date (YYYY-MM-DD): ").strip()
            try:
                datetime.strptime(date_text, "%Y-%m-%d")
                matches = search_event_by_date(EVENTS, date_text)
                if matches:
                    display_events(matches)
                else:
                    print("No events found for that date.")
            except ValueError:
                print("Invalid date format. Use YYYY-MM-DD.")
        elif choice == "5":
            conflicts = find_conflicts(EVENTS)
            if conflicts:
                print("Conflicts found:")
                for first, second in conflicts:
                    print(f"- {first['title']} and {second['title']} at "
                          f"{first['date']} {first['time']}")
            else:
                print("No exact date-and-time conflicts found.")
        elif choice == "0":
            break
        else:
            print("Invalid choice. Please try again.")


def main():
    while True:
        print("\n==============================================")
        print(" E-COMMERCE SORTING & CALENDAR SCHEDULING")
        print("==============================================")
        print("1. E-commerce Product Sorting")
        print("2. Calendar Scheduling")
        print("0. Exit")
        choice = input("Enter choice: ").strip()

        if choice == "1":
            product_menu()
        elif choice == "2":
            calendar_menu()
        elif choice == "0":
            print("Thank you for using the case study project.")
            break
        else:
            print("Invalid choice. Please try again.")


if __name__ == "__main__":
    main()
