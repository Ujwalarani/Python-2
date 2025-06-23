import random

def quick_sort(seq):
    if len(seq) <= 1:
        return seq

    pivot = random.choice(seq)
    rest = [x for x in seq if x != pivot]
    left = [x for x in rest if x <= pivot]
    right = [x for x in rest if x > pivot]

    return quick_sort(left) + [pivot] + quick_sort(right)

letters = list("helloworld")
sorted_letters = quick_sort(letters)
print()
print("".join(sorted_letters))
print()


words = ["banana", "apple", "orange", "mango", "grape"]
sorted_words = quick_sort(words)
print(sorted_words)
print()
# Output: ['apple', 'banana', 'grape', 'mango', 'orange']


sentence = "quick brown fox jumps over the lazy dog"
word_list = sentence.split()
sorted_sentence = quick_sort(word_list)
print(" ".join(sorted_sentence))


