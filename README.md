# AI Abalone Project
Antoine Scaviner 20520

Matthieu Faget 20517


## **1.Programming language :** 

Python 


## **2. Libraries :**  

- *socket :*  

- *jsonNetwork :*  

- *threading :*

- *sys :*

- *json :*

- *time :* 

- *collections :*

- *random :* 

- *copy :* 

## **3. AI strategy :**  
- *First, Ai take the location advantage ! :* all the marbles go to the center of the board and stay together as possible as they can

- *Second, Ai push the marbles ! :* the Ai try to push the marble near the boarderline of the board,
              from the center to the second crown and form the second crown to the last crown(boarderline)

- *Thirdly, Ai attack ! :* The Ai try to push out the opponent marbles as soon as possible even if there is other moves available

- *Thourthly, Ai defend ! :* if a allie marble is on the boarderline in alignment with opponents marbles,
                        The Ai try to make escape the marble 

## **4. How to run a Ai game :**  

- *Firstly :*  open the repository "PI2CChampionshipRunner" and run the "server.py" file with the command : 'python server.py abalone'

- *Secondly :* run the 'client.py' file to subscribe the AI with the command: 'python client.py 3001 Toto1'    

            3001 is a port number that can be change but, it can't be 3000 because server use it already.
            Toto1 is a Name and can be change 

- *Thirdly :* subscribe your AI or run  the 'client2.py' file to subscribe the second AI with the command: 'python client2.py 3002 Toto2'    

- *Then :* the game start !
