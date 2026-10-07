def make_snippet(string):
    words = string.split(' ')
    length = len(words)
    if length <= 5:
        return string
    else:
        first_five = words[0:5]
        snippet = " ".join(first_five)
        return snippet + "..."