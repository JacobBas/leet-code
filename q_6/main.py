from math import floor


def convert(s: str, numRows: int) -> str:
    if numRows == 1:
        return s

    rows = ["" for i in range(numRows)]
    i = 0
    j = 0
    dir = 1
    while (i < len(s)):
        rows[j] += s[i]
        if j == (numRows - 1):
            dir = -1
        if j == 0:
            dir = 1

        j += dir
        i += 1

    return ''.join(rows)


if __name__ == '__main__':
    print(convert('PAYPALISHIRING', 4))
