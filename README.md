# theory of machines and languages 

## check strings by DFA 
   this script read DFA information from a text file in specefic format like below and create DFA for checking strings.
   
   a b     :    alphabet  <br />
   Q0 Q1 Q2 :   states <br />
   Q0    :      start state <br />
   Q1     :     accept state <br />
   Q0 a Q1 :    functions <br />
   Q0 b Q1 <br />
   Q1 a Q2 <br />
   Q1 b Q2 <br />
   Q2 a Q2 <br />
   Q2 b Q2 <br />

## convert NFA to DFA
   this script read NFA information from a text file like above , and convert epsilon NFA to NFA and write new NFA to
   a text file in root directory , then convert new NFA to DFA and write this DFA beside of our script.