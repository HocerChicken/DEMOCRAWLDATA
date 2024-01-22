import random

# Hàm tạo một từ tiếng Việt bắt đầu bằng "a"
def generate_word():
    vowels = "aeiouy"
    consonants = "bcdfghjklmnpqrstvxz"
    return 'a' + random.choice(vowels) + random.choice(consonants)

# Tạo danh sách với 500 phần tử bắt đầu bằng "a"
list_a = [generate_word() for _ in range(500)]

# In ra 10 phần tử đầu tiên để kiểm tra
print(list_a[:10])