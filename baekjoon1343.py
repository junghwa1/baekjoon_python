board=input()
result_board=""

AB=board.split('.')

for once in AB:
    count=once.count('X')
    if count%2==1:
        print('-1')
        break
    if count//4:
        result_board=result_board+"AAAA"*(count//4)
    if count%4==2:
        result_board=result_board+"BB"
    result_board=result_board+'.'

if count%2!=1:
    print(result_board[:-1])
