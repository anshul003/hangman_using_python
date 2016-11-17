# hangman game

def hangman(argument):
	switcher = {
        1: """
             .  ___  .
             . (___) .
             .   |   .
          """,
        2: """
             .  ___  .
             . (___) .
             .   |   .
             .  /    .
             . /     .
          """,
        3: """
            .  ___  .
            . (___) .
            .   |   .
            .  /|   .
            . / |   .
            """,
        4:"""
            .  ___  .
            . (___) .
            .   |   .
            .  /|\  .
            . / | \ .
            """,
        5:"""
            .  ___  .
            . (___) .
            .   |   .
            .  /|\  .
            . / | \ .
            .  /    .
            . /     .
            """,
        6:"""
            .  ___  .
            . (___) .
            .   |   .
            .  /|\  .
            . / | \ .
            .  / \  .
            . /   \ .
            """
	}
	return switcher.get(argument,"")

list_easy = ['bake','make','cook','india','fool','break','eat','drink','heal','dark']
list_medium = ['statement','motivation','inspiration','impulse','language','dreamers','maverick','trendsetter','trailblazer','independence']
list_hard = ['accoutrements','circumlocution','idiosyncratic','magnanimous','parsimonious','perfidiousness','remunerative','sesquipedalian','superabundant','unencumbered']

print "Choose your level: 1.hard 2.medium 3.easy"
level = raw_input()

from random import randint
random_num = randint(0,9)

if(level=='1'):
	print "SO YOU THINK YOU KNOW A LOT! WE'LL SEE!"
	a = list_hard[random_num]

elif(level=='2'):
	print "PLAYING THE GAME SAFE! LET US SEE HOW GOOD YOU ARE!"
	a = list_medium[random_num]

elif(level=='3'):
	print "HAVE SOME CONFIDENCE AND AT LEAST GO TO THE MEDIUM LEVEL!"
	a = list_easy[random_num]

else:
	print "Read the instructions carefully and select between 1,2 and 3"
	import sys
	sys.exit()

print "KEEP ENTERING A CHARECTOR! YOU HAVE 7 ATTEMPTS BEFORE HANGMAN GETS COMPLETE"

list(a)
n=len(a)
b=range(n)
for i in range(n):
	b[i]="_"

counter=0
the_ender=0

while (counter<6):
	c=raw_input()
	count=0
	for j in range(n):
		if(c==a[j]):
			b[j]=c
			count+=1
        print b
#        print count
        if (count==0):
            counter+=1
#            print counter
            print hangman(counter)

	the_ender=0;
	for j in range(n):
		if(b[j]=='_'):
			the_ender+=1

	if(the_ender==0):
		print "CONGRATULATIONS! YOU WON!!!"
		break


if (counter==6):
	print "You lose. The word was"
