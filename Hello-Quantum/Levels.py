# -*- coding: utf-8 -*-

#    Created by James Wootton
#    Copyright © 2018 University of Basel. All rights reserved.

from Engine import *

# Story Mode
def GetLevelStory ( ) :

    state_list = []
    success_condition_list = []
    qubits_used_list = []
    allowed_gates_list = []
    intro = []
    outro = []
    
    #1
    state_list.append( {"XI":0.0, "ZI":-1.0,
                                            "XX":0.0,"XZ":0.0,"ZX":0.0,"ZZ":0.0,"YY":0.0,
                                            "IX":0.0, "IZ":0.0} )
    success_condition_list.append( {"ZI":1.0} )
    qubits_used_list.append( [ "0", "1" ] )
    allowed_gates_list.append( { "0":{"x":3}, "1":{}, "both":{} } )

    intro.append( ["In these puzzles, you'll see a grid and be given a task",
                                 "Your job is to complete that task by using quantum programming",
                                 "Your first job concerns a single qubit, which we call qubit 0",
                                 "The state of this is visualized on the grid using two coloured boxes",
                                 "Each is either on, off, or something in between",
                                 "In the first puzzle, your job is to turn the blue box off using the command known as x",
                                 "One x should be enough but, to make sure it's working properly, do it three times instead",
                                 "TARGET: Turn off the blue box, and use the x command 3 times"] )
    outro.append( ["Great!",
                                 "The x command turns the blue box on and off, and does nothing to the red box"] )
    
    #2
    state_list.append( {"XI":0.0, "ZI":0.0,
                                            "XX":0.0,"XZ":0.0,"ZX":0.0,"ZZ":0.0,"YY":0.0,
                                            "IX":0.0, "IZ":-1.0} )
    success_condition_list.append( {"IZ":1.0} )
    qubits_used_list.append( [ "0", "1" ] )
    allowed_gates_list.append( { "0":{}, "1":{"x":3}, "both":{} } )

    intro.append( ["Now we'll look at another qubit, called qubit 1",
                                 "It's also described by two boxes. But because it's a different qubit, they are in a different place",
                                 "To reset it, and to test out the x, do the same as before",
                                 "TARGET: Turn off the blue box, and use the x command 3 times"] )
    outro.append( ["Great!",
                                 "Now you've gotten the hang of x, you won't need to repeat it 3 times any more."] )
    
    #3
    state_list.append( {"XI":0.0, "ZI":-1.0,
                                            "XX":0.0,"XZ":0.0,"ZX":0.0,"ZZ":0.0,"YY":0.0,
                                            "IX":0.0, "IZ":0.0} )
    success_condition_list.append( {"ZI":1.0} )
    qubits_used_list.append( [ "0", "1" ] )
    allowed_gates_list.append( { "0":{"x":0}, "1":{}, "both":{} } )

    intro.append( ["Now we move on to another chip, with another qubit 0. But what is a qubit?",
                                 "A qubit is a quantum object that can be turned into a bit",
                                 "There are many ways we can do this, and the result we get depends on the method we use",
                                 "Our favourite way to extract the bit is to use the blue box",
                                 "If it's 'off', we get 0. If it's 'on' we get 1",
                                 "TARGET: Turn off the blue box"] )
    outro.append( ["Great!","Now for the next qubit"] )
    
    #4
    state_list.append( {"XI":0.0, "ZI":0.0,
                                            "XX":0.0,"XZ":0.0,"ZX":0.0,"ZZ":0.0,"YY":0.0,
                                            "IX":0.0, "IZ":-1.0} )
    success_condition_list.append( {"IZ":1.0} )
    qubits_used_list.append( [ "0", "1" ] )
    allowed_gates_list.append( { "0":{}, "1":{"x":0}, "both":{} } )

    intro.append( ["Looks like this will just be another blue box to turn off",
                                 "TARGET: Turn off the blue box"] )
    outro.append( ["Great!","Now on to the next chip"] )
    
    #5
    state_list.append( {"XI":1.0, "ZI":0.0,
                                            "XX":0.0,"XZ":0.0,"ZX":0.0,"ZZ":0.0,"YY":0.0,
                                            "IX":0.0, "IZ":0.0} )
    success_condition_list.append( {"ZI":1.0} )
    qubits_used_list.append( [ "0", "1" ] )
    allowed_gates_list.append( { "0":{"x":0,"h":3}, "1":{}, "both":{} } )

    intro.append( ["This chip has a new operation enabled, called h",
                                 "It swaps the contents of the two boxes",
                                 "To test it out, do the old trick of repeating three times",
                                 "TARGET: Turn off the blue box, and use the h command 3 times"] )
    outro.append( ["Great!",
                                 "Now for the next qubit"] )
    
    #6
    state_list.append( {"XI":0.0, "ZI":0.0,
                                            "XX":0.0,"XZ":0.0,"ZX":0.0,"ZZ":0.0,"YY":0.0,
                                            "IX":1.0, "IZ":0.0} )
    success_condition_list.append( {"IZ":1.0} )
    qubits_used_list.append( [ "0", "1" ] )
    allowed_gates_list.append( { "0":{}, "1":{"x":3,"h":0}, "both":{} } )

    intro.append( ["Have you noticed that x has no effect when the blue box is only half on?",
                                 "It inverts what the box is doing: off becomes on, on becomes off, but half remains half",
                                 "TARGET: Turn off the blue box, and use the x command 3 times"] )
    outro.append( ["Great!",
                                 "By the way, extracting an output from a box that's half on would give a random result"] )
    
    #7
    state_list.append( {"XI":0.0, "ZI":-1.0,
                                            "XX":0.0,"XZ":0.0,"ZX":0.0,"ZZ":0.0,"YY":0.0,
                                            "IX":0.0, "IZ":0.0} )
    success_condition_list.append( {"ZI":1.0} )
    qubits_used_list.append( [ "0", "1" ] )
    allowed_gates_list.append( { "0":{"z":0,"h":0}, "1":{}, "both":{} } )

    intro.append( ["The x operation isn't working on this chip",
                                 "But you will have a new operation, called z, which inverts the red box instead",
                                 "You'll need work out how to reset the qubits with z and h",
                                 "TARGET: Turn off the blue box without using the x command"] )
    outro.append( ["Great!","Now for the next qubit"] )

    #8
    state_list.append( {"XI":0.0, "ZI":0.0,
                                            "XX":0.0,"XZ":0.0,"ZX":0.0,"ZZ":0.0,"YY":0.0,
                                            "IX":1.0, "IZ":0.0} )
    success_condition_list.append( {"IZ":1.0} )
    qubits_used_list.append( [ "0", "1" ] )
    allowed_gates_list.append( { "0":{}, "1":{"z":0,"h":0}, "both":{} } )

    intro.append( ["The red boxes represent another way to get a bit out of a qubit",
                                 "Again, 'off' gives you a 0 and 'on' gives you a 1."
                                 "The red box can only be certain of the result it would give when the blue box is completely random",
                                 "Qubits only have a limited amount of certainty to go round",
                                 "The h command swaps the results you'd get for blue and red",
                                 "TARGET: Move the off to blue and the randomness to red"] )
    outro.append( ["Great!","Now on to the next chip"] )
    
    #9
    state_list.append( {"XI":0.0, "ZI":-1.0,
                                            "XX":0.0,"XZ":0.0,"ZX":1.0,"ZZ":0.0,"YY":0.0,
                                            "IX":-1.0, "IZ":0.0} )
    success_condition_list.append( {"ZI":1.0,"IZ":1.0} )
    qubits_used_list.append( [ "0", "1" ] )
    allowed_gates_list.append( { "0":{"x":0,"z":0,"h":0}, "1":{"x":0,"z":0,"h":0}, "both":{} } )

    intro.append( ["Now you know the basic tools, you can tackle both qubits at once",
                                 "You'll see the four boxes you are used to, which represent the two qubits",
                                 "There will be some extra ones too, but don't worry about these for now",
                                 "TARGET: Turn off the blue boxes"] )
    outro.append( ["Great!","Now on to the next chip"] )
    
    #10
    state_list.append( {"XI":-1.0, "ZI":0.0,
                                            "XX":0.0,"XZ":1.0,"ZX":0.0,"ZZ":0.0,"YY":0.0,
                                            "IX":0.0, "IZ":-1.0} )
    success_condition_list.append( {"ZI":1.0,"IZ":1.0} )
    qubits_used_list.append( [ "0", "1" ] )
    allowed_gates_list.append( { "0":{"z":0,"h":0}, "1":{"z":0,"h":0}, "both":{} } )

    intro.append( ["Another chip with the x turned off",
                                 "So another chance to practice your workarounds",
                                 "TARGET: Turn off the blue boxes without using the x command"] )
    outro.append( ["Great!","Now on to the next chip"] )

    #11
    state_list.append( {"XI":0.0, "ZI":-1.0,
                                            "XX":0.0,"XZ":0.0,"ZX":0.0,"ZZ":1.0,"YY":0.0,
                                            "IX":0.0, "IZ":-1.0} )
    success_condition_list.append( {"ZI":1.0,"IZ":1.0} )
    qubits_used_list.append( [ "0", "1" ] )
    allowed_gates_list.append( { "0":{"x":0,"z":0,"h":0}, "1":{"x":0,"z":0,"h":0}, "both":{} } )

    intro.append( ["In case you are wondering about the extra boxes, they tell us about the relationship between the two qubits",
                                 "The blue one, for example, keeps track of how likely the two blue outputs are to agree",
                                 "It is off when the blue ouptuts of the two qubits will definitely agree, and on when they'll definitely disagree",
                                 "Keep an eye on how it changes on this chip",
                                 "TARGET: Turn off the blue boxes"] )
    outro.append( ["Great!",
                                 "The extra red box similarly looks for agreements of the red boxes",
                                 "The two purple ones are for the blue output of one qubit, and the red one of the other"] )
    
    #12
    state_list.append( {"XI":0.0, "ZI":-1.0,
                                            "XX":0.0,"XZ":0.0,"ZX":1.0,"ZZ":0.0,"YY":0.0,
                                            "IX":-1.0, "IZ":0.0} )
    success_condition_list.append( {"ZI":1.0,"IZ":1.0} )
    qubits_used_list.append( [ "0", "1" ] )
    allowed_gates_list.append( { "0":{"x":0,"z":0,"h":0}, "1":{"x":0,"z":0,"h":0}, "both":{} } )

    intro.append( ["The x doesn't just invert the blue box of qubit 0, but all the boxes in that column",
                                 "TARGET: Turn off the blue boxes"] )
    outro.append( ["Great!","Now on to the next chip"] )
    
    #13
    state_list.append( {"XI":-1.0, "ZI":0.0,
                                            "XX":0.0,"XZ":1.0,"ZX":0.0,"ZZ":0.0,"YY":0.0,
                                            "IX":0.0, "IZ":-1.0} )
    success_condition_list.append( {"ZI":1.0,"IZ":1.0} )
    qubits_used_list.append( [ "0", "1" ] )
    allowed_gates_list.append( { "0":{"z":0,"h":0}, "1":{"z":0,"h":0}, "both":{} } )

    intro.append( ["The z for qubit 0 similarly affects all the boxes of the other column",
                                 "TARGET: Turn off the blue boxes without using the x command"] )
    outro.append( ["Great!","Now on to the next chip"] )

    #14
    state_list.append( {"XI":-1.0, "ZI":0.0,
                                            "XX":0.0,"XZ":1.0,"ZX":0.0,"ZZ":0.0,"YY":0.0,
                                            "IX":0.0, "IZ":-1.0} )
    success_condition_list.append( {"ZI":1.0,"IZ":1.0} )
    qubits_used_list.append( [ "0", "1" ] )
    allowed_gates_list.append( { "0":{"z":0,"h":0}, "1":{"z":0,"h":0}, "both":{} } )

    intro.append( ["The h for qubit 0 swaps the two columns",
                                 "TARGET: Turn off the blue boxes without using the x command"] )
    outro.append( ["Great!","Now on to the next chip"] )

    #15
    state_list.append( {"XI":1.0, "ZI":-1.0,
                                            "XX":1.0,"XZ":0.0,"ZX":1.0,"ZZ":0.0,"YY":0.0,
                                            "IX":-1.0, "IZ":0.0} )
    success_condition_list.append( {"ZI":1.0,"IZ":1.0} )
    qubits_used_list.append( [ "0", "1" ] )
    allowed_gates_list.append( { "0":{"x":0,"z":0,"h":0}, "1":{"x":0,"z":0,"h":0}, "both":{} } )

    intro.append( ["The operations for qubit 1 have similar effects, but on the rows instead of the columns",
                                 "The x affects one row, z affects the other, and h swaps them",
                                 "TARGET: Turn off the blue boxes"] )
    outro.append( ["Great!","Now on to the next chip"] )

    #16
    state_list.append( {"XI":-1.0, "ZI":0.0,
                                            "XX":1.0,"XZ":0.0,"ZX":0.0,"ZZ":0.0,"YY":0.0,
                                            "IX":-1.0, "IZ":0.0} )
    success_condition_list.append( {"ZI":1.0,"IZ":1.0} )
    qubits_used_list.append( [ "0", "1" ] )
    allowed_gates_list.append( { "0":{"x":0,"z":0,"h":0}, "1":{"x":0,"z":0,"h":0}, "both":{} } )

    intro.append( ["This is a nice chip with everything working. So just do your magic!",
                                 "TARGET: Turn off the blue boxes"] )
    outro.append( ["Great!","Now on to the next chip",
                                 "Have you noticed the program that is getting displayed as you work",
                                 "This is the code you are writing for the quantum computer, using the QISKit SDK",
                                 "Check out qiskit.org for more information"] )
    
    #17
    state_list.append( {"XI":1.0, "ZI":-1.0,
                                            "XX":1.0,"XZ":0.0,"ZX":1.0,"ZZ":0.0,"YY":0.0,
                                            "IX":-1.0, "IZ":0.0} )
    success_condition_list.append( {"ZI":1.0,"IZ":1.0} )
    qubits_used_list.append( [ "0", "1" ] )
    allowed_gates_list.append( { "0":{"x":0,"z":0,"h":0}, "1":{"x":0,"z":0,"h":0}, "both":{} } )

    intro.append( ["Another well behaved chip",
                                 "By the way, most of IBM's chips have more than just two qubits",
                                 "In fact, you can use a real device with 16 qubits from the comfort of your own home"
                                 "TARGET: Turn off the blue boxes"] )
    outro.append( ["Great!","Now on to the next chip"] )

    #18
    state_list.append( {"XI":0.0, "ZI":0.0,
                                            "XX":0.0,"XZ":1.0,"ZX":1.0,"ZZ":0.0,"YY":1.0,
                                            "IX":0.0, "IZ":0.0} )
    success_condition_list.append( {"ZI":1.0,"IZ":1.0} )
    qubits_used_list.append( [ "0", "1" ] )
    allowed_gates_list.append( { "0":{"x":0,"z":0,"h":0}, "1":{"x":0,"z":0,"h":0}, "both":{"cz":0} } )

    intro.append( ["This chip has a new operation enabled: cz",
                                 "Like h, we can think of this as swapping the contents of boxes",
                                 "It swaps the contents of the red box of each qubit with the purple box next to it",
                                 "These swaps let us make big changes to the way the qubits are correlated with each other",
                                 "For this reason, cz is known as an entangling operation",
                                 "You'll probably need to use it to disentangle the qubits here",
                                 "TARGET: Turn off the blue boxes"] )
    outro.append( ["Great!",
                                 "This box swapping interpretation is just one way to understand the cz",
                                 "On the next chip, you'll need to use another"] )

    #19
    state_list.append( {"XI":0.0, "ZI":1.0,
                                            "XX":0.0,"XZ":0.0,"ZX":-1.0,"ZZ":0.0,"YY":0.0,
                                            "IX":-1.0, "IZ":0.0} )
    success_condition_list.append( {"ZI":1.0,"IZ":1.0} )
    qubits_used_list.append( [ "0", "1" ] )
    allowed_gates_list.append( { "0":{"x":0,"h":0}, "1":{"h":0}, "both":{"cz":0} } )

    intro.append( ["The cz can also be thought of as a conditional operation",
                                 "If the blue box for qubit 0 is off, the cz does nothing",
                                 "But if it is on, the cz does a z on qubit 1",
                                 "Since the normal z is not working for on this chip, and x only works for qubit 0, this feature of the cz should come in handy",
                                 "TARGET: Turn off the blue boxes using the allowed gates"] )
    outro.append( ["Great!","Now on to the next chip"] )
    
    #20
    state_list.append( {"XI":0.0, "ZI":0.0,
                                            "XX":1.0,"XZ":0.0,"ZX":0.0,"ZZ":1.0,"YY":-1.0,
                                            "IX":0.0, "IZ":0.0} )
    success_condition_list.append( {"ZI":1.0,"IZ":1.0} )
    qubits_used_list.append( [ "0", "1" ] )
    allowed_gates_list.append( { "0":{"x":0,"z":0,"h":0}, "1":{"x":0,"z":0,"h":0}, "both":{"cz":0} } )

    intro.append( ["This chip is in an entangled state. The qubits are correlated in a way that only quantum objects can be",
                                 "Though outputs coming from both qubits will be completely random, and have not yet decided what to randomly be, they are certain to always agree",
                                 "What does this mean for the cz? If the blue boxes are full of undecided randomness, does a z get applied to qubit 1 or not?",
                                 "For the time being, you are probably better off with the box swapping interpretation when stuff like this is going on",
                                 "TARGET: Turn off the blue boxes"] )
    outro.append( ["Great!",
                                 "Now on to the next chip, and another interpretation of the cz"] )
    
    #21
    state_list.append( {"XI":-1.0, "ZI":0.0,
                                            "XX":0.0,"XZ":-1.0,"ZX":0.0,"ZZ":0.0,"YY":0.0,
                                            "IX":0.0, "IZ":1.0} )
    success_condition_list.append( {"ZI":1.0,"IZ":1.0} )
    qubits_used_list.append( [ "0", "1" ] )
    allowed_gates_list.append( { "0":{"h":0},"1":{"x":0,"h":0}, "both":{"cz":0} } )

    intro.append( ["You have used cz to do something to qubit 1 that was condition on qubit 0",
                                 "Sometimes you might want an operation that works the other way",
                                 "It turns out that cz does this too! The exact same operation can be interpreted in the opposite way",
                                 "Which is handy, since it is qubit 0 for which x and z aren't working for this chip",
                                 "TARGET: Turn off the blue boxes using the allowed gates"] )
    outro.append( ["Great! The fact that all three of these interpretations of cz are true at once is quite an interesting feature",
                                 "There are those who like to reflect upon the mystery of how this works",
                                 "But they aren't tiny, and stuck in a fancy fridge and trying to do a job that they can't even remember",
                                 "So you'd better save your reflections for later. On to the next chip!"] )

    #22
    state_list.append( {"XI":0.0, "ZI":1.0,
                                            "XX":0.0,"XZ":0.0,"ZX":0.0,"ZZ":-1.0,"YY":0.0,
                                            "IX":0.0, "IZ":-1.0} )
    success_condition_list.append( {"IZ":1.0,"ZI":1.0} )
    qubits_used_list.append( [ "0", "1" ] )
    allowed_gates_list.append( { "0":{"x":0,"z":0,"h":0}, "1":{"h":0}, "both":{"cz":0} } )

    intro.append( ["Combining the cz with other operations, we can get new kinds of conditional behaviour",
                                 "For example, what if we wanted a conditional x rather than a conditional z",
                                 "Using your expertise with using a z to make an x, you should be able to work it out",
                                 "TARGET: Turn off the blue boxes using the allowed gates"] )
    outro.append( ["Great!",
                                 "You made an operation that does an x on qubit 1, depending on whether the blue box of qubit 0 is on",
                                 "We call this the cx operation, or the cnot"] )

    #23
    state_list.append( {"XI":0.0, "ZI":-1.0,
                                            "XX":0.0,"XZ":0.0,"ZX":0.0,"ZZ":-1.0,"YY":0.0,
                                            "IX":0.0, "IZ":1.0} )
    success_condition_list.append( {"IZ":1.0,"ZI":1.0} )
    qubits_used_list.append( [ "0", "1" ] )
    allowed_gates_list.append( { "0":{"h":0}, "1":{"x":0,"z":0,"h":0}, "both":{"cz":0} } )

    intro.append( ["Unlike cz, the cx operation is not symmetric",
                                 "To make it conditional on qubit 1 instead, you'll need to apply h elsewhere",
                                 "TARGET: Turn off the blue boxes using the allowed gates"] )
    outro.append( ["Great!","Now on to the next chip"] )

    #24
    state_list.append( {"XI":0.0, "ZI":1.0,
                                            "XX":0.0,"XZ":0.0,"ZX":0.0,"ZZ":-1.0,"YY":0.0,
                                            "IX":0.0, "IZ":-1.0} )
    success_condition_list.append( {"IZ":1.0,"ZI":1.0} )
    qubits_used_list.append( [ "0", "1" ] )
    allowed_gates_list.append( { "0":{"x":0,"z":0,"h":0}, "1":{"h":0,"cx":0}, "both":{} } )

    intro.append( ["Most IBM quantum devices actually use cx as the basic entangling operation instead of cz",
                                 "Which means you have to worry about which way round you are allowed to apply them",
                                 "This chip is one of those devices",
                                 "You have a cx that is conditional on the blue box of qubit 0, and which can apply an x to qubit 1",
                                 "Though it affects both qubits, you'll find it in your list of allowed operations for qubit 1",
                                 "TARGET: Turn off the blue boxes using the allowed gates"] )
    outro.append( ["Great!","Now on to the next chip"] )

    #25
    state_list.append( {"XI":-1.0, "ZI":0.0,
                                            "XX":-1.0,"XZ":0.0,"ZX":0.0,"ZZ":0.0,"YY":0.0,
                                            "IX":1.0, "IZ":0.0} )
    success_condition_list.append( {"IZ":1.0,"ZI":1.0} )
    qubits_used_list.append( [ "0", "1" ] )
    allowed_gates_list.append( { "0":{"h":0}, "1":{"h":0,"z":0,"cx":0}, "both":{} } )

    intro.append( ["Like the cz, there are different ways to interpret the cx",
                                 "In the last chip we used the fact that it does an x to qubit 1 conditional on the blue box of qubit 0",
                                 "But it can also be interpreted as doing a z to qubit 0, conditional on the red box of qubit 1",
                                 "This is the interpretation you'll need to reset this chip",
                                 "But since everyone is so obsessed with the other interpretation, you'll still find it in your list of allowed qubit 1 operations",
                                 "TARGET: Turn off the blue boxes using the allowed gates"] )
    outro.append( ["Great!","Now on to the next chip"] )

    #26
    state_list.append( {"XI":0.0, "ZI":-1.0,
                                            "XX":0.0,"XZ":0.0,"ZX":0.0,"ZZ":1.0,"YY":0.0,
                                            "IX":0.0, "IZ":-1.0} )
    success_condition_list.append( {"IZ":1.0,"ZI":1.0} )
    qubits_used_list.append( [ "0", "1" ] )
    allowed_gates_list.append( { "0":{"h":0,"x":0,"cx":0}, "1":{"h":0}, "both":{} } )

    intro.append( ["The cx on this chip is the other way around: It does an x to qubit 0 conditional on the blue box of qubit 1",
                                 "Unfortunately, one that does the x to qubit 1 is what you need to reset this chip",
                                 "But don't worry. With a few h operations you can turn the cx around",
                                 "TARGET: Turn off the blue boxes using the allowed gates"] )
    outro.append( ["Great!",
                                 "With an h on both qubits before and after a cx, it effectively works the other way around",
                                 "If you remember anything from your time here, it should be this",
                                 "It is a very useful trick when using IBM's cx based devices",
                                 "Now on to the next chip"] )

    #27
    state_list.append( MakeState( {"XI":0, "ZI":1,"XX":0.0,"XZ":0.0,"ZX":0.0,"ZZ":1.0,"YY":0.0,"IX":0.0, "IZ":1.0}, [["qdg","0"],["qdg","0"],["qdg","0"]]) )
    success_condition_list.append( {"ZI":1.0} )
    qubits_used_list.append( [ "0", "1" ] )
    allowed_gates_list.append( { "0":{"bloch":1,"q":0}, "1":{}, "both":{"unbloch":0} } )

    intro.append( ["This chip is used to test an operation called u3(math.pi,0,0)",
                                 "But that's a lot to type, so we'll call it q instead",
                                 "To introduce the q gate, we'll go back to doing the qubits one-by-one",
                                 "The q operation makes most sense when the qubits boxes are drawn on top of each other",
                                 "To do this, use the bloch command",
                                 "TARGET: Use the bloch command on qubit 0, and turn off the blue boxes using the q gate"] )
    outro.append( ["Great!", "On to the next qubit"] )

    #28
    state_list.append( MakeState( {"XI":0, "ZI":1,"XX":0.0,"XZ":0.0,"ZX":0.0,"ZZ":1.0,"YY":0.0,"IX":0.0, "IZ":1.0}, [["qdg","1"],["qdg","1"],["qdg","1"]]) )
    success_condition_list.append( {"IZ":1.0} )
    qubits_used_list.append( [ "0", "1" ] )
    allowed_gates_list.append( { "0":{}, "1":{"bloch":1,"q":0}, "both":{"unbloch":0} } )

    intro.append( ["So what does this q thing do?",
                                 "Around the boxes, are a circle",
                                 "In this circle, at the point where the levels of the boxes meet, is a *",
                                 "The job of the q operation is to rotate that point, dragging the levels of the boxes with it",
                                 "One q rotates the point 1/8 of the way around the circle in the clockwise direction",
                                 "TARGET: Use the bloch command on qubit 1, and turn off the blue boxes using the q gate"] )
    outro.append( ["Great!", "On to the next qubit"] )

    #29
    state_list.append( MakeState( {"XI":0, "ZI":1,"XX":0.0,"XZ":0.0,"ZX":0.0,"ZZ":1.0,"YY":0.0,"IX":0.0, "IZ":1.0},
                                                                    [["qdg","0"],["qdg","0"],["qdg","1"]]) )
    success_condition_list.append( {"IZ":1.0} )
    qubits_used_list.append( [ "0", "1" ] )
    allowed_gates_list.append( { "0":{"bloch":0,"q":0}, "1":{"bloch":0,"q":0}, "both":{"unbloch":0} } )

    intro.append( ["Now you can do both qubits at once",
                                 "Notice that q on qubit 0 affects the columns, just like other qubit 0 operations",
                                 "And q on qubit 1 affects the rows",
                                 "You don't need to use the bloch operations for the qubits to apply q",
                                 "But I'd advise that you do",
                                 "TARGET: Turn off the blue boxes using the q gate"] )
    outro.append( ["Great!", "On to the next chip"] )

    #30
    state_list.append( MakeState( {"XI":0, "ZI":1,"XX":0.0,"XZ":0.0,"ZX":0.0,"ZZ":1.0,"YY":0.0,"IX":0.0, "IZ":1.0},
                                                                    [["qdg","0"],["q","1"]]) )
    success_condition_list.append( {"IZ":1.0} )
    qubits_used_list.append( [ "0", "1" ] )
    allowed_gates_list.append( { "0":{"x":0,"z":0,"h":0,"bloch":0,"q":1}, "1":{"x":0,"z":0,"h":0,"bloch":0,"q":1}, "both":{"unbloch":0} } )

    intro.append( ["This chip will only let you do one q on each qubit",
                                 "So hopefully you won't need more than that",
                                 "If you do, you might be able to hack a solution using other operations",
                                 "TARGET: Turn off the blue boxes using only one q gate on each qubit"] )
    outro.append( ["Great!", "On to the next chip"] )

    #31
    state_list.append( MakeState( {"XI":0, "ZI":1,"XX":0.0,"XZ":0.0,"ZX":0.0,"ZZ":1.0,"YY":0.0,"IX":0.0, "IZ":1.0},
                                                                    [["q","0"],["q","0"],["q","1"]]) )
    success_condition_list.append( {"IZ":1.0} )
    qubits_used_list.append( [ "0", "1" ] )
    allowed_gates_list.append( { "0":{"x":0,"z":0,"h":0,"bloch":0,"q":0,"qdg":0}, "1":{"x":0,"z":0,"h":0,"bloch":0,"q":0,"qdg":0}, "both":{"unbloch":0} } )

    intro.append( ["A shortcut way of doing this hack is qdg",
                                 "This is simply a anti-clockwise version of q",
                                 "Or counter clockwise, if you prefer",
                                 "Or widdershins. Widdershins is a great word. Let's all use widdershins",
                                 "TARGET: Turn off the blue boxes using the allowed gates"] )
    outro.append( ["Great!", "On to the next chip"] )

    #32
    state_list.append( MakeState( {"XI":0, "ZI":1,"XX":0.0,"XZ":0.0,"ZX":0.0,"ZZ":1.0,"YY":0.0,"IX":0.0, "IZ":1.0},
                                                                    [["z","0"],["h","0"],["h","1"]]) )
    success_condition_list.append( {"IZ":1.0} )
    qubits_used_list.append( [ "0", "1" ] )
    allowed_gates_list.append( { "0":{"x":0,"z":0,"bloch":0,"q":0,"qdg":0}, "1":{"x":0,"z":0,"bloch":0,"q":0,"qdg":0}, "both":{"unbloch":0} } )

    intro.append( ["The h operation is not working on this chip",
                                 "Fortunately, you can build it using q or qdg",
                                 "Use them to remind this chip how h is supposed to be done",
                                 "TARGET: Turn off the blue boxes using the allowed gates"] )
    outro.append( ["Great!", "On to the next chip"] )
    
    #33
    state_list.append( MakeState( {"XI":0, "ZI":1,"XX":0.0,"XZ":0.0,"ZX":0.0,"ZZ":1.0,"YY":0.0,"IX":0.0, "IZ":1.0},
                                                                    [["h","1"]]) )
    success_condition_list.append( {"IZ":1.0} )
    qubits_used_list.append( [ "0", "1" ] )
    allowed_gates_list.append( { "0":{"x":0,"z":0,"h":0,"bloch":0,"q":0,"qdg":0}, "1":{"x":0,"z":0,"bloch":0,"q":1,"qdg":1}, "both":{"unbloch":0,"cz":0} } )

    intro.append( ["With q and qdg, we can make conditional operations that are more interesting than just cz and cx",
                                 "Like a one that does an h to one qubit, conditional on the other",
                                 "Qubit 1 on this chip has a bunch of broken gates",
                                 "So you may need to create one of these",
                                 "TARGET: Turn off the blue boxes using the allowed gates"] )
    outro.append( ["Great!",
                                 "You have successfully tested and reset a whole bunch of qubits",
                                 "To find out how to do more than just reset them, check out the other modes in this program"] )

    level_num = len(state_list)
        
    return state_list, success_condition_list, qubits_used_list, allowed_gates_list, level_num, intro, outro


# sandbox
def GetLevelSwaps () :

    state_list = []
    success_condition_list = []
    qubits_used_list = []
    allowed_gates_list = []
    intro = []
    outro = []

    
    # 1
    state_list.append( {"XI":0.5, "ZI":0.5,
                                            "XX":-0.5,"XZ":0.0,"ZX":0.0,"ZZ":-0.5,"YY":0.0,
                                            "IX":-0.5, "IZ":-0.5} )
    target, target_string = MakeTarget( state_list[-1], 'swap' )
    success_condition_list.append( target )
    qubits_used_list.append( [ "0", "1" ] )
    allowed_gates_list.append( { "0":{"h":0}, "1":{"h":0}, "both":{"cz":0} } )

    intro.append( ["In these puzzles, your job is to swap the states of two qubits",
                   "This can always be done with nothing more than h operations, and either cz or cx",
                   "TARGET: Everything from qubit 0 must be moved to the same place on qubit 1, and vice-versa",
                   "So given the initial state you'll get, the final state should look like this",
                   target_string,
                   "Once the actual puzzle grid comes, you'll have to scroll up to see this again"] )
    outro.append( ["Well done!","Now try another"] )

    # 2
    state_list.append( {"XI":0.5, "ZI":0.0,
                                            "XX":0.5,"XZ":0.5,"ZX":0.0,"ZZ":-0.5,"YY":0.5,
                                            "IX":0.0, "IZ":0.5} )
    target, target_string = MakeTarget( state_list[-1], 'swap' )
    success_condition_list.append( target )
    qubits_used_list.append( [ "0", "1" ] )
    allowed_gates_list.append( { "0":{"h":0}, "1":{"h":0}, "both":{"cz":0} } )

    intro.append( ["TARGET: Everything from qubit 0 must be moved to the same place on qubit 1, and vice-versa",
                   "So given the initial state you'll get, the final state should look like this",
                   target_string,
                   "Once the actual puzzle grid comes, you'll have to scroll up to see this again"] )
    outro.append( ["Well done!","Now try another"] )
        
    # 3
    state_list.append( {"XI":0.0, "ZI":0.5,
                                            "XX":-0.5,"XZ":0.0,"ZX":-0.5,"ZZ":0.5,"YY":0.5,
                                            "IX":-0.5, "IZ":0.0} )
    target, target_string = MakeTarget( state_list[-1], 'swap' )
    success_condition_list.append( target )
    qubits_used_list.append( [ "0", "1" ] )
    allowed_gates_list.append( { "0":{"h":0}, "1":{"h":0}, "both":{"cz":0} } )

    intro.append( ["TARGET: Everything from qubit 0 must be moved to the same place on qubit 1, and vice-versa",
                   "So given the initial state you'll get, the final state should look like this",
                   target_string,
                   "Once the actual puzzle grid comes, you'll have to scroll up to see this again"] )
    outro.append( ["Well done!","Now try another"] )
        
    # 4
    state_list.append( {"XI":0.0, "ZI":-0.5,
                                            "XX":0.0,"XZ":0.5,"ZX":0.5,"ZZ":-0.5,"YY":0.5,
                                            "IX":0.0, "IZ":0.5} )
    target, target_string = MakeTarget( state_list[-1], 'swap' )
    success_condition_list.append( target )
    qubits_used_list.append( [ "0", "1" ] )
    allowed_gates_list.append( { "0":{"h":0}, "1":{"h":0}, "both":{"cz":0} } )

    intro.append( ["TARGET: Everything from qubit 0 must be moved to the same place on qubit 1, and vice-versa",
                   "So given the initial state you'll get, the final state should look like this",
                   target_string,
                   "Once the actual puzzle grid comes, you'll have to scroll up to see this again"])
    outro.append( ["Well done!","Now try another"] )
        
    # 5
    state_list.append( {"XI":0.0, "ZI":0.5,
                                            "XX":0.0,"XZ":0.5,"ZX":-0.5,"ZZ":0.5,"YY":-0.5,
                                            "IX":0.0, "IZ":0.5} )
    target, target_string = MakeTarget( state_list[-1], 'swap' )
    success_condition_list.append( target )
    qubits_used_list.append( [ "0", "1" ] )
    allowed_gates_list.append( { "0":{"h":0}, "1":{"h":0}, "both":{"cz":0} } )

    intro.append( ["TARGET: Everything from qubit 0 must be moved to the same place on qubit 1, and vice-versa",
                   "So given the initial state you'll get, the final state should look like this",
                   target_string,
                   "Once the actual puzzle grid comes, you'll have to scroll up to see this again"] )
    outro.append( ["Well done!","Now try another"] )
        
    # 6
    state_list.append( {"XI":0.5, "ZI":0.0,
                                            "XX":-0.5,"XZ":-0.5,"ZX":-0.5,"ZZ":0.0,"YY":0.5,
                                            "IX":-0.5, "IZ":0.0} )
    target, target_string = MakeTarget( state_list[-1], 'swap' )
    success_condition_list.append( target )
    qubits_used_list.append( [ "0", "1" ] )
    allowed_gates_list.append( { "0":{"h":0}, "1":{"h":0}, "both":{"cz":0} } )

    intro.append( ["TARGET: Everything from qubit 0 must be moved to the same place on qubit 1, and vice-versa",
                   "So given the initial state you'll get, the final state should look like this",
                   target_string,
                   "Once the actual puzzle grid comes, you'll have to scroll up to see this again"] )
    outro.append( ["Well done!","Now try another"] ) 
        
    # 7
    state_list.append( {"XI":0.5, "ZI":0.0,
                                            "XX":0.5,"XZ":0.5,"ZX":-0.5,"ZZ":0.0,"YY":-0.5,
                                            "IX":0.5, "IZ":0.0} )
    target, target_string = MakeTarget( state_list[-1], 'swap' )
    success_condition_list.append( target )
    qubits_used_list.append( [ "0", "1" ] )
    allowed_gates_list.append( { "0":{"h":0}, "1":{"h":0}, "both":{"cz":0} } )

    intro.append( ["TARGET: Everything from qubit 0 must be moved to the same place on qubit 1, and vice-versa",
                   "So given the initial state you'll get, the final state should look like this",
                   target_string,
                   "Once the actual puzzle grid comes, you'll have to scroll up to see this again"] )
    outro.append( ["Well done!",
                                 "Your solution to each of these probably would have worked for all the others too",
                                 "If so, you suceeded in making a swap gate!"] ) 
        
    level_num = len(state_list)

    return state_list, success_condition_list, qubits_used_list, allowed_gates_list, level_num, intro, outro



# sandbox
def GetLevelSandbox () :

    state_list = []
    success_condition_list = []
    qubits_used_list = []
    allowed_gates_list = []
    intro = []
    outro = []

    
    state_list.append( {"XI":0.0, "ZI":1.0,
                                            "XX":0.0,"XZ":0.0,"ZX":0.0,"ZZ":1.0,"YY":0.0,
                                            "IX":0.0, "IZ":1.0} )
    success_condition_list.append( {"XI":1.0,"ZI":1.0} )
    qubits_used_list.append( [ "0", "1" ] )
    allowed_gates_list.append( { "0":{"x":0,"z":0,"h":0,"bloch":0,"q":0,"qdg":0,"cx":0}, "1":{"x":0,"z":0,"h":0,"bloch":0,"q":0,"qdg":0,"cx":0}, "both":{"unbloch":0,"cz":0} } )

    intro.append( ["This is a sandox. You have all gates available, and can do what you want",
                                 "The initial state is the one with ouput 00, which is the usual initial state for quantum computers",
                                 "There are no conditions for success. You can just keep playing as long as you like",
                                 "Bear in mind that ascii art isn't the most precise way of representing quantum states. So things might start looking strange for complex programs"] )
    outro.append( ["If you are seeing this, you somehow disproved Heisenberg's uncertainty principle",
                                 "Either that or there is a bug"] )


    level_num = len(state_list)

    return state_list, success_condition_list, qubits_used_list, allowed_gates_list, level_num, intro, outro


# image superposer
def    GetLevelSuperposer ( string1, string2 ) :

    state_list = []
    success_condition_list = []
    qubits_used_list = []
    allowed_gates_list = []
    intro = []
    outro = []

    definite = {"0":[],"1":[]}
    superpos = {"same":[],"diff":[]}
    first_super = -1
    for j in range(4) :

            if string1[j]==string2[j] :
                    definite[str(string1[j])].append( str(j) )
            else :
                    if first_super == -1 :
                            first_super = j
                            superpos["same"].append( str(j) )
                    else :
                            if string1[j]==string1[first_super] :
                                    superpos["same"].append( str(j) )
                            else :
                                    superpos["diff"].append( str(j) )


    # if a bit is 0 in both file names, nothing need be done

    # if a bit is 1 in both, this needs done
    for j in definite["1"] :

        state_list.append( {"XI":0.0, "ZI":1.0,
	                                "XX":0.0,"XZ":0.0,"ZX":-1.0,"ZZ":0.0,"YY":0.0,
	                                "IX":0.0, "IZ":1.0} )
        success_condition_list.append( {"IZ":-1.0,} )
        qubits_used_list.append( [ "a", "b[" + j + "]" ] )
        allowed_gates_list.append( { "a":{}, "b[" + j + "]":{"x":0,"z":0,"h":0}, "both":{} } )
        intro.append( ["Since bit "+j+" has the value 1 for both in both file names, the qubit named b["+j+"] should be given a full blue box"] )
        outro.append( ["Great!", "Copy the QISKit program into the notebook."] )


    if first_super != -1 :

        state_list.append( {"XI":0.0, "ZI":1.0,
	                                "XX":0.0,"XZ":0.0,"ZX":0.0,"ZZ":1.0,"YY":0.0,
	                                "IX":0.0, "IZ":1.0} )
        success_condition_list.append( {"XI":1.0} )
        qubits_used_list.append( [ "a", "b[0}" ] )
        allowed_gates_list.append( { "a":{"x":0,"z":0,"h":0}, "b[0}":{}, "both":{} } )
        intro.append( ["Since we are making a superposition of two things, so let's start with a superposition of 0 and 1 on a single qubit",
                                                 "We'll do it on qubit a, even though this won't actually be part of our final results",
                                                 "The superposition can be spread to the other qubits from here",
                                                 "Since we want a superposition of 0 and 1, we need a half full blue box",
                                                 "Let's go for the superposition for which the red box is empty"] )
        outro.append( ["Great!",
                                                 "Copy the QISKit program into the notebook. Do this with a right click, rather than ctrl-C"] )

    for j in superpos["same"] :

        if j==str(first_super) :
            state_list.append( {"XI":1.0, "ZI":0.0, "XX":0.0,"XZ":1.0,"ZX":0.0,"ZZ":0.0,"YY":0.0, "IX":0.0, "IZ":1.0} )
        else :
            state_list.append( {"XI":0.0, "ZI":0.0, "XX":0.0,"XZ":0.0,"ZX":0.0,"ZZ":0.0,"YY":0.0, "IX":0.0, "IZ":1.0} )

        success_condition_list.append( {"ZZ":1.0} )
        qubits_used_list.append( [ "a", "b[" + j + "]" ] )
        allowed_gates_list.append( { "a":{"z":0}, "b[" + j + "]":{"x":0,"z":0,"h":0}, "both":{"cz":0} } )
        intro.append( ["Since bit "+j+" has different values for the two file names, it needs to be part of the superposition",
        "So we spread the superposition from qubit a to qubit b["+j+"] by copying the superposed bit",
        "This will mean that both qubits will have random outputs from their blue boxes, but those outputs will always agree",
     "The signature of this is that the middle blue box will be empty, so work towards this target"] )
        outro.append( ["Great!",
        "Copy the QISKit program into the notebook. Do this with a right click, rather than ctrl-C"] )

    for j in superpos["diff"] :

        state_list.append( {"XI":0.0, "ZI":0.0,"XX":0.0,"XZ":0.0,"ZX":0.0,"ZZ":0.0,"YY":0.0,"IX":0.0, "IZ":1.0} )
        success_condition_list.append( {"ZZ":-1.0} )
        qubits_used_list.append( [ "a", "b[" + j + "]" ] )
        allowed_gates_list.append( { "a":{"z":0}, "b[" + j + "]":{"x":0,"z":0,"h":0}, "both":{"cz":0} } )
        intro.append( ["Since bit "+j+" has different values for the two file names, it needs to be part of the superposition",
        "But since its value is always different to the first bit in the superposition, we also need to make it disagree",
        "This means that the middle blue box will need to be full"] )
        outro.append( ["Great!",
        "Copy the QISKit program into the notebook. Do this with a right click, rather than ctrl-C"] )


    level_num = len(state_list)

    return state_list, success_condition_list, qubits_used_list, allowed_gates_list, level_num, intro, outro

# sandbox
def GetLevelBell () :

    state_list = []
    success_condition_list = []
    qubits_used_list = []
    allowed_gates_list = []
    intro = []
    outro = []

    # create target state and string
    target, target_string = MakeTarget( {"XI":0, "ZI":1.0,"XX":0.0,"XZ":0.0,"ZX":0.0,"ZZ":1.0,"YY":0.0,"IX":0.0, "IZ":1.0}, [["h","0"],["cx","1"],["q","0"],["h","0"]] )
    
    # add them in
    state_list.append( {"XI":0.0, "ZI":1.0,
                                            "XX":0.0,"XZ":0.0,"ZX":0.0,"ZZ":1.0,"YY":0.0,
                                            "IX":0.0, "IZ":1.0} )
    success_condition_list.append( target )
    allowed_gates_list.append( { "A":{"x":0,"z":0,"h":0,"bloch":0,"q":0,"qdg":0,"cx":0}, "B":{"x":0,"z":0,"h":0,"bloch":0,"q":0,"qdg":0,"cx":0}, "both":{"unbloch":0,"cz":0} } )

    intro.append(    ["This mode relates to a Jupyter notebook in which you can explore Bell tests",
                                    "You'll find the notebook at github.com/decodoku/Quantum_Programming_Tutorial/tree/master/bell-test ",
                                    "A good state to aim for is the following",
                                    target_string,
                                    "But you can also use this mode as a sandbox"])
    qubits_used_list.append( [ "A", "B" ] )
    outro.append( ["If you are seeing this, you somehow disproved Heisenberg's uncertainty principle",
                                 "Either that or there is a bug"] )


    level_num = len(state_list)

    return state_list, success_condition_list, qubits_used_list, allowed_gates_list, level_num, intro, outro