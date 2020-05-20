from collections import Counter
# read data from text file 
f = open("DFA_Input_1.txt",'r')
alphabet = f.readline().split()
all_states = f.readline().split()
start_state =  f.readline().strip()
finite_states = f.readline().split()
#transmisions is our delta 
transmissions = {}

# for reducing memory usage we use list for transmision and dicuse it in worksheet
for x in all_states :
    transmissions[x] = [None]*len(alphabet)


# here we dont use while loop because we are sure that each dfa delta function for every state has vertex by number of alphabet letters
for i in range (len(alphabet)*len(all_states)):
    trans = f.readline().split()
    alp_index = alphabet.index(trans[1])
    transmissions[trans[0]][alp_index] = trans[2]
# print(transmissions)



while (True):
    inputStr = input("input your string : ")
    if inputStr == "exit":
        break
    
    # here we check if input string contains some letters that we dont have them in out alphabet 
    # warn the user and wants input new string
    string_letters =list(Counter(inputStr).keys())
    if set(string_letters)- set(alphabet) == set():
        pass
    else:
        print("your string contains some letters that is not in your dfa alphabet")
        print("try again")
        continue

    # ps is stand for present state 
    ps = start_state   
    for char in inputStr :
        ps = transmissions[ps][alphabet.index(char)]

    # after iteration bt alphabet and
    if (ps in finite_states):
        print("accepted string")
    else:
        print("string is not accpeted")    






