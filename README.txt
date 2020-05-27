How to run the N-Queen Python program
Steps:
1) Open E949F496_NQueen.py in IDLE(Python) editor
2) Click Run Module or enter 'F5' to run the program

Example-1

Enter Size of the Board i.e. n>=4: 4
*******Queen Position index start from 0********
Enter the Queen position in column -  1  :
1

Enter the Queen position in column -  2  :
2

Enter the Queen position in column -  3  :
0

Enter the Queen position in column -  4  :
3


Initial Start State of Queen positions in each column on the Board:  [1, 2, 0, 3]

----------------START STATE----------------------
['o', 'o', 'x', 'o']
['x', 'o', 'o', 'o']
['o', 'x', 'o', 'o']
['o', 'o', 'o', 'x']

-----------------OUTPUT---------------------
| o | x | o | o |
| o | o | o | x |
| x | o | o | o |
| o | o | x | o |

Example-2

Enter Size of the Board i.e. n>=4: 8
*******Queen Position index start from 0********
Enter the Queen position in column -  1  :
1

Enter the Queen position in column -  2  :
3

Enter the Queen position in column -  3  :
2

Enter the Queen position in column -  4  :
4

Enter the Queen position in column -  5  :
6

Enter the Queen position in column -  6  :
5

Enter the Queen position in column -  7  :
7

Enter the Queen position in column -  8  :
0


Initial Start State of Queen positions in each column on the Board:  [1, 3, 2, 4, 6, 5, 7, 0]

----------------START STATE----------------------
['o', 'o', 'o', 'o', 'o', 'o', 'o', 'x']
['x', 'o', 'o', 'o', 'o', 'o', 'o', 'o']
['o', 'o', 'x', 'o', 'o', 'o', 'o', 'o']
['o', 'x', 'o', 'o', 'o', 'o', 'o', 'o']
['o', 'o', 'o', 'x', 'o', 'o', 'o', 'o']
['o', 'o', 'o', 'o', 'o', 'x', 'o', 'o']
['o', 'o', 'o', 'o', 'x', 'o', 'o', 'o']
['o', 'o', 'o', 'o', 'o', 'o', 'x', 'o']

-----------------OUTPUT---------------------
| o | o | o | o | o | x | o | o |
| o | o | x | o | o | o | o | o |
| o | o | o | o | x | o | o | o |
| o | o | o | o | o | o | x | o |
| x | o | o | o | o | o | o | o |
| o | o | o | x | o | o | o | o |
| o | x | o | o | o | o | o | o |
| o | o | o | o | o | o | o | x |

Example-3

Enter Size of the Board i.e. n>=4: 5
*******Queen Position index start from 0********
Enter the Queen position in column -  1  :
1

Enter the Queen position in column -  2  :
4

Enter the Queen position in column -  3  :
2

Enter the Queen position in column -  4  :
3

Enter the Queen position in column -  5  :
0


Initial Start State of Queen positions in each column on the Board:  [1, 4, 2, 3, 0]

----------------START STATE----------------------
['o', 'o', 'o', 'o', 'x']
['x', 'o', 'o', 'o', 'o']
['o', 'o', 'x', 'o', 'o']
['o', 'o', 'o', 'x', 'o']
['o', 'x', 'o', 'o', 'o']

-----------------OUTPUT---------------------
| o | o | o | o | x |
| o | o | x | o | o |
| x | o | o | o | o |
| o | o | o | x | o |
| o | x | o | o | o |