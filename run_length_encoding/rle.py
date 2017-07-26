def encode(s):
    if len(s) > 0:
        char = s[0]
        count = 1
        result = ''
        for c in s[1:]:
            if c == char:
                count += 1
            else:
                if count == 1:
                    result += char
                else:
                    result += str(count) + char
                char = c
                count = 1
        if count == 1:
            result += char
        else:
            result += str(count) + char
        return result
    return ''


def decode(s):
    result = ''
    n = 0
    for c in s:
        if c.isdigit():
            n = n * 10 + int(c)
        else:
            if n == 0:
                n = 1
            result += c * n
            n = 0
    return result
