# 56. Word Ladder Problem
# ------------------------------------------------------------
# CODE FLOW:
# 1. Start from the beginning word.
# 2. At each step, change one letter at a time.
# 3. If the new word is in the dictionary and not visited, add to the queue.
# 4. Use BFS to ensure the shortest path is found.
# 5. Continue until the target word is reached or no more words remain.
#
# REAL-WORLD USE CASE:
# This is similar to finding the shortest transformation in data correction,
# such as suggesting the closest valid word from a dictionary in a spell checker.

from collections import deque

def word_ladder(beginWord, endWord, wordList):
    wordSet = set(wordList)
    if endWord not in wordSet:
        return 0

    queue = deque([(beginWord, 1)])  # (current_word, transformation_steps)

    while queue:
        word, steps = queue.popleft()

        if word == endWord:
            return steps

        for i in range(len(word)):
            for c in 'abcdefghijklmnopqrstuvwxyz':
                next_word = word[:i] + c + word[i+1:]
                if next_word in wordSet:
                    wordSet.remove(next_word)
                    queue.append((next_word, steps + 1))

    return 0

# Example execution:
begin = "hit"
end = "cog"
dictionary = ["hot", "dot", "dog", "lot", "log", "cog"]

result = word_ladder(begin, end, dictionary)

print(f"Shortest transformation length from '{begin}' to '{end}': {result}")


# Shortest transformation length from 'hit' to 'cog': 5  =ouput