# Name: Vasu Parmar
# Enrollment: 92600565007

print("Name: Vasu Parmar")
print("Enrollment: 92600565007")

# Q-10 Python Programs to perform various operations on Strings using functions


def string_length(s):
    return len(s)


def uppercase_string(s):
    return s.upper()


def lowercase_string(s):
    return s.lower()


def concatenate_strings(s1, s2):
    return s1 + s2


def reverse_string(s):
    return s[::-1]


def count_vowels(s):
    vowels = "aeiouAEIOU"
    return sum(1 for ch in s if ch in vowels)


text = "Python Programming"
name = "Vasu"

print("Original string:", text)
print("Length:", string_length(text))
print("Uppercase:", uppercase_string(text))
print("Lowercase:", lowercase_string(text))
print("Concatenation:", concatenate_strings("Hello ", "World"))
print("Reverse:", reverse_string(text))
print("Vowel count:", count_vowels(text))
print("Name:", name)
