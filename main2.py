from collections import deque


def is_palindrome(s):
    # Видалення пробілів та перетворення рядка до нижнього регістру
    s = ''.join(s.split()).lower()

    # Створення двосторонньої черги з символів рядка
    char_deque = deque(s)

    while len(char_deque) > 1:
        # Порівняння та видалення символів з обох кінців
        if char_deque.popleft() != char_deque.pop():
            return False
    return True


print(is_palindrome("A man a plan a canal Panama"))  # True
print(is_palindrome("Was it a car or a cat I saw"))  # True
print(is_palindrome("No lemon, no melon"))  # True
print(is_palindrome("Hello, world"))  # False
