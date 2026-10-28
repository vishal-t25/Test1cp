def main():
    num_photos = int(input())

    inspect = []

    for idx in range(num_photos):
        num_ppl = int(input())

        list_ppl = list(map(int,input().split()))

        
        bob = list_ppl[num_ppl - 1]

        me = float('inf')
        
        found_alice = False

        i = num_ppl - 2
        while not found_alice and i >= 0:
            if list_ppl[i] < bob and list_ppl[i] < me:
                me = list_ppl[i]
            elif list_ppl[i] < bob and list_ppl[i] > me:
                found_alice = True
                inspect.append(idx+1)
            elif list_ppl[i] > bob:
                bob = list_ppl[i]
            

            i-=1

    inspect.sort()

    print(len(inspect))
    for ins in inspect:
        print(ins)


main()

