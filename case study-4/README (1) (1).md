# Simple Dictionary Using Hash Tables

## Description
A small Python dictionary application that stores words and meanings in a hash table. It uses **separate chaining** to handle collisions.

## Features
- Add a word and meaning
- Search for a word
- Update a meaning if the word already exists
- Display all words

## How to Run
```bash
python dictionary.py
```

No extra libraries are needed.

## Sample Output
```text
Word added.
Word added.
Word added.

Search apple: A fruit
Search dog: Word not found.

All words:
apple: A fruit
book: Something to read
python: A programming language
```

## Concept
The hash function adds the character codes in a word and takes the remainder after dividing by the table size. If two words get the same index, both are stored in that bucket's list. This is called **separate chaining**.

## GitHub Description
A simple Python dictionary using a hash table and separate chaining for collision resolution.
