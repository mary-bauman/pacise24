# B - Bowling Score Sheet

A single bowling game consists of ten frames. The object in each frame is to
roll a ball at ten bowling pins arranged in an equilateral triangle and to knock
down as many pins as possible. For each frame, a bowler is allowed a maximum of
two rolls to knock down all ten pins. If the bowler knocks them all down on the
first attempt, the frame is scored as a strike. If the bowler does not knock
them down on the first attempt in the frame the bowler is allowed a second
attempt to knock down the remaining pins. If the bowler succeeds in knocking the
rest of the pins down in the second attempt, the frame is scored as a spare.

The score for a bowling game consists of sum of the scores for each frame. The
score for each frame is the total number of pins knocked down in the frame, plus
bonuses for strikes and spares. In particular, if a bowler scores a strike in a
particular frame, the score for that frame is ten plus the sum of the next two
rolls. If a bowler scores a spare in a particular frame, the score for that
frame is ten plus the score of the next roll. If a bowler scores a strike in the
tenth (final) frame, the bowler is allowed two more rolls. Similarly, a bowler
scoring a spare in the tenth frame is allowed one more roll. The maximum
possible score in a game of bowling (strikes in all ten frames plus two extra
strikes for the tenth frame strike) is 300.

## Input
The input will consist of a sequence of bowling game scores. Each line will
contain the scores for a single game, with the scores for each roll of the ball
separated by a single space. The score for a single roll will be represented by
a single character -- either a number indicating the number of pins knocked
down, a '/' for a spare or a 'X' for a strike.

## Output
Your program should output the total game score for each game in the input. The
order of the scores on the output should correspond to the order of the games on
the input. Each line should follow the format "Game {i}: {score}" where i starts
at 1.

## Sample
Input:
```
1 0 1 / 2 2 X 3 3 X 1 / 3 / X 1 2
1 0 1 / 2 2 X 3 3 X 1 / 3 / 1 / X 8 0
1 0 1 / 2 2 X 3 3 X 1 / 3 / 1 / 8 / 9
```

Output:
```
Game 1: 108
Game 2: 121
Game 3: 120
```
