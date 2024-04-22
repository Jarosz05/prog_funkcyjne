from collections import Counter

def most_common_element(lst):
    count = Counter(lst)
    return max(count, key=count.get)

my_list = [1, 2, 3, 4, 2, 2, 3, 3, 3]
result = most_common_element(my_list)
print("Najczęściej występująca cyfra:", result)
