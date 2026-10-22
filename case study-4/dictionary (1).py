# Simple Dictionary using a Hash Table
# Collision resolution: Separate Chaining

class Dictionary:
    def __init__(self, size=10):
        self.size = size
        self.table = [[] for _ in range(size)]

    def hash_word(self, word):
        return sum(ord(char) for char in word.lower()) % self.size

    def add(self, word, meaning):
        index = self.hash_word(word)
        for item in self.table[index]:
            if item[0] == word.lower():
                item[1] = meaning
                print("Meaning updated.")
                return
        self.table[index].append([word.lower(), meaning])
        print("Word added.")

    def search(self, word):
        index = self.hash_word(word)
        for item in self.table[index]:
            if item[0] == word.lower():
                return item[1]
        return "Word not found."

    def display(self):
        for bucket in self.table:
            for word, meaning in bucket:
                print(f"{word}: {meaning}")


dictionary = Dictionary()

dictionary.add("apple", "A fruit")
dictionary.add("book", "Something to read")
dictionary.add("python", "A programming language")

print("\nSearch apple:", dictionary.search("apple"))
print("Search dog:", dictionary.search("dog"))

print("\nAll words:")
dictionary.display()
