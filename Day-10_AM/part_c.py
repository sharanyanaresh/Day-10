from collections import defaultdict

# Q1 Conceptual answers
print("Dict lookup, insert, delete average time complexity: O(1)")
print("Worst case: O(n) when hash collisions occur")
print("Python uses hash tables for dictionaries")
print("Strings are hashed using character-based algorithms")
print("Integers use direct numeric hashing")
print("Use dict when you need fast key-value lookup")


# Q2 Group Anagrams
def group_anagrams(words):
    groups = defaultdict(list)

    for word in words:
        key = "".join(sorted(word))
        groups[key].append(word)

    return dict(groups)


print(group_anagrams(['eat', 'tea', 'tan', 'ate', 'nat', 'bat']))


# Q3 Debugged char frequency function
def char_freq(text):

    freq = {}

    for char in text:
        freq[char] = freq.get(char, 0) + 1

    sorted_freq = sorted(freq.items(), key=lambda x: x[1], reverse=True)

    return sorted_freq


print(char_freq("programming"))