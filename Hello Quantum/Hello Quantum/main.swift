//
//  main.swift
//  HelloQuantum
//
//  Created by James Wootton on 07/12/17.
//  Copyright © 2017 University of Basel. All rights reserved.
//

import Foundation

func Input ( message: String ) {
    //  DESCRIPTION:
    //      Prints the message to screen and waits for an (unused) input to proceed.
    print( message )
    if var unused_input = readLine() {
        unused_input = unused_input + ""
    }
}

func PrintBottomLines (message: String ) {
    //  DESCRIPTION:
    //      Deletes the bottom two lines of the terminal ouput and then prints over them.

    print("\u{001B}[5F") // move cursor back 5 lines
    print("\u{001B}[0J") // clear from cursor
    print( message ) // print the message

}

func  Expect2Prob ( expect: Double ) -> Double {
    //  DESCRIPTION:
    //      Converts expectation value to a probability of getting the outcome 1.
    return (1-expect)/2
}

func Expect2Polar ( boxes: [String: Double] ) -> [Double] {
    //  DESCRIPTION:
    //      Takes the contents of an X and Z box and turns it into polar coordinates for the Bloch circle.
    //  INPUT:
    //      [String: Double]    boxes       Should have entries for "X" and "Z", which serve as the horizontal and vertical boxes respectively.
    //  OUTPUT:
    //      [Double]            [ degrees, radius ]     degrees is between 0 and 1. It is the angle clockwise from the top as a fraction of 2*Pi. Radius is how far out the point is. Will be 1 for pure states and 0 for maximally mixed.
    
    let radius: Double = sqrt( pow( boxes["X"]! ,2) + pow( boxes["Z"]! ,2) )
    var degrees: Double = 0 // default value of 0
    if radius>0.0 {
        degrees = acos( -boxes["Z"]! / radius ) / (2*Double.pi)
        if boxes["X"]!>=0.0 {
            degrees = 1 - degrees
        }
    }

    return [ degrees, radius ]
}

func Polar2Expect ( polar_coords: [Double] ) -> [String: Double] {
    //  DESCRIPTION:
    //      As Boxes2Polar, but with inputs and outputs reversed
    var boxes = [String: Double]()
    boxes["X"] = -polar_coords[1] * sin( 2*Double.pi*polar_coords[0])
    boxes["Z"] = -polar_coords[1] * cos( 2*Double.pi*polar_coords[0])
    return boxes
}

func ExchangeBoxes ( state: [String: Double], box1: String, box2: String ) -> [String: Double] {
    //  DESCRIPTION:
    //      Given a state and two of its boxes, the values for these boxes are exchanged
    var output_state: [String: Double] = state
    let temp: Double = output_state[box1]!
    output_state[box1]! = output_state[box2]!
    output_state[box2]! = temp
    return output_state
}

func ApplyGate ( state: [String: Double], gate: String, qubit: String ) -> [String: Double] {
    //  DESCRIPTION:
    //      Transforms the given state according to the given gate.
    //  INPUT:
    //      [String: Double]    state       Full two qubit state. Needs entries for XI, ZI, IZ, IX, XX, XZ, ZX, ZZ and YY
    //      String              gate        QISKit style string to specify a gate (can be x, z, h, q, qdg, or cz)
    //      Int                 qubit       Qubit on which single qubit gate is applied. Unused for CZ.
    //  OUTPUT:
    //      [String: Double]    state       Transformed version of input state.
    
    // We begin constructing the output state by copying the input state.
    var output_state: [String: Double] = state
    
    // Single qubit gates require special treatment, so we deal with these separately.
    if ["x","z","h","q","qdg"].contains(gate) {
        // Single qubit gates act on pairs of boxes. These are the pairs that form Bloch circles.
        // For qubit 0, these pairs are  (XI, ZI), (XX,ZX) and (XZ,ZZ).
        // For qubit 2 they are (IX, IZ), (XX,XZ) and (ZX,ZZ).
        // Here we loop over and construct the three pairs, which in each case will be (p[0],p[1]).
        for rc in ["I","X","Z"] {
            
            var box_name: [String: String] = ["X":rc,"Z":rc]
            for p in ["X","Z"] {
                if qubit=="0" {
                    box_name[p]! = p + box_name[p]!
                } else {
                    box_name[p]! = box_name[p]! + p
                }
            }
            
            // What we do to the pairs depends on the gate we apply.
            if gate=="x"{ // invert Z box and invert YY
                output_state[box_name["Z"]!]! = -output_state[box_name["Z"]!]!
                output_state["YY"]! = -output_state["YY"]!
            } else if gate=="z" {// invert X box and invert YY
                output_state[box_name["X"]!]! = -output_state[box_name["X"]!]!
                output_state["YY"]! = -output_state["YY"]!
            } else if gate=="h" { // exchange X and Z boxes and invert YY
                output_state = ExchangeBoxes(state:output_state, box1:box_name["X"]!, box2:box_name["Z"]!)
                output_state["YY"]! = -output_state["YY"]!
            } else if ["q","qdg"].contains(gate) {
                var polar_coords: [Double] = Expect2Polar(boxes: [ "X":output_state[box_name["X"]!]!, "Z":output_state[box_name["Z"]!]! ] ) // convert to polar coords
                if gate=="q" { // change angle according to the rotation
                    polar_coords[0] += 1/8
                } else {
                    polar_coords[0] -= 1/8
                }
                // convert back to boxes
                let output_boxes: [String: Double] = Polar2Expect(polar_coords: polar_coords)
                for p in ["X","Z"] { output_state[box_name[p]!]! = output_boxes[p]! }
            } else {
                print("Error: Unknown single qubit gate")
            }
            
        }
    // Now for the two qubit gates
    } else if gate=="cz" {
        // exchange contents of XI and XZ
        output_state = ExchangeBoxes(state:output_state, box1:"XI", box2:"XZ")
        // exchange contents of IX and ZX
        output_state = ExchangeBoxes(state:output_state, box1:"IX", box2:"ZX")
        // exchange contents of XX and YY
        output_state = ExchangeBoxes(state:output_state, box1:"XX", box2:"YY")
    } else if gate=="cx" {
        if qubit=="1" {
            // exchange contents of XI and XX
            output_state = ExchangeBoxes(state:output_state, box1:"XI", box2:"XX")
            // exchange contents of IZ and ZZ
            output_state = ExchangeBoxes(state:output_state, box1:"IZ", box2:"ZZ")
            // exchange contents of XZ and YY
            output_state = ExchangeBoxes(state:output_state, box1:"XZ", box2:"YY")
            // invert XZ 
            output_state["XZ"]! = -output_state["XZ"]!
        } else if qubit=="0" {
            // exchange contents of ZI and ZZ
            output_state = ExchangeBoxes(state:output_state, box1:"ZI", box2:"ZZ")
            // exchange contents of IX and XX
            output_state = ExchangeBoxes(state:output_state, box1:"IX", box2:"XX")
            // exchange contents of ZX and YY
            output_state = ExchangeBoxes(state:output_state, box1:"ZX", box2:"YY")
            // invert ZX       
            output_state["ZX"]! = -output_state["ZX"]!
        }
        output_state["YY"]! = -output_state["YY"]! // invert YY
    } else {
        print("Error: Unknown gate")
    }
    
    return output_state
    
}

func MakeInitial ( target_state : [String: Double], inverse_solution: [[String]] ) -> ( [String: Double] ) {
    //  DESCRIPTION:
    //      Constructs an initial state such that the target state and solution are as specified by the input
    //      Note that the inverse of the desired solution must be supplied here
    //      Put simply, this means that the first gate should be on the right, and the substition q <-> qdg should be used
    
    var state: [String: Double] = target_state
    for gate in inverse_solution {
        state = ApplyGate(state:state,gate:gate[0],qubit:gate[1])
    }
    return state
    
}

func MakeCell ( cell_state: [String: Double] ) -> [String] {
    //  DESCRIPTION:
    //      Prints a single box or Bloch circle, depending on the input state.
    //  INPUT:
    //      [String: Double]    cell_state  With key "X", value is the expectation value for horizontal red box.
    //                                      Similarly for "Z" and the vertical blue box, and "Y" for a diagonal purple box.
    //                                      Note that a cell that uses "Y" will correspond to XZ or ZZ boxes. Not a Y box.
    //  OUTPUT:
    //      [String]            lines       List of 12 lines, which when printed sequentially will display the cell.
    //  PROCESS:
    //      When a single key is supplied, the corresponding box is printed.
    //      When both "X" and "Z" are supplied, the boxes are combined into a Bloch circle.
    //      In all cases, the level on the box is first converted from the expectation value to the probability.
    var reso: [String:  Int] = ["X":17, "Z":9, "Y":13] // number of characters used for each type of box (including center)

    let bottom: String = "───────────────────────" // bottom border
    let right: String = "|" // right border

    // The 8 points around the circle and one in the middle. Default to a dot
    var c = [String]()
    
    c.append("˙")
    c.append(".")
    c.append("·")
    c.append("˙")
    c.append(".")
    c.append("˙")
    c.append("·")
    c.append(".")
    c.append(" ")
    
    // When a Bloch sphere is displayed, the point corresponding to the state is denoted by "o"
    // This is displayed only for pretty mixed states (radius <0.25) and pretty pure ones (radius>0.75)
    if (cell_state["X"] != nil && cell_state["Z"] != nil ) { // both X  and Z boxes need to be present in the cell
        if ( Expect2Polar( boxes: cell_state )[1]<0.25 ) { // if state is pretty mixed, point is shown in the center
            c[8] = "*"
        } else if Expect2Polar( boxes: cell_state )[1]>0.75 { // if state is pretty pure, it is one of the 8 around the edge
            var point: Int = 0
            let degree = Expect2Polar( boxes: cell_state )[0]
            for eighth in 1...7 {
                if  degree>(Double(eighth)/8 - 1.0/16) && degree<=(Double(eighth)/8 + 1.0/16 ) {
                    point = eighth
                }
            }
            if [1,4,7].contains(point) {
                c[ point ] = "⁎"
            } else {
                c[ point ] = "*"
            }
        }
    }

    // Strings for the three boxes. Blank if unused, but filled with █ and ░ if used to represent how 'filled' they are.
    var b: [String: [String]] = [ "X":[], "Z":[], "Y":[] ]
    for box in [ "X", "Z", "Y" ] {
        var this_b = [String]()
        if cell_state[box] == nil {
            for _ in 1...reso[box]! {
                this_b.append(" ")
            }
        } else {
            let prob = Expect2Prob( expect: cell_state[box]! ) // convert from expectation value to prob of a 1 outcome
            var fill = Int( Double(reso[box]!) * prob )
            if (prob>0.5 && fill != reso[box]!) { // if over half filled, but not completely filled, round up (for clear visuals)
                fill += 1
            }
            for _ in 0..<fill {
                if box == "X" {
                    this_b.append("█".redColor)
                } else if box == "Z" {
                    this_b.append("█".blueColor)
                }
                else if box == "Y" {
                    this_b.append("█".purpleColor)
                }
            }
            for _ in fill..<reso[box]! {
                if box == "X" {
                    this_b.append("░".redColor)
                } else if box == "Z" {
                    this_b.append("░".blueColor)
                }
                else if box == "Y" {
                    this_b.append("░".purpleColor)
                }                
            }
        }
        b[box]! = this_b
    }
    
    // center is X with the colour of the cell, unless the cell is empty
    if cell_state["Y"] != nil {
        c[8] = b["Y"]![Int(reso["Y"]!/2)].purpleColor
    } else if cell_state["X"] != nil {
        c[8] = b["X"]![Int(reso["X"]!/2)].redColor
    } else if cell_state["Z"] != nil {
        c[8] = b["Z"]![Int(reso["Z"]!/2)].blueColor
    }
    
    b["X"]![Int(reso["X"]!/2)] = c[8] // The center will be the ninth element of c instead

    // Declare and construct the lines.
    var lines = [String]()
    if cell_state.isEmpty {
        for _ in 1...11 {
            lines.append( "                       "+right )
        }
    } else {
        lines.append( "      .·  "+c[0]+"  ·.        "+right )
        lines.append( "   "+c[7]+"˙     "+b["Z"]![8]+"     ˙"+c[1]+"     "+right )
        lines.append( "  ·       "+b["Z"]![7]+"    "+b["Y"]![11]+b["Y"]![12]+" ·    "+right )
        lines.append( " ·        "+b["Z"]![6]+"  "+b["Y"]![9]+b["Y"]![10]+"    ·   "+right )
        lines.append( "          "+b["Z"]![5]+""+b["Y"]![7]+b["Y"]![8]+"          "+right )
        lines.append( ""+c[6]+" "+b["X"]!.joined()+" "+c[2]+"  "+right )
        lines.append( "        "+b["Y"]![4]+b["Y"]![5]+""+b["Z"]![3]+"            "+right )
        lines.append( " ˙    "+b["Y"]![2]+b["Y"]![3]+"  "+b["Z"]![2]+"        ˙   "+right )
        lines.append( "  · "+b["Y"]![0]+b["Y"]![1]+"    "+b["Z"]![1]+"       ·    "+right )
        lines.append( "   "+c[5]+".     "+b["Z"]![0]+"     ."+c[3]+"     "+right )
        lines.append( "      ˙·  "+c[4]+"  ·˙        "+right )
    }
    lines.append( bottom + right )
    
    return lines

}

func MakeGrid ( state: [String: Double], shown_qubit: Int, active_qubit: Int, bloch: Bool ) -> [String] {

    //  DESCRIPTION:
    //      The inputs describe what the grid is doing. This function puts all that information together to actually make the grid.
    //  INPUT:
    //      [String: Double]    state   Full two qubit state. Needs entries for XI, ZI, IZ, IX, XX, XZ, ZX, ZZ and YY
    //      Int     shown_qubit     If this is 0 or 1, only the two boxes of that qubit are shown. Otherwise, all are shown.
    //      Int     active_qubit	If this is 0 or 1, the diagonals are straightened according to their function for this qubit. Otherwise they remain diagonal.
    //	    Bool    bloch       	Whether or not to display Bloch circles for the qubit specified above
    //  OUTPUT:
    //      [String]    grid_lines   An array of strings that represent the grid
    
    var cells: [String: [String]] = ["XI":[], "ZI":[],
                                    "XX":[],"XZ":[],"ZX":[],"ZZ":[],"YY":[],"II":[],
                                    "IX":[], "IZ":[]]
    
    // determine which cells behave in which way (I is blank, B is Bloch circle, X and Z are horizontal and vertical boxes and Y are diagonal)
    var grid_lines = [String]()
    var cell_types = [String: [String]]()
    if bloch {
        if shown_qubit==0 {
            cell_types = ["I":["II","ZI","XX","XZ","ZX","ZZ","YY","IX","IZ"],"X":[],"Y":[],"Z":[],"B":["XI"]] // shown_qubit is used as active qubit
        } else if shown_qubit==1 {
            cell_types = ["I":["II","XI","ZI","XX","XZ","ZX","ZZ","YY","IZ"],"X":[],"Y":[],"Z":[],"B":["IX"]] // shown_qubit is used as active qubit
        } else {
            if active_qubit==0 {
                cell_types = ["I":["II","ZI","ZX","ZZ"],"X":["IX"],"Y":[],"Z":["IZ"],"B":["XI","XX","XZ"]]
            } else if active_qubit==1 {
                cell_types = ["I":["II","IZ","XZ","ZZ"],"X":["XI"],"Y":[],"Z":["ZI"],"B":["IX","XX","ZX"]] // these are the same as above but with strings reversed
            } else {
                print("Error: A valid qubit must be chosen to display a Bloch circle")
            }
        }
    } else {
        if shown_qubit==0 {
            cell_types = ["I":["II","XX","XZ","ZX","ZZ","YY","IX","IZ"],"X":["XI"],"Y":[],"Z":["ZI"],"B":[]]
        } else if shown_qubit==1 {
            cell_types = ["I":["II","XI","ZI","XX","XZ","ZX","ZZ","YY","IX","IZ"],"X":["IX"],"Y":[],"Z":["IZ"],"B":[]]
        } else {
            // Y for diagonal boxes, since there is no active qubit
            cell_types = ["I":["II"],"X":["XI","IX","XX"],"Y":["XZ","ZX"],"Z":["ZI","IZ","ZZ"],"B":[]]
        }
    }
    // make blank cell
    for cell in cell_types["I"]! {
        cells[cell]! = MakeCell( cell_state: [:] )
    }
    // make cells with horizontal and vertical boxes
    for cell_type in ["X","Z"] {
        for cell in cell_types[cell_type]! {
            cells[cell]! = MakeCell( cell_state: [ cell_type:state[cell]! ] )
        }
    }
    // make cells with diagonal boxes
    for cell in cell_types["Y"]! {
        if [0,1].contains(active_qubit) {
            let index = cell.index(cell.startIndex, offsetBy: active_qubit)
            cells[cell]! = MakeCell( cell_state: [ String(cell[index]):state[cell]! ] ) // qubit dependent cell type is used
        } else {
            cells[cell]! = MakeCell( cell_state: [ "Y":state[cell]! ] ) // same as in X,Z loop above
        }
    }
    // make cells with Bloch circle
    for cell in cell_types["B"]! {
    	let index = cell.index(cell.startIndex, offsetBy: (1-active_qubit) )
        if active_qubit==0 {
                cells[cell]! = MakeCell( cell_state: [ "X":state["X"+String(cell[index])]!, "Z":state["Z"+String(cell[index])]! ] )
            
        } else {
                cells[cell]! = MakeCell( cell_state: [ "X":state[String(cell[index])+"X"]!, "Z":state[String(cell[index])+"Z"]! ] )
        }
    }
    
    for l in 0...11{
        grid_lines.append( cells["II"]![l] + cells["ZI"]![l] + cells["XI"]![l] )
    }
    for l in 0...11{
        grid_lines.append( cells["IZ"]![l] + cells["ZZ"]![l] + cells["XZ"]![l] )
    }
    for l in 0...11{
        grid_lines.append( cells["IX"]![l] + cells["ZX"]![l] + cells["XX"]![l] )
    }

     return grid_lines

}

// Here we iterate through each level, getting the details for each from GetLevel()

var state: [String: Double] = [:]
var success_condition: [String: Double] = [:]
var qubits_used: [String] = []
var allowed_gates: [String:[String: Int]] = [:]
var level_num: Int = 1
var intro: [String] = []
var outro: [String] = []

var grid_lines: [String]

// clear screen and put title
print("\u{001B}[2J")
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
print("           github.com/decodoku/Quantum_Programming_Tutorial")
print("\n")
print("\n")
print("\n")
print("  Choose which mode you want to play from the following list")
print("")
print("  1 - Story Mode\n      A gamified tutorial for programming quantum computers.\n")
print("  2 - Sandbox\n      A chance to do what you want with two qubits.\n")
print("  3 - Image Superposer\n      Write a quantum program to create superpositions of images.\n")
print("\n> Input a number to select a mode...")
//putting in some protections to prevent it from crashing if fed the wrong input
guard let modeString = readLine(), let modeFromInput = Int(modeString) else { exit(EXIT_FAILURE) }
var mode = modeFromInput
if mode < 1 || mode>3 {
    mode = 1
}

var level: Int = 1
var string1: String = ""
var string2: String = ""
if mode==1 {

    ( state, success_condition, qubits_used, allowed_gates, level_num, intro, outro ) = GetLevelStory( level: 0 ) // get level settings, but just to get the number of levels

    print("\n> Choose level to start at\n> Type a number below and press Enter...")
    //putting in some protections to prevent it from crashing if fed the wrong input
    guard let levelString = readLine(), let levelFromInput = Int(levelString) else { exit(EXIT_FAILURE) }
    level = levelFromInput
    if level < 1 || level>level_num {
        level = 1
    }

} else if mode==2 {
    ( state, success_condition, qubits_used, allowed_gates, level_num, intro, outro ) = GetLevelStory( level: 0 ) // get level settings, but just to get the number of levels
} else if mode==3 {

    Input(message:"\n> In the following puzzles, you'll write a quantum program that can be run on a real machine...(Press Enter to continue)")
    Input(message:"\n> This will create a quantum superposition of two images. See [github link] for more details...")

    let allowed_filenames = ["0000","0001","0010","0011", "0100","0101","0110","0111", "1000","1001","1010","1011", "1100","1101","1110","1111"]

    var names_needed = true
    while names_needed==true {

	    print("\n> Input the filename of the first image for the superposition\n  This must be a string of four bits (e.g. 0000, 0101, 0110, 111)....")
	    string1 = readLine()!
	    print("\n> Input the filename of the second image for the superposition\n  This must be a string of four bits (e.g. 0000, 0101, 0110, 111)....")
	    string2 = readLine()!

	    if allowed_filenames.contains( string1 ) && allowed_filenames.contains( string2 ) && ( string1 != string2 ) {
		names_needed = false
	    } else {
                Input(message:"\n> Something wasn't quite right with those bit strings. Try again...")
            }

    }

    ( state, success_condition, qubits_used, allowed_gates, level_num, intro, outro ) = GetLevelSuperposer( level: 0 , string1:string1, string2:string2 ) // get level settings

}

while (level==1 || level<=level_num) {
    
    var bloch: Bool = false // always start a level with Bloch off
    var active_qubit: Int = -1
    var program: [String] = []
    
    // calling these functions every level seems a bit inefficient
    // probably we should change it to output the full lists, and output them only once
    if mode==1 {
        ( state, success_condition, qubits_used, allowed_gates, level_num, intro, outro ) = GetLevelStory( level: level-1 ) // get level settings
    } else if mode==2 {
        ( state, success_condition, qubits_used, allowed_gates, level_num, intro, outro ) = GetLevelSandbox( level: level-1 ) // get level settings
    } else if mode==3 {
        ( state, success_condition, qubits_used, allowed_gates, level_num, intro, outro ) = GetLevelSuperposer( level: level-1 , string1:string1, string2:string2 )// get level settings
    }

    // every puzzle is thought of as one involving two qubits, even if only one of those qubits is involved
    // qubits_used should therefore always be a list of two qubits, the first is the one displayed on the top, and the second is the one on the bottom

    var shown_qubit: Int
    if let q_zero_gates = allowed_gates[qubits_used[0]], q_zero_gates.isEmpty { // if no gates are allowed for the qubit on top, we know to only show the qubit on the side
        shown_qubit = 1
    } else if let q_one_gates = allowed_gates[qubits_used[1]], q_one_gates.isEmpty { // and vice versa
        shown_qubit = 0
    } else {
        shown_qubit = 2
    }

    var success = false
    var restart = false
    
    print("\u{001B}[2J")
    print("\nLevel \(level)\n")
    for line in intro{
        Input(message: "> " + line + "...")
    }
    
    var required_gates: [String:[String: Int]] = allowed_gates

    while success==false && restart==false {
        
	// set up the screen: job 1
	// text at the top
        print("\u{001B}[2J")
        print("\nLevel \(level)\n")
        for line in intro{
            print("> " + line + "...\n")
        }
        if program != [] {
            print("\nYour QISKit program so far\n")
            for line in program {
                print(line)
            }
        }
        print("\n")

        // set up the screen: job 2
        // the grid
        grid_lines = MakeGrid( state: state, shown_qubit: shown_qubit, active_qubit: active_qubit, bloch: bloch )
        for line in grid_lines {
            print("   "+line)
        }
        
        // set up the screen: job 3
        // state allowed gates
        var gate_types = qubits_used // this will be an ordered list of [qubit at top, qubit at side, both (if such operations exist)]
        if let two_qubit_gates = allowed_gates["both"], !(two_qubit_gates.isEmpty){
            gate_types.append("both")
        }
        for qubit in gate_types {
            if let qubit_gates = allowed_gates[qubit], !(qubit_gates.isEmpty) {

                if qubit=="both" {
                    print("\nAllowed two qubit operations:")
                } else {
                	print("\nAllowed operations for qubit " + qubit + ":")
                }
                var gate_list: String = ""
                for gate in qubit_gates.keys {
                    if let num_gates = qubit_gates[gate], num_gates > 0 {
                        gate_list += "   "+gate+" (use exactly \(num_gates) times)"
                    } else {
                        gate_list += "  "+gate
                    }
                }
                print(gate_list)
            }
        }

        // set up the screen: job 4
        // ask player to choose an operation
        print("Error: This should have been overwritten\nError: This should have been overwritten\nError: This should have been overwritten\nError: This should have been overwritten")

        var gate: String = ""
        while gate == "" {
	    let combined_gates: Set<String> = Set( Array(allowed_gates[qubits_used[0]]!.keys) + Array(allowed_gates[qubits_used[1]]!.keys) + Array(allowed_gates["both"]!.keys) )
            PrintBottomLines(message: "> Choose one of the allowed operations from the list above by typing its name below\n> Or type restart to start this puzzle over..." )
            if let input = readLine() {
                if combined_gates.contains(input) || input=="restart" {
                    gate = input
                }

            }
        
        }

        // ask player for a qubit to act on (if there is a choice)...
        var qubit: String = ""
        if ["cz","unbloch","restart"].contains(gate) { // for gates that act symmetrically the choice is irrelevant, and so set by default to both
            qubit = "both"
        } else if shown_qubit==0 { // if only the top qubit is shown, that's what the gate acts on
	    qubit = qubits_used[0]
	} else if shown_qubit==1 { // if only the side qubit is shown, that's what the gate acts on
	    qubit = qubits_used[1]
	} else if !Array(allowed_gates[qubits_used[0]]!.keys).contains(gate) { // if the gate isn't an allowed one for the top qubit, it acts on the side
            qubit = qubits_used[1]
        } else if !Array(allowed_gates[qubits_used[1]]!.keys).contains(gate) { // and vice-versa
            qubit = qubits_used[0]
        } else { // otherwise, the choice must be made
            while [qubits_used[0],qubits_used[1]].contains(qubit) == false {
                PrintBottomLines(message: "> Choose a qubit to act on:\n> Type in "+qubits_used[0]+" or "+qubits_used[1]+"...")
                qubit = readLine() ?? ""
            }
        }  



        // if it is a gate, apply it
        if ["x","z","h","q","qdg","cz","cx"].contains(gate) {
            // the apply gate function adresses qubits as 0 and 1, so we convert back to this before applying
            var qubit_pos: String
	    if qubit==qubits_used[0] {
                qubit_pos = "0"
            } else if qubit==qubits_used[1] {
                qubit_pos = "1"
            } else {
                qubit_pos = "both"
            }
            state = ApplyGate( state: state, gate: gate, qubit: qubit_pos )
            // then we write the qiskit commands
            if gate=="cz"{
                program.append("program.cz( qubit["+qubits_used[0]+"], qubit["+qubits_used[1]+"] )")
            } else if gate=="cx"{
                if qubit==qubits_used[0] {
		    program.append("program.cx( qubit["+qubits_used[1]+"], qubit["+qubits_used[0]+"] )")
                } else {
                    program.append("program.cx( qubit["+qubits_used[0]+"], qubit["+qubits_used[1]+"] )")
                }
            } else {
                program.append("program."+gate+"( qubit["+qubit+"] )")
            }
        }
        // if it is a visualization command, apply it
        else if gate=="bloch" {
            bloch = true
            if qubit==qubits_used[0]{
                active_qubit = 0
            } else if qubit==qubits_used[1] {
                active_qubit = 1
            }
        } else if gate=="unbloch" {
            bloch = false
            active_qubit = -1
        } else if gate=="restart" {
            restart = true
        } else {
            print("Error: Something's not quite right")
        }

        // log it
        if let qubit_gates = allowed_gates[qubit], let q_gate = qubit_gates[gate] {
            if q_gate > 0 {
                //weve already checked to see if these things exist, and we know they do so its ok to implicitly unwrap them
                // James: actually, now the above checks allows_gates, and below we manipulated required gates. But it should work!
                required_gates[qubit]![gate]! -= 1
            }
            if required_gates[qubit]![gate]! < 0 {
                Input(message: "> You have used this gate too many times, so the level will restart...")
                restart = true
            }
        } else {
            print("That operation is not allowed here fool")
        }
        
        // see if success conditions are met
        success = true
        // the final state has to be right
        for (box, expect) in success_condition {
            print(box,expect,state[box]!)
            success = success && state[box]!==expect
        }
        // and the number of ops has to be right
        for qubit in required_gates.keys {
            for gate in required_gates[qubit]!.keys {
                if (required_gates[qubit]![gate]! > 0) {
                    success = false
                }
            }
        }


    }
    
    if restart==false {
    
        // set up the screen: job 1
        // text at the top
        print("\u{001B}[2J")
        print("")
        for line in intro{
            print("> " + line + "...")
        }
        if program != [] {
            print("\nYour QISKit program so far\n")
            for line in program {
                print("  " + line)
            }
        }
        print("\n")

        // set up the screen: job 2
        // the grid
        grid_lines = MakeGrid( state: state, shown_qubit: shown_qubit, active_qubit: active_qubit, bloch: bloch )
        for line in grid_lines {
            print("   "+line)
        }
        
        // set up the screen: job 3
        // a gap of the same height as the allowed qubits
        for qubit in allowed_gates.keys {
            if let qubit_gates = allowed_gates[qubit], !(qubit_gates.isEmpty) {
                if ["0","1"].contains(qubit) {
                    print("\n")
                } else {
                    print("\n")
                }
                print("\n")
            }
        }
        
        // set up the screen: job 4
        // outro
        for line in outro{
            Input(message: "> " + line + "...")
        }
        
        level += 1
    }

}

if mode==1 {
    Input(message: "> That's all the levels we have for now. Restart the program, or continue your QISKit journey at QISKit.org")
} else if mode==2 {
    Input(message: "> How are you seeing this?!?!?!?!?!?!?!")
} else if mode==3 {
    Input(message: "> Now you have your QISKit program. You just need to run the notebook for your image.")
}

