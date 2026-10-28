import sys
input = sys.stdin.readline
def lcs_length(a, b):
    n, m = len(a), len(b)
    prev = [0] * (m + 1)

    for i in range(1, n + 1):
        curr = [0] * (m + 1)
        for j in range(1, m + 1):
            if a[i-1] == b[j-1]:
                curr[j] = prev[j-1] + 1 # characters match: extend
            else:
                curr[j] = max(prev[j], curr[j-1]) # take best of skip-a or skip-b
        prev = curr
    return prev[m]


def main():
    # Input: two strings (or sequences), one per line
    a = input().strip()
    b = "abcdefghijklmnopqrstuvwxyz"
    print(26 - lcs_length(a, b))
        
main()