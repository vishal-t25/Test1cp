
def main():


    def recurse(list_ppl1,num_ppl1):
        bob = list_ppl1[num_ppl1 - 1]

        me = float('inf')
        
        optionA = False

        i = num_ppl1 - 2
        while i >= 0:
            if list_ppl1[i] < bob and list_ppl1[i] < me:
                me = list_ppl1[i]
            elif list_ppl1[i] < bob and list_ppl1[i] > me:
                return True
            elif list_ppl1[i] > bob:
                if me == float('inf'):
                    bob = list_ppl1[i]
                else:
                    cpy = list_ppl1[:(i+1)]
                    optionA = optionA or recurse(cpy,i+1)
                    if optionA:
                        return True

            i -= 1

        return optionA or False

    num_photos = int(input())

    inspect = []

    for idx in range(num_photos):
        num_ppl = int(input())

        list_ppl = list(map(int,input().split()))


        found = recurse(list_ppl,num_ppl)

        if found:
            inspect.append(idx+1)

        '''
        bob = list_ppl[num_ppl - 1]

        me = float('inf')
        
        found_alice = False

        i = num_ppl - 2
        while not found_alice and i >= 0:
            if list_ppl[i] < bob and list_ppl[i] < me:
                me = list_ppl[i]
            elif list_ppl[i] < bob and list_ppl[i] > me:
                found_alice = True
                inspect.append(idx)
            elif list_ppl[i] > bob:
                bob = list_ppl[i]
            

            i-=1
        '''

    print(len(inspect))
    for ins in inspect:
        print(ins)


main()

