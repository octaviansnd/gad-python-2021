import sys


def convert(s):
    if len(s) == 0 or s == '\n':
        return
    s1 = s[0].lower()
    for i in range(1, len(s)):
        if s[i] == ' ':
            i += 1
            s1 += s[i].upper()
        if s[i-1] == ' ':
            s1 += ""
        else:
            s1 += s[i].lower()
    print(s1)


def main():
    for line in sys.stdin:
        if line == "Exit\n":
            return
        convert(line)


if __name__ == "__main__":
    main()

