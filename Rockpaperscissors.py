"""
A simple Rock, Paper and Scissors game.
"""

from random import randint
import collections
from time import sleep      # To create suspense while displaying results ;p

stats = {}

def p_wins():
"""
Prints a message if player wins
"""
    print("\n"+Name + " wins !\n")

def c_wins():
"""
Prints a message if computer wins
"""
    print("\nComputer wins !\n")

def show_stats():
"""
Shows the statistics of all the rounds played in a particular session
"""
    print("\n\n")
    sorted_stats = collections.OrderedDict(sorted(stats.items()))
    
    for rnd,win in sorted_stats.items():
        print(rnd+" -> "+win)

    print("\nTotal ::\n\t"+Name+" :: "+str(decide_winner.p_cnt)+ ' - ' +str(decide_winner.c_cnt)+" :: Computer")

def decide_winner(player,computer,i):
""""
Decides who wins the game
"""
    global plc
    global ccc
    if player == computer :
        print("\nRound :: {0}\n\tIt's a tie !!\n".format(i))
        stats["Round "+str(i)] = "Tie"
        return
    
    elif player == 1 and computer == 3:
        decide_winner.p_cnt += 1
        p_wins()
        stats["Round "+str(i)] = Name

    elif player == 2 and computer == 1:
        decide_winner.p_cnt += 1
        p_wins()
        stats["Round "+str(i)] = Name

    elif player == 3 and computer == 2:
        decide_winner.p_cnt += 1
        p_wins()
        stats["Round "+str(i)] = Name

    else :
        decide_winner.c_cnt += 1
        c_wins()
        stats["Round "+str(i)] = "Computer"

    plc = decide_winner.p_cnt
    ccc = decide_winner.c_cnt
		
    print("\nRound :: {0}\n\t{1} : {2}\n\tComputer : {3}\n".format(i,Name,decide_winner.p_cnt,decide_winner.c_cnt))
decide_winner.p_cnt = 0
decide_winner.c_cnt = 0   

def grande_total():
"""
Shows the final result concluded from overall games played in a session.
"""
    print ('\n\t\tFINAL RESULTS::\n')
    
    if decide_winner.p_cnt > decide_winner.c_cnt:
        print("\t\t"+Name+" WINS !!")
    elif decide_winner.c_cnt > decide_winner.p_cnt:
        print("\t\tComputer WINS !!")
    else :
        print("\t\tIt's a tie !!")
    

def main():
    global Name
    Name = input("What's your name ? ")

    ub = tc = int(input("Enter the number of turns you want to play, "+Name+" :: "))
    rps = {"Rock":1, "Paper":2, "Scissor":3}

    global p_cnt
    global c_cnt
    p_cnt=0
    c_cnt=0
    
    while tc:

        p_choice = input("Select : Rock /Paper /Scissor ::\n"+Name+" :: ")

        if p_choice != p_choice.title():
            p_choice = p_choice.title()
            
        for p_k,p_v in rps.items():
            if p_choice == p_k:
                p_val = p_v


        c_val = randint(1,3)
        for c_k,c_v in rps.items():
            if c_val == c_v :
                c_choice = c_k

        print("Computer :: " + c_choice)
        sleep(1)
        counter = decide_winner(p_val,c_val,ub-tc+1)

        tc -= 1

    grande_total()
    show = int(input("\n\nPress 1. to show stats. (Pressing any other number would cause the program to terminate) :: "))
    if show == 1:
        show_stats()

if __name__==main():
    main()
input()
