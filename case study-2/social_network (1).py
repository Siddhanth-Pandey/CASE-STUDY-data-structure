# Social Network Friendship Game
# Enter 1 if two users are friends, or 0 if they are not.

users = ["Alice", "Bob", "Charlie", "David", "Emma"]

# Hidden friendship matrix: 1 = friends, 0 = not friends
matrix = [
    [0, 1, 0, 1, 0],
    [1, 0, 1, 0, 0],
    [0, 1, 0, 0, 1],
    [1, 0, 0, 0, 1],
    [0, 0, 1, 1, 0]
]

print("SOCIAL NETWORK FRIENDSHIP GAME")
print("Users:", ", ".join(users))
print("Enter 1 if they are friends, or 0 if they are not friends.\n")

pairs = [
    ("Alice", "Bob"),
    ("Alice", "Charlie"),
    ("Bob", "Charlie"),
    ("Charlie", "Emma"),
    ("David", "Emma")
]

score = 0

for user1, user2 in pairs:
    answer = input(f"Are {user1} and {user2} friends? (0/1): ").strip()

    while answer not in ("0", "1"):
        answer = input("Please enter only 0 or 1: ").strip()

    i = users.index(user1)
    j = users.index(user2)
    correct_answer = str(matrix[i][j])

    if answer == correct_answer:
        print("Correct!\n")
        score += 1
    else:
        print(f"Incorrect. The correct answer is {correct_answer}.\n")

print(f"Game over! Your score: {score}/{len(pairs)}")
