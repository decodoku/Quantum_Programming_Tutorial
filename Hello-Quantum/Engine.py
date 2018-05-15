# -*- coding: utf-8 -*-

import math

def ClearScreen () :
  # DESCRIPTION:
  #     Prints a whole bunch of space to screen
  print("\n"*200)

def ColouredString (message,colour) :
  #  DESCRIPTION:
  #      Prints in a colour specified by the colour in ["r","b","p"] and then sets what follows back to white

  # first the colour
  coloured_message = ""
  if colour=="r": # red
    coloured_message += "\x1b[1;31m"
  elif colour=="g": # green
    coloured_message += "\x1b[1;32m"
  elif colour=="b": # blue
    coloured_message += "\x1b[1;34m" 
  elif colour=="p": # purple
    coloured_message += "\x1b[1;35m"
  else: # black (which should actually be the default text colour)
    coloured_message += "\x1b[0m"
  
  # then the message
  coloured_message += message

  # and back to black
  coloured_message += "\x1b[0m"
  
  return coloured_message

def  Expect2Prob ( expect ) :
  #  DESCRIPTION:
  #      Converts expectation value to a probability of getting the outcome 1.
  return (1-expect)/2
  
def Expect2Polar ( boxes ) :
  #  DESCRIPTION:
  #      Takes the contents of an X and Z box and turns it into polar coordinates for the Bloch circle.
  #  INPUT:
  #      {String: Float}    boxes       Should have entries for "X" and "Z", which serve as the horizontal and vertical boxes respectively.
  #  OUTPUT:
  #      [Float]            [ degrees, radius ]     degrees is between 0 and 1. It is the angle clockwise from the top as a fraction of 2*Pi. Radius is how far out the point is. Will be 1 for pure states and 0 for maximally mixed.
 
  radius = math.sqrt( boxes["X"]**2 + boxes["Z"]**2)
  degrees = 0 # default value of 0
  if radius>0.0:
    degrees = math.acos( -boxes["Z"] / radius ) / (2*math.pi)
    if boxes["X"]>=0.0:
      degrees = 1 - degrees

  return [ degrees, radius ]

def Polar2Expect ( polar_coords ) :
  #  DESCRIPTION:
  #      As Boxes2Polar, but with inputs and outputs reversed
  boxes = {}
  boxes["X"] = -polar_coords[1] * math.sin( 2*math.pi*polar_coords[0])
  boxes["Z"] = -polar_coords[1] * math.cos( 2*math.pi*polar_coords[0])
  return boxes
    
def ExchangeBoxes ( state, box1, box2 ) :
  #  DESCRIPTION:
  #      Given a state and two of its boxes, the values for these boxes are exchanged
  output_state = state
  temp = output_state[box1]
  output_state[box1] = output_state[box2]
  output_state[box2] = temp
  return output_state

def Swap ( state ) :
  #  DESCRIPTION:
  #      Determines the state after a swap gate
  #  INPUT:
  #      {String: Float}    state       Two qubit state.
  #  OUTPUT:
  #      {String: Float}    state       Transformed version of input state.
    
  swapped_state = {}
  for box in state.keys():
    swapped_state[box[1]+box[0]] = state[box]
    
  return swapped_state

def ApplyGate ( state, gate, qubit ) :
  #  DESCRIPTION:
  #      Transforms the given state according to the given gate.
  #  INPUT:
  #      {String: Float}    state       Full two qubit state. Needs entries for XI, ZI, IZ, IX, XX, XZ, ZX, ZZ and YY
  #      String              gate        QISKit style str to specify a gate (can be x, z, h, q, qdg, or cz)
  #      Int                 qubit       Qubit on which single qubit gate is applied. Unused for CZ.
  #  OUTPUT:
  #      {String: Float}    state       Transformed version of input state.
  
  # We begin constructing the output state by copying the input state.
  output_state = state
  
  # Single qubit gates require special treatment, so we deal with these separately.
  if gate in ["x","z","h","q","qdg"] :
    # Single qubit gates act on pairs of boxes. These are the pairs that form Bloch circles.
    # For qubit 0, these pairs are  (XI, ZI), (XX,ZX) and (XZ,ZZ).
    # For qubit 2 they are (IX, IZ), (XX,XZ) and (ZX,ZZ).
    # Here we loop over and construct the three pairs, which in each case will be (p[0],p[1]).
    for rc in ["I","X","Z"] :
            
      box_name = {"X":rc,"Z":rc}
      for p in ["X","Z"] :
        if qubit=="0" :
          box_name[p] = p + box_name[p]
        else :
          box_name[p] = box_name[p] + p
      
      # What we do to the pairs depends on the gate we apply.
      if gate=="x": # invert Z box and invert YY
        output_state[box_name["Z"]] = -output_state[box_name["Z"]]
        output_state["YY"] = -output_state["YY"]
      elif gate=="z" :# invert X box and invert YY
        output_state[box_name["X"]] = -output_state[box_name["X"]]
        output_state["YY"] = -output_state["YY"]
      elif gate=="h" : # exchange X and Z boxes and invert YY
        output_state = ExchangeBoxes( output_state, box_name["X"], box_name["Z"])
        output_state["YY"] = -output_state["YY"]
      elif gate in ["q","qdg"] :
        polar_coords = Expect2Polar( { "X":output_state[box_name["X"]], "Z":output_state[box_name["Z"]] } ) # convert to polar coords
        if gate=="q" : # change angle according to the rotation
          polar_coords[0] += 1/8
        else :
          polar_coords[0] -= 1/8
          
        # convert back to boxes
        output_boxes = Polar2Expect(polar_coords)
        for p in ["X","Z"] :
          output_state[box_name[p]] = output_boxes[p]
      else :
        print("Error: Unknown single qubit gate")

  # Now for the two qubit gates
  elif gate=="cz" :
    # exchange contents of XI and XZ
    output_state = ExchangeBoxes( output_state, "XI", "XZ")
    # exchange contents of IX and ZX
    output_state = ExchangeBoxes( output_state, "IX", "ZX")
    # exchange contents of XX and YY
    output_state = ExchangeBoxes( output_state, "XX", "YY")
  elif gate=="cx" :
    if qubit=="1" :
      # exchange contents of XI and XX
      output_state = ExchangeBoxes( output_state, "XI", "XX")
      # exchange contents of IZ and ZZ
      output_state = ExchangeBoxes( output_state, "IZ", "ZZ")
      # exchange contents of XZ and YY
      output_state = ExchangeBoxes( output_state, "XZ", "YY")
      # invert XZ
      output_state["XZ"] = -output_state["XZ"]
    elif qubit=="0" :
      # exchange contents of ZI and ZZ
      output_state = ExchangeBoxes( output_state, "ZI", "ZZ")
      # exchange contents of IX and XX
      output_state = ExchangeBoxes( output_state, "IX", "XX")
      # exchange contents of ZX and YY
      output_state = ExchangeBoxes( output_state, "ZX", "YY")
      # invert ZX
      output_state["ZX"] = -output_state["ZX"]
      output_state["YY"] = -output_state["YY"] # invert YY
    else :
      print("Error: Unknown gate")
  
  
  return output_state
  
def MakeInitial ( target_state, inverse_solution ) :
  #  DESCRIPTION:
  #      Constructs an initial state such that the target state and solution are as specified by the input
  #      Note that the inverse of the desired solution must be supplied here
  #      Put simply, this means that the first gate should be on the right, and the substition q <-> qdg should be used
    
  state = target_state
  for gate in inverse_solution :
      state = ApplyGate( state, gate[0], gate[1] )
  return state
  
def MakeCell ( cell_state ) :
  #  DESCRIPTION:
  #      Prints a single box or Bloch circle, depending on the input state.
  #  INPUT:
  #      {String: Float}    cell_state  With key "X", value is the expectation value for horizontal red box.
  #                                      Similarly for "Z" and the vertical blue box, and "Y" for a diagonal purple box.
  #                                      Note that a cell that uses "Y" will correspond to XZ or ZZ boxes. Not a Y box.
  #  OUTPUT:
  #      [String]            lines       List of 12 lines, which when printed sequentially will display the cell.
  #  PROCESS:
  #      When a single key is supplied, the corresponding box is printed.
  #      When both "X" and "Z" are supplied, the boxes are combined into a Bloch circle.
  #      In all cases, the level on the box is first converted from the expectation value to the probability.
  
  reso = {"X":17, "Z":9, "Y":13} # number of characters used for each type of box (including center)

  bottom = "───────────────────────" # bottom border
  right = "|" # right border

  # The 8 points around the circle and one in the middle. Default to a dot
  c = []
  c.append("˙")
  c.append(".")
  c.append("·")
  c.append("˙")
  c.append(".")
  c.append("˙")
  c.append("·")
  c.append(".")
  c.append(" ")
  
  # When a Bloch sphere is displayed, the point corresponding to the state is denoted by "*"
  # This is displayed only for pretty mixed states (radius <0.25) and pretty pure ones (radius>0.75)
  if ( "X" in cell_state.keys() and "Z" in cell_state.keys() ) : # both X  and Z boxes need to be present in the cell
    if ( Expect2Polar( cell_state )[1]<0.25 ) : # if state is pretty mixed, point is shown in the center
      c[8] = "*"
    elif Expect2Polar( cell_state )[1]>0.75 : # if state is pretty pure, it is one of the 8 around the edge
      point = 0
      degree = Expect2Polar( cell_state )[0]
      for eighth in range(1,8) :
        if degree>(float(eighth)/8 - 1.0/16) and degree<=(float(eighth)/8 + 1.0/16 ) :
          point = eighth
      if point in [1,4,7] :
        c[ point ] = "⁎"
      else :
        c[ point ] = "*"


  # Strings for the three boxes. Blank if unused, but filled with █ and ░ if used to represent how 'filled' they are.
  b = {"X":[], "Z":[], "Y":[] }
  for box in [ "X", "Z", "Y" ] :
    this_b = []
    if box not in cell_state.keys() :
      for _ in range(1,reso[box]+1) :
        this_b.append(" ")
    else :
      prob = Expect2Prob( cell_state[box] ) # convert from expectation value to prob of a 1 outcome
      fill = int( float(reso[box]) * prob )
      
      if (prob>0.5 and fill != reso[box]) : # if over half filled, but not completely filled, round up (for clear visuals)
          fill += 1
      for _ in range(fill) :
        if box == "X" :
          this_b.append( ColouredString( "█" , "r" ) )
        elif box == "Z" :
          this_b.append( ColouredString( "█" , "b" ) )
        elif box == "Y" :
          this_b.append( ColouredString( "█" , "p" ) )

      for _ in range(fill,reso[box]) :
        if box == "X" :
          this_b.append( ColouredString( "░" , "r" ) )
        elif box == "Z" :
          this_b.append( ColouredString( "░" , "b" ) )
        elif box == "Y" :
          this_b.append( ColouredString( "░" , "p" ) )
    b[box] = this_b
  
  # center is X with the colour of the cell, unless the cell is empty
  if "Y" in cell_state.keys() :
    c[8] = ColouredString( b["Y"][int(reso["Y"]/2)], "p" )
  elif "X" in cell_state.keys() :
    c[8] = ColouredString( b["X"][int(reso["X"]/2)], "r" )
  elif "Z" in cell_state.keys() :
    c[8] = ColouredString( b["Z"][int(reso["Z"]/2)], "b" )
  
  b["X"][int(reso["X"]/2)] = c[8] # The center will be the ninth element of c instead

  # Declare and construct the lines.
  lines = []
  if cell_state=={"II":1.0} :
    for _ in range(11) :
      lines.append( "                       "+right )
  else :
    lines.append( "      .·  "+c[0]+"  ·.        "+right )
    lines.append( "   "+c[7]+"˙     "+b["Z"][8]+"     ˙"+c[1]+"     "+right )
    lines.append( "  ·       "+b["Z"][7]+"    "+b["Y"][11]+b["Y"][12]+" ·    "+right )
    lines.append( " ·        "+b["Z"][6]+"  "+b["Y"][9]+b["Y"][10]+"    ·   "+right )
    lines.append( "          "+b["Z"][5]+""+b["Y"][7]+b["Y"][8]+"          "+right )
    lines.append( ""+c[6]+" "+"".join(b["X"])+" "+c[2]+"  "+right )
    lines.append( "        "+b["Y"][4]+b["Y"][5]+""+b["Z"][3]+"            "+right )
    lines.append( " ˙    "+b["Y"][2]+b["Y"][3]+"  "+b["Z"][2]+"        ˙   "+right )
    lines.append( "  · "+b["Y"][0]+b["Y"][1]+"    "+b["Z"][1]+"       ·    "+right )
    lines.append( "   "+c[5]+".     "+b["Z"][0]+"     ."+c[3]+"     "+right )
    lines.append( "      ˙·  "+c[4]+"  ·˙        "+right )
  lines.append( bottom + right )
  
  return lines

def MakeGrid ( state, shown_qubit, active_qubit, bloch ) :

  #  DESCRIPTION:
  #      The inputs describe what the grid is doing. This function puts all that information together to actually make the grid.
  #  INPUT:
  #      {String: Float}    state   Full two qubit state. Needs entries for XI, ZI, IZ, IX, XX, XZ, ZX, ZZ and YY
  #      Int     shown_qubit     If this is 0 or 1, only the two boxes of that qubit are shown. Otherwise, all are shown.
  #      Int     active_qubit  If this is 0 or 1, the diagonals are straightened according to their function for this qubit. Otherwise they remain diagonal.
  # Bool    bloch         Whether or not to display Bloch circles for the qubit specified above
  #  OUTPUT:
  #      [String]    grid_lines   An array of strs that represent the grid
  
  cells = { "XI":[], "ZI":[], "XX":[],"XZ":[],"ZX":[],"ZZ":[],"YY":[],"II":[], "IX":[], "IZ":[] }
  
  # determine which cells behave in which way (I is blank, B is Bloch circle, X and Z are horizontal and vertical boxes and Y are diagonal)
  grid_lines = []
  cell_types = {}
  if bloch :
    if shown_qubit==0 :
      cell_types = {"I":["II","ZI","XX","XZ","ZX","ZZ","YY","IX","IZ"],"X":[],"Y":[],"Z":[],"B":["XI"]} # shown_qubit is used as active qubit
    elif shown_qubit==1 :
      cell_types = {"I":["II","XI","ZI","XX","XZ","ZX","ZZ","YY","IZ"],"X":[],"Y":[],"Z":[],"B":["IX"]} # shown_qubit is used as active qubit
    else :
      if active_qubit==0 :
        cell_types = {"I":["II","ZI","ZX","ZZ"],"X":["IX"],"Y":[],"Z":["IZ"],"B":["XI","XX","XZ"]}
      elif active_qubit==1 :
        cell_types = {"I":["II","IZ","XZ","ZZ"],"X":["XI"],"Y":[],"Z":["ZI"],"B":["IX","XX","ZX"]} # these are the same as above but with strs reversed
      else :
        print("Error: A valid qubit must be chosen to display a Bloch circle")
  else :
    if shown_qubit==0 :
      cell_types = {"I":["II","XX","XZ","ZX","ZZ","YY","IX","IZ"],"X":["XI"],"Y":[],"Z":["ZI"],"B":[]}
    elif shown_qubit==1 :
      cell_types = {"I":["II","XI","ZI","XX","XZ","ZX","ZZ","YY","IX","IZ"],"X":["IX"],"Y":[],"Z":["IZ"],"B":[]}
    else :
      # Y for diagonal boxes, since there is no active qubit
      cell_types = {"I":["II"],"X":["XI","IX","XX"],"Y":["XZ","ZX"],"Z":["ZI","IZ","ZZ"],"B":[]}

  # make blank cell
  for cell in cell_types["I"] :
    if cell=="II" :
      cells[cell] = MakeCell( {"II":1.0} )
    else :
      cells[cell] = MakeCell( {} )

  # make cells with horizontal and vertical boxes
  for cell_type in ["X","Z"] :
      for cell in cell_types[cell_type] :
          cells[cell] = MakeCell( { cell_type: state[cell] } )

  # make cells with diagonal boxes
  for cell in cell_types["Y"] :
    if active_qubit in [0,1] :
      index = active_qubit
      cells[cell] = MakeCell( { str(cell[index]):state[cell] } ) # qubit dependent cell type is used
    else :
      cells[cell] = MakeCell( { "Y":state[cell] } ) # same as in X,Z loop above

  # make cells with Bloch circle
  for cell in cell_types["B"] :
    index = (1-active_qubit)
    if active_qubit==0 :
      cells[cell] = MakeCell( { "X":state["X"+str(cell[index])], "Z":state["Z"+str(cell[index])] } )
    else :
      cells[cell] = MakeCell( { "X":state[str(cell[index])+"X"], "Z":state[str(cell[index])+"Z"] } )
  
  for l in range(12) :
      grid_lines.append( cells["II"][l] + cells["ZI"][l] + cells["XI"][l] )
  for l in range(12) :
      grid_lines.append( cells["IZ"][l] + cells["ZZ"][l] + cells["XZ"][l] )
  for l in range(12) :
      grid_lines.append( cells["IX"][l] + cells["ZX"][l] + cells["XX"][l] )

  return grid_lines

def PrintScreen ( message, level, intro, program, state, shown_qubit, active_qubit, bloch, allowed_gates, required_gates ) :

  print("\n"*3)

  # set up the screen: job 1
  # text at the top
  ClearScreen ()
  print("\nLevel "+str(level+1)+"\n")
  for line in intro[level] :
    print("> " + line + "...")

  if program != [] :
    print("\nYour QISKit program so far\n")
    for line in program :
      print(line)
    print("\n")

  # set up the screen: job 2
  # the grid
  print("\n")
  grid_lines = MakeGrid( state, shown_qubit, active_qubit, bloch )
  for line in grid_lines :
    print("   "+line)

  # set up the screen: job 3
  # state allowed gates
  for qubit in allowed_gates.keys() :
    gate_list = ""
    for gate in allowed_gates[qubit].keys() :
      if required_gates[qubit][gate] > 0 :
        gate_list += "   "+gate+" (use exactly "+str(required_gates[qubit][gate])+" times)"
      elif allowed_gates[qubit][gate]==0:
        gate_list += "  "+gate
    if gate_list!="" :
      if qubit=="both" :
        print("\nAllowed two qubit operations:")
      else :
        print("\nAllowed operations for qubit " + qubit + ":")
      print(gate_list)

  return input("\n"+message+"\n")