__author__ = 'stephenosullivan'

def charAt(s, i):
    if len(s) - 1 < i:
        return " "

    return s[i]

if __name__ == "__main__":
    print(charAt("This is a sentence", 14))
