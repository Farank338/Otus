def print_board(number:int):
    if number is None: return 

    board=[]
    for x in range(8):
        arr=[]
        for y in range(8):
            arr.append(0)
        board.append(arr)

    number_temp=number
    for x in range(8):
        for y in range(8):
            board[x][y]=0
            board[x][y]=number_temp&0b1 
            
            # print(number_temp&0b1,end=' ')
            number_temp=number_temp>>1
        # print()    
    # print()
    for x in reversed(range(8)):
        for y in range(8):
            print(board[x][y],end=' ')   
        print()    
    print()


def king_moveset(king_pos):
    king_pos_orig=king_pos
    king_pos=\
      king_pos<<1<<8|king_pos<<8 |king_pos>>1<<8 \
    | king_pos << 1 |             king_pos >>1   \
    | king_pos>>1>>8|king_pos>>8 |king_pos<<1>>8


    if king_pos_orig & 72340172838076673!=0:   
        return king_pos & 9187201950435737471
    if king_pos_orig & 9259542123273814144!=0:
        return king_pos & 18374403900871474942
    return king_pos
        
def horse_moveset(horse_pos):
    horse_pos_orig=horse_pos
    horse_pos=\
      horse_pos<<2<<8|horse_pos<<1<<8<<8|horse_pos>>1<<8<<8 |horse_pos>>2<<8 \
    | horse_pos>>2>>8|horse_pos>>1>>8>>8|horse_pos<<1>>8>>8 |horse_pos<<2>>8 \


    if horse_pos_orig & 217020518514230019!=0:   
        return horse_pos & 4557430888798830399
    if horse_pos_orig & 13889313184910721216!=0:
        return horse_pos & 18229723555195321596
    return horse_pos
        

def moveset(figures_pos:int,horse:bool):
    figures_moves=0
    figure_pos=1
    pos=0
    
    while figures_pos>0:
        if figures_pos&0b1:
            figure_pos=figure_pos<<pos
            if horse==False:
                figures_moves=figures_moves|king_moveset(figure_pos)   
            else:
                figures_moves=figures_moves|horse_moveset(figure_pos)   
            figures_pos=figures_pos>>1
            pos=pos+1
            figure_pos=1
        else:
            pos=pos+1
            figures_pos=figures_pos>>1
    return figures_moves 
        

def calc_bit(bits:int,variant:bool):
    count=0
    if variant==True:        
        while bits!=0:
            if bits&0b1:
                count=count+1
            bits=bits>>1
        return count
    else:       
        while bits!=0:
            bits=bits&(bits-1)
            count=count+1
        return count


horse=moveset(18014398509482496,horse=True)
king=king_moveset(18014398509482496)
print_board(horse)
print()
print_board(king)
print(calc_bit(horse,True),calc_bit(king,True))
print(calc_bit(horse,False),calc_bit(king,False))

# check for auto test
import os
path=r'HW5/0.BITS/1.Bitboard - Король'
test={}
for file in os.listdir(path):
    if file.endswith(".in"):
        with open(os.path.join(path, file)) as f:
            a=[]
            a.append(int(f.readline()))
            test[file[:-3]]=a

for file in os.listdir(path):
    if file.endswith(".out"):
        with open(os.path.join(path, file)) as f:     
            a=test[file[:-4]] 
            a.append(int(f.readline()))
            a.append(int(f.readline()))
            test[file[:-4]]=a
            
for k in test:
    i=test[k]
    number=1<<i[0]
    
    res_posible=moveset(number,horse=False)
    bits=calc_bit(res_posible,True)
    if res_posible==i[2] and bits==i[1]:
        print("test",k,"passed, input",i[0],"expected",i[1],i[2],"result",bits,res_posible)     
    else:
        print("test",k,"NOT passed, input",i[0],"expected",i[1],i[2],"result",bits,res_posible)    