def swap_case(s):
    word=""
    for ch in s:
        if ch.isupper():
            word+=ch.lower()
        else:
            word+=ch.upper()
    return word

if __name__ == '__main__':
    s = input()
    result = swap_case(s)
    print(result)
