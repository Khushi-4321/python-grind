# Write a recursive function that reverses a string.
# recursive_reverse("hello") → "olleh"

def recursive_reverse(s):
    if s == "":
        return ""
    return (s[-1]) + recursive_reverse(s[:-1]) 

s = "hello"
print(recursive_reverse(s))