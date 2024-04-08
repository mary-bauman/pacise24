https://lightoj.com/contest/pacise-2024/arena/problem/5519

A developer of crossword puzzles (and other similar word games) has decided to develop a mapping between every possible word with from one to twenty characters and unique integers. The mapping is very simple, with the ordering being done first by the length of the word, and then alphabetically. Part of the list is shown below.

word	number

a	1

b	2

...	...

z	26

aa	27

ab	28

...	...

snowfall	157,118,051,752

...	...

Your job in this problem is to develop a program which can translate, bidirectionally, between the unique word numbers and the corresponding words.

**Input**

Input to the program is a list of words and numbers, one per line. A number will consist only of decimal digits (0 through 9) followed immediately by the end of line (that is, there will be no commas in input numbers). A word will consist of between 1 and 12 (inclusive) lowercase alphabetic characters (a through z).

**Output**

For each word or number, output a single line containing the word, a single space, and the corresponding word number. Regardless of whether the word or number was given initially, both must be printed.

**Sample**

**Input**

29697684282993

transcendental

28011622636823854456520

computationally

**Output**

elementary 29697684282993

transcendental 51346529199396181750

prestidigitation 28011622636823854456520

computationally 232049592627851629097

