import hagman_art
import words_list
import os
clear = lambda: os.system('cls')

import random
#variables
word_list = words_list.word_list
stages = hagman_art.stages

life = len(stages);
lines = [];
game_over = False;

logo = hagman_art.logo

print(logo)

random_choice = random.choice(word_list);
size = len(random_choice);

for str in random_choice:
    lines += "_";


def display_lines(lines):
    for l in lines:
        print(l,end="");

game_over = False;
while not game_over:
    if life > 0:
        display_lines(lines)
        print()
        letter = input("Guess a letter please : ").lower();
        clear()
        for i in range(size):
            if letter == random_choice[i]:
                lines[i] = letter;

        if letter not in random_choice:
            life -=1;
            print(stages[life])

        if "_" not in lines:
            print("You Win");
            word_list.remove(random_choice);
            quit = input("You want Play again Y(es)/N(o)").lower();

            if quit == 'n':
                print("All right good playing, see you next time");
                print("exiting...")
                game_over = True;
            elif quit == 'y':
                life = 6;
                lines = [];
                count = 0;
                random_choice = random.choice(word_list);
                print(random_choice);
                size = len(random_choice);
                for i in random_choice:
                    lines += "_";
                    count += 1;
    else:
        print("GAME OVER")
        quit = input("You want Play again Y(es)/N(o)").lower();
        if quit == 'n':
            print("All right good playing, see you next time");
            print("exiting...")
            game_over = True;
        elif quit == 'y':
            life = 6;
            lines = [];
            count = 0;
            random_choice = random.choice(word_list);
            print(random_choice);
            size = len(random_choice);
            for i in random_choice:
                lines += "_";
                count += 1;

    #easy way
    #if lines.count("_") == 0:
        #print("You Win");