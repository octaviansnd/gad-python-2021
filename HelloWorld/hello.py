import sys


s1 = ''


def convert(s, s1):
    if len(s) == 0 or s == '\n':
        return
    s1 += s[0].lower()
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
            print(s1)
            return
        convert(line, s1)


if __name__ == "__main__":
    main()

