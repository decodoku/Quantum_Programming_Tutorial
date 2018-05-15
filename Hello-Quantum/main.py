# -*- coding: utf-8 -*-

#    Created by James Wootton
#    Copyright © 2018 University of Basel. All rights reserved.

# import things we need
import math, copy

from Engine import *
from Levels import *

    
# clear screen and put title
ClearScreen ()
print("")
print("")
print("              ██╗  ██╗███████╗██╗     ██╗      ██████╗       ")              
print("              ██║  ██║██╔════╝██║     ██║     ██╔═══██╗    ")                
print("              ███████║█████╗  ██║     ██║     ██║   ██║     ")               
print("              ██╔══██║██╔══╝  ██║     ██║     ██║   ██║     ")               
print("              ██║  ██║███████╗███████╗███████╗╚██████╔╝      ")              
print("              ╚═╝  ╚═╝╚══════╝╚══════╝╚══════╝ ╚═════╝           ")          
print("                                                                   ") 
print("    ██████╗ ██╗   ██╗ █████╗ ███╗   ██╗████████╗██╗   ██╗███╗   ███╗")
print("   ██╔═══██╗██║   ██║██╔══██╗████╗  ██║╚══██╔══╝██║   ██║████╗ ████║")
print("   ██║   ██║██║   ██║███████║██╔██╗ ██║   ██║   ██║   ██║██╔████╔██║")
print("   ██║▄▄ ██║██║   ██║██╔══██║██║╚██╗██║   ██║   ██║   ██║██║╚██╔╝██║")
print("   ╚██████╔╝╚██████╔╝██║  ██║██║ ╚████║   ██║   ╚██████╔╝██║ ╚═╝ ██║")
print("    ╚══▀▀═╝  ╚═════╝ ╚═╝  ╚═╝╚═╝  ╚═══╝   ╚═╝    ╚═════╝ ╚═╝     ╚═╝")
print("\n")
print("\n")
print("             A GAMIFIED TUTORIAL FOR QUANTUM PROGRAMMING")
print("                               ")
print("                     For more information visit:")
print("           github.com/decodoku/Quantum_Programming_Tutorial")
print("\n")
print("\n")
print("\n")
print("\n")
print("\n")
print("\n")
input("> Note: For the best experience, you may need to zoom out\n> Press Enter to continue...\n")
ClearScreen()
print("  Choose which mode you want to play from the following list")
print("")
print("  1 - Main Tutorial\n      A gamified tutorial for programming quantum computers.\n")
print("  2 - Qubit Swapper\n      A few puzzles dedicated to the task of swapping qubits\n")
print("  3 - Sandbox\n      A chance to do what you want with two qubits.\n")
print("  4 - Image Superposer\n      Write a quantum program to create superpositions of images.\n")
choosing = True
while choosing:
    mode = input("> Input a number to select a mode...\n")
    if mode in ["1","2","3","4"]:
        choosing = False
    else:
        input("> That's not a valid mode. Press Enter to try again...\n")

if mode in ["1","2"]:
    if mode=="1":
            state_list, success_condition_list, qubits_used_list, allowed_gates_list, level_num, intro, outro = GetLevelStory()
    elif mode=="2":
            state_list, success_condition_list, qubits_used_list, allowed_gates_list, level_num, intro, outro = GetLevelSwaps()
    choosing = True
    while choosing:
        level = input("\n> Select a level (from 1 to "+str(level_num)+")...\n")
        if level.isdigit():
            level = int(level)
            if level in range(1,level_num+1):
                level = int(level)-1
                choosing = False
            else:
                input("> That level does not exist. Press Enter to try again...\n")
        else:
            level = 0
            choosing = False
            input("> That was not a valid level, so we'll start from the beginning...\n")
elif mode=="3":
    state_list, success_condition_list, qubits_used_list, allowed_gates_list, level_num, intro, outro = GetLevelSandbox()
    level = 0
elif mode=="4":

    allowed_filenames = ["0000","0001","0010","0011", "0100","0101","0110","0111", "1000","1001","1010","1011", "1100","1101","1110","1111"]

    input("\n> This mode relates to a Jupyter notebook, which you'll find at github.com/decodoku/Quantum_Programming_Tutorial/tree/master/image-superposer...\n")
    input("\n> There you'll find 16 images, all with a bit string as their filename...\n")
    choosing = True
    while choosing :
        string1 = input("\n> Choose one of these images by typing the filename below...\n")
        if string1 in allowed_filenames:
            choosing = False
        else:
            input("> That was not a valid filename. Press Enter to try again...\n")
    choosing = True
    while choosing :
        string2 = input("\n> Choose another image typing the filename below...\n")
        if string2 in allowed_filenames and string2!=string1:
            choosing = False
        else:
            input("> That was not a valid filename. Press Enter to try again...\n")
    input("\n> You'll now write a QISKit program to superpose these two images...\n")
    input("\n> This can then be run on a real machine using the Jupyter notebook...\n")

    state_list, success_condition_list, qubits_used_list, allowed_gates_list, level_num, intro, outro = GetLevelSuperposer(string1,string2)
    level = 0

else:
    print("> Oops! You shouldn't have been allowed to pick this mode. Restart the program and try again...")


while (level<level_num) :
        
    # specifications for this level
    state = copy.deepcopy(state_list[level])
    allowed_gates = copy.deepcopy(allowed_gates_list[level])
    required_gates = copy.deepcopy(allowed_gates)
    qubits_used = copy.deepcopy(qubits_used_list[level])
    success_condition = copy.deepcopy(success_condition_list[level])

    bloch = False # always start a level with Bloch off
    active_qubit = -1 # and no active qubit
    program = [] # and an empty program

    # every puzzle is thought of as one involving two qubits, even if only one of those qubits is involved
    # qubits_used should therefore always be a list of two qubits, the first is the one displayed on the top, and the second is the one on the bottom

    if allowed_gates[qubits_used[0]]=={} : # if no gates are allowed for the qubit on top, we know to only show the qubit on the side
            shown_qubit = 1
    elif allowed_gates[qubits_used[1]]=={} : # and vice versa
            shown_qubit = 0
    else :
            shown_qubit = 2

    success = False
    restart = False
        
    ClearScreen ()
    print("\nLevel "+str(level+1)+"\n")
    for line in intro[level] :
        input("> " + line + "...")

    while success==False and restart==False :

        # ask player to choose an operation
        combined_gates = []
        for qubit in [qubits_used[0],qubits_used[1],"both"]:
            for gate in allowed_gates[qubit].keys() :
                if allowed_gates[qubit][gate]==0 or required_gates[qubit][gate]>0:
                    if gate not in combined_gates:
                        combined_gates.append(gate)
        
        gate = ""
        while gate=="":
 
            message = "> Choose one of the allowed operations from the list above by typing its name below\n> Or type restart to start this puzzle over..."
            given_input = PrintScreen ( message, level, intro, program, state, shown_qubit, active_qubit, bloch, allowed_gates, required_gates )

            if given_input in combined_gates or given_input=='restart' :
                gate = given_input

        # ask player for a qubit to act on (if there is a choice)...
        qubit = ""
        if gate in ["cz","unbloch","restart"]: # for gates that act symmetrically the choice is irrelevant, and so set by default to both
            qubit = "both"
        elif shown_qubit==0 : # if only the top qubit is shown, that's what the gate acts on
            qubit = qubits_used[0]
        elif shown_qubit==1 : # if only the side qubit is shown, that's what the gate acts on
            qubit = qubits_used[1]
        elif gate not in allowed_gates[qubits_used[0]].keys(): # if the gate isn't an allowed one for the top qubit, it acts on the side
            qubit = qubits_used[1]
        elif gate not in allowed_gates[qubits_used[1]].keys(): # and vice-versa
            qubit = qubits_used[0]
        else :
            while qubit not in [qubits_used[0],qubits_used[1]]:
                message = "> Choose a qubit to act on:\n> Type in "+qubits_used[0]+" or "+qubits_used[1]+"..."
                qubit = PrintScreen ( message, level, intro, program, state, shown_qubit, active_qubit, bloch, allowed_gates, required_gates )


        # if it is a gate, apply it
        if gate in ["x","z","h","q","qdg","cz","cx"] :
            # the apply gate function adresses qubits as 0 and 1, so we convert back to this before applying
            if qubit==qubits_used[0] :
                qubit_pos = "0"
            elif qubit==qubits_used[1] :
                qubit_pos = "1"
            else :
                qubit_pos = "both"
            # now apply
            state = ApplyGate( state, gate, qubit_pos )
            # then we write the qiskit commands
            if gate=="cz" :
                program.append("program.cz( qubit["+qubits_used[0]+"], qubit["+qubits_used[1]+"] )")
            elif gate=="cx" :
                if qubit==qubits_used[0] :
                    program.append("program.cx( qubit["+qubits_used[1]+"], qubit["+qubits_used[0]+"] )")
                else :
                    program.append("program.cx( qubit["+qubits_used[0]+"], qubit["+qubits_used[1]+"] )")
            else :
                program.append("program."+gate+"( qubit["+qubit+"] )")

        # if it is a visualization command, apply it
        elif gate=="bloch" :
            bloch = True
            if qubit==qubits_used[0] :
                active_qubit = 0
            elif qubit==qubits_used[1] :
                active_qubit = 1
            elif gate=="unbloch" :
                bloch = false
                active_qubit = -1
        elif gate=="restart" :
            restart = True
        else :
            print("Error: Something's not quite right")


        # log the number of these gates if it is important
        if gate!="restart" :
            if allowed_gates[qubit][gate] > 0 :
                required_gates[qubit][gate] -= 1
                if required_gates[qubit][gate] < 0 :
                    input("> You have used this gate too many times, so the level will restart...\n")
                    restart = True

                
        # see if success conditions are met
        success = True
        # the final state has to be right
        for box, expect in success_condition.items() :
            success =    success and state[box]==expect
        # and the number of ops has to be right
        for qubit in required_gates.keys() :
            for gate in required_gates[qubit].keys() :
                if (required_gates[qubit][gate] > 0) :
                    success = False

        
    if restart==False :
        
        message = "\n> Target achieved.\n\n\n> Press Enter to continue..."
        given_input = PrintScreen ( message, level, intro, program, state, shown_qubit, active_qubit, bloch, {}, required_gates )
                
        # print the outro
        for line in outro[level] :
            input("> " + line + "...")
                
        # interate the level
        level += 1


if mode in ["1","2"] :
    input("> That's all the levels we have for now. Restart the program, or continue your QISKit journey at QISKit.org\n")
elif mode=="3" :
    input("> How are you seeing this?!?!?!?!?!?!?!\n")
elif mode=="4" :
    input("> Now you have your QISKit program. You just need to run the notebook for your image.\n")




    
    
    
    
    
    
    
    
    
    
    
    
    
    
    