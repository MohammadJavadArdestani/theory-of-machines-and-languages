import os
#here we read data from text file 
f = open("NFA_Input_2.txt",'r')
landa_alphabet = f.readline().split()
landa_alphabet.append('Î»')
landa_all_states = f.readline().split()
landa_start_state =  f.readline().strip()
landa_finite_states = f.readline().split()
landa_NFA_transmissions = {}
landa_closure = {}
for x in landa_all_states :
    landa_NFA_transmissions[x] = {}
    landa_closure[x]  = []



#read each transmision from text file and add it onto landa_NFA_transmision which is a dictionary as you can see above
while(True):
    trans = f.readline()
    if not trans:
        break
    trans = trans.split()
    if trans[1]  in  landa_NFA_transmissions[trans[0]].keys():
        landa_NFA_transmissions[trans[0]][trans[1]].append(trans[2])
    else:      
        landa_NFA_transmissions[trans[0]][trans[1]] = [trans[2]]
f.close()

# print(landa_NFA_transmissions)



#a recursive function that iterate among states by landa and add each state to closure set of states
# this function get 2 input first ,first starting state and second clouser state 
# we start from state and iterate by landa and add new state to closuer set of closure state
def create_landa_clouser(state,clouser_state):
    ps = state
    if 'Î»' in landa_NFA_transmissions[ps].keys() : 
        ns = landa_NFA_transmissions[ps]['Î»']
        landa_closure[clouser_state].extend(ns)
        landa_closure[clouser_state] = list(set( landa_closure[clouser_state]))
        for ns_eleman in ns:
            ps = ns_eleman
            create_landa_clouser(ps,clouser_state)
    else:
        return    

#call our recursive function for each state and booth are same 

for x in landa_NFA_transmissions.keys(): 
    create_landa_clouser(x,x)

# add eaach state to closuer set of each itself
for x in landa_closure.keys():
    landa_closure[x].append(x)
    #by casting list to set and then cast it to list we prevent repeated eleman 
    landa_closure[x]=list(set(landa_closure[x]))    
# print(landa_closure)



# create wo_landa_NFA_finite_stete by adding each state that has finite state in its closure  into landa_finite_states
wo_landa_NFA_finite_stete = landa_finite_states
for y in landa_closure.keys():
    for x in landa_finite_states:
        if x in landa_closure[y]:
            wo_landa_NFA_finite_stete.append(y)
            break

wo_landa_NFA_finite_stete = list(set(wo_landa_NFA_finite_stete))         




# this part of code has 4 indentation of for loops and its not good in time complexity but
# we are sure this algorithem is proper for every landa_nfa
# in worksheet we dicuse about relation of algorith and code 
wo_landa_NFA_transmisions ={}
for x in  landa_all_states :
    wo_landa_NFA_transmisions[x] = {}
for state in landa_all_states:
    for closuer_state in landa_closure[state]:
        for alphabet_letter in landa_alphabet[:-1]:
            if alphabet_letter == 'Î»':
                continue
            if alphabet_letter in landa_NFA_transmissions[closuer_state].keys():
                wo_landa_NFA_transmisions[state][alphabet_letter]=[]
                for x in landa_NFA_transmissions[closuer_state][alphabet_letter]:
                    wo_landa_NFA_transmisions[state][alphabet_letter].extend(landa_closure[x])                
# print(wo_landa_NFA_transmisions)




# writing data in standard format into text file 

fw = open("wo_landa_NFA.txt","w")
fw.write(" ".join(landa_alphabet[:-1])+"\n")
fw.write(" ".join(landa_all_states)+"\n")
fw.write(landa_start_state+"\n")
fw.write(" ".join(wo_landa_NFA_finite_stete)+"\n")
for x in wo_landa_NFA_transmisions.keys() :
    for y in wo_landa_NFA_transmisions[x].keys() :
        for z in wo_landa_NFA_transmisions[x][y]:
            fw.write(x+" ")
            fw.write(y+" ")
            fw.write(z)
            fw.write("\n")
fw.close()

#until now we create a nfa without landa and save it 


#************************************************************************


# here we want cast nfa into dfa


#reading data from text file 
f = open("wo_landa_NFA.txt",'r')
alphabet = f.readline().split()
all_states = f.readline().split()
start_state =  f.readline().strip()
finite_states = f.readline().split()
NFA_transmissions = {}
for x in all_states :
    NFA_transmissions[x] = {}






#read each transmision from text file and save it into NFA_transmissions dictionary 
while(True):
    trans = f.readline()
    if not trans:
        break
    trans = trans.split()
    if trans[1]  in  NFA_transmissions[trans[0]].keys():
        NFA_transmissions[trans[0]][trans[1]].append(trans[2])
    else:      
        NFA_transmissions[trans[0]][trans[1]] = [trans[2]]
f.close()
# print(NFA_transmissions)    



# create dfa state and dfa transmisions 

# we save each dfa state as a set
DFA_states = [[start_state]]
DFA_transmissions = {start_state:{}}
DFA_finite_states =[] 

counter = 0
while(counter < len(DFA_states) ):
    present_state = DFA_states[counter]
    counter +=1
    for x in alphabet:
        #we use set to prevent repeatitive eleman or state in our dfa states
        dfa_state=set()
        for nfa_state in present_state:
            dfa_state |=set(NFA_transmissions[nfa_state][x])

        if dfa_state not in DFA_states :
            DFA_states.append(dfa_state)

        if ''.join(present_state) not in DFA_transmissions.keys():
            DFA_transmissions[''.join(present_state)]={}
        DFA_transmissions[''.join(present_state)][x] = "".join(dfa_state)      
# print(DFA_transmissions)    




# check each dfa state if each of them contains a nfa finite state we add it to DFA_finite_states list
DFA_states = DFA_transmissions.keys()
for x in DFA_states :
    for y in finite_states:
        if y in x:
            DFA_finite_states.append(x)
            break 




# write data into text file in standard format

fw = open("created_DFA.txt","w")
fw.write(" ".join(alphabet)+"\n")
fw.write(" ".join(DFA_states)+"\n")
fw.write(start_state+"\n")
fw.write(" ".join(DFA_finite_states)+"\n")

for x in DFA_transmissions.keys() :
    for y in alphabet :
        fw.write(x+" ")
        fw.write(y+" ")
        fw.write(DFA_transmissions[x][y])
        fw.write("\n")
fw.close()

print
print("\n \n"+"your files created here  ==> " + os.getcwd() + "\n")