def custom_sort(lst):

    return sorted(lst, key=len, reverse=True)


words = ["apple", "banana", "orange", "strawberry", "grape"]
sorted_words = custom_sort(words)
print("Posortowane wyrazy od najdłuższych do najkrótszych:", sorted_words)
