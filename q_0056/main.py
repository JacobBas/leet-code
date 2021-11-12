from typing import List


def merge(intervals: List[List[int]]) -> List[List[int]]:
    resp = []
    for start, end in sorted(intervals):
        if resp:
            if resp[-1][1] >= start:
                resp[-1][1] = max(resp[-1][1], end)
            else:
                resp.append([start, end])
        else:
            resp.append([start, end])
    return resp


if __name__ == "__main__":

    mat = [[2, 3], [4, 5], [6, 7], [8, 9], [1, 10]]
    print(merge(mat))
