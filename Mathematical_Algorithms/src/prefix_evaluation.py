"""
Output:

Enter a Prefix Equation (space separated) = + 8 ^ 6 2
 Symbol  |    Action    | Stack
-----------------------------------
       2 | push(2)      | 2
       6 | push(6)      | 2,6
         | pop(6)       | 2
         | pop(2)       |
       ^ | push(2^6)    | 64
       8 | push(8)      | 64,8
         | pop(8)       | 64
         | pop(64)      |
       + | push(64+8)   | 72

	Result =  72
"""

import operator as op

def Solve(Postfix):
    Stack = []
    Div = lambda x, y: int(x/y)     # integer division operation
    Opr = {'^':op.pow, '*':op.mul, '/':Div, '+':op.add, '-':op.sub}     # operators & their respective operation

    # print table header
    print('Symbol'.center(8), 'Action'.center(12), 'Stack', sep = " | ")
    print('-'*(30+len(Postfix)))

    for x in Postfix:
        if( x.isdigit() ):          # if x in digit
            Stack.append(x)         # append x to stack
            print(x.rjust(8), ('push('+x+')').ljust(12), ','.join(Stack), sep = " | ")      # output in tabular format
        else:
            B = Stack.pop()             # pop stack
            print("".rjust(8), ('pop('+B+')').ljust(12), ','.join(Stack), sep = " | ")      # output in tabular format

            A = Stack.pop()             # pop stack
            print("".rjust(8), ('pop('+A+')').ljust(12), ','.join(Stack), sep = " | ")      # output in tabular format

            Stack.append( str(Opr[x](int(A), int(B))) )         # evaluate the 2 values poped from stack & push result to stack
            print(x.rjust(8), ('push('+A+x+B+')').ljust(12), ','.join(Stack), sep = " | ")      # output in tabular format

    return int(Stack[0])

def Convert(Prefix):
    Prefix.reverse()        # Reverse  the Prefix Equation
    return Solve(Prefix)    # evaluate the reversed Prefix Equation (as a Postfix Equation)

Prefix = input("\n\nEnter a Prefix Equation (space separated) = ").strip().split(' ')
print("\n\tResult = ", Convert(Prefix))
