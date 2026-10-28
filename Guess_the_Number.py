import sys

def main():
    max_val = 1000
    min_val = 1

    mid = (max_val+min_val)/2

    print(mid)
    inp = input().strip()

    while inp != "correct":
        if inp == "lower":
            max_val = mid -1
        else:
            min_val = mid + 1
        

        mid = (max_val+min_val)//2
        print(mid)
        inp = input().strip()

    return

main()