"""
Your task is to divide a string into segments so that each segment is a repeat of the same character. The segments should be represented as a list of pairs containing the segments lengths and characters.

For example, the string aaabbccdddd has four segments and can be represented as the list [(3, 'a'), (2, 'b'), (2, 'c'), (4, 'd')].

In a file segments.py, implement the function find_segments with a string as a parameter. The function returns a list of pairs representing the segments of the string.

Your function will be tested using many different strings. Each test string consists of the characters a–z and contains 1–100 characters.

"""


def find_segments(data):
    letter = ''
    segments = []
    count = 0
    for char in data:
        if char == letter:
            count += 1
        else:
            if count > 0:
                segments.append((count, letter))
            letter = char
            count = 1
    if count > 0:
        segments.append((count, letter))

    return segments



if __name__ == "__main__":
    print(find_segments("aaabbccdddd"))
    # [(3, 'a'), (2, 'b'), (2, 'c'), (4, 'd')]

    print(find_segments("aaaaaaaaaaaaaaaaaaaa"))
    # [(20, 'a')]

    print(find_segments("abcabc"))
    # [(1, 'a'), (1, 'b'), (1, 'c'), (1, 'a'), (1, 'b'), (1, 'c')]

    print(find_segments("kissa"))
    # [(1, 'k'), (1, 'i'), (2, 's'), (1, 'a')]

    print(find_segments("mmzxzj"))
    # [(2, 'm'), (1, 'z'), (1, 'x'), (1, 'z'), (1, 'j')]

