
def move(state, player):
    ask = isPossibleTo()
    if (isContact()) :#contact with opponent
        if (ask.moveOpponentMarbleOutOfTheBoard()):
            if (manyContact()):
                moves=computeMovesKeepingMaxNeighbour()# Compute wich valid move will keep the most neighbour and move out opponnent marble with maximum marbles to do it

                validMoves=ValidMove(Moves)               # return valid possibilites
                outMove=chooseMove(validMove)
            else :
                move=computeMoveWithMaxMarble()
                outmove=ValidMoves(move)    
        else : #If (!no possible to move opponnent marble out of the board) :
            if (manyContact()):
                if loseaMarbleofMyself():
                    if MyMarblecanEscape():#Available position & no neighbour will out me
                      gotoNeighbourMarble()#close as possible
                    else :
                        #marble is lost 
                        pass
                else :
                    if AllMyMarbleareNeighbour():
                        if (ask.moveOpponentMarbleCloseToTheBorder()):
                            #move it 
                            movemarble(position,numbersofmarble=max,direction=tochoose)
                    
                        else :
                            if ask.moveaMarbleNexttoAllie():
                                #move it 
                                movemarble(position,numbersofmarble=max,direction=tochoose)
                            else :
                                if ask.moveaMarble():
                                    movemarble(position,numbersofmarble=max,direction=tochoose)
                                else :
                                    pass
                
                    else:
                        if ask.moveaMarbleNexttoAllie():
                            #move it 
                            movemarble(position,numbersofmarble=max,direction=tochoose)
                    
                        else :
                            marbleonborder = selectmarbleclosetotheborder()
                            if marbleonborder == freetomove:
                                #move it to the center 
                                movemarble(position,numbersofmarble,direction=center)
                            else :
                                if othermarbleavailable():
                                    selectOtherMarble()
                                    #moveit
                                    movemarble(position,numbersofmarble,direction)
                                else :
                                    pass
            else :
                if AllMyMarbleareNeighbour():
                    if (ask.moveOpponentMarbleCloseToTheBorder()):
                        #move it 
                        movemarble(position,numbersofmarble=max,direction=tochoose)
                    
                    else :
                        if ask.moveaMarbleNexttoAllie():
                            #move it 
                            movemarble(position,numbersofmarble=max,direction=tochoose)
                        else :
                            if ask.moveaMarble():
                                movemarble(position,numbersofmarble=max,direction=tochoose)
                            else :
                                pass
                else:
                    if ask.moveaMarbleNexttoAllie():
                        #move it 
                        movemarble(position,numbersofmarble=max,direction=tochoose)
                    
                    else :
                        marbleonborder = selectmarbleclosetotheborder()
                        if marbleonborder == freetomove:
                            #move it to the center 
                            movemarble(position,numbersofmarble,direction=center)
                        else :
                            if othermarbleavailable():
                                selectOtherMarble()
                                #moveit
                                movemarble(position,numbersofmarble,direction)
                            else :
                                pass
                        
    else :
        if (ask.moveManyMarbles()):
            moves = computeMovesKeepingMaxNeighbour() # return many possibilites
            validMoves=ValidMove(Moves)               # return valid possibilites
            outMove=chooseMove(validMove)             # out move 
        else :
            if ( ask.aMarblesNextToAllies()):
                moves=computeSingleMarbleMove()       # return many possibilities
                validMoves=ValidMove(Moves)               # return valid possibilites
                outMove=chooseMove(validMove)             # out move
            else :
                outMove=[(None,None)]


#try go contact with most neighbour of my color
#strategies:
#When contact with opponent
#Yes : -Is it possible de move opponenent marble out of the board ? 
#   -Yes : If different contact :
#            Yes : Compute wich valid move will keep the most neighbour and move out opponnent marble with maximum marbles to do it
#            No : Move out opponnent marble with maximum marbles to do it
#   -No : If different contact :
#           Yes : Will I lost a marble ?(Do I get a marbles next to the boarder and 2 opponent align with my marble)
#                   Yes : Can I escape ? ( Available position & no neighbour will out me)
#                           Yes : Try to go next to a neighbour select the marbles with the most marbles neighbours 'allies'
#                           No : Marble is lost go to No
#                   No : Do all my marbles are neighboor ?
#                           Yes : Can I move opponents marbles close to the border?
#                                    Yes : I do it with the maximum marble
#                                    No : Can I move a marble next to allie marble ?
#                                           Yes : do it 
#                                           No : Can I move a marble ? 
#                                                    yes : move marble
#                                                    no : pass 
#                            No : Can I move many marbles next to alies marble ? (all free to move)
#                                   yes : Do it with the maximum marble
#                                   no : Choose a marble the closest from border to move :
#                                           is it free to move ? :
#                                               yes : move it to the center
#                                                no : next marble if none pass                          
#           No :  Do all my marbles are neighboor ?
#                           Yes : Can I move opponents marbles close to the border?
#                                    Yes : I do it with the maximum marble
#                                    No : Can I move a marble next to allie marble ?
#                                           Yes : do it 
#                                           No : Can I move a marble ? 
#                                                    yes : move marble
#                                                    no : pass 
#                            No : Can I move many marbles next to alies marble ? (all free to move)
#                                   yes : Do it with the maximum marble
#                                   no : Choose a marble the closest from border to move :
#                                           is it free to move ? :
#                                               yes : move it to the center
#                                                no : next marble if none pass
#No :
#   Is it possible to move many marble (allies) ?
#        Yes : random of moves for move  with maximum number of marble keeping most neigbour 
#        No  : Can I move a marble next to allies marbles :
#                Yes : move  
#                No : Can I move a marble ?
#                        Yes : move 
#                        No : pass
