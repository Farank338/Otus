def lucky_2():
    k=0
    count=[]
    for i1 in range(10):
        for i2 in range(10):
            if i1==i2:
                k=k+1
                count.append(1)
    return k,count

def lucky(N):
    if N<=2:
        return lucky_2()
    else:
        # выделим таблицу заполненную 0
        size=(N-1)*9+1
        array=[]
        for i in range(10):
            array.append([0]*size)
        
        # запросим результаты с N-1
        res=lucky(N-1)
        sum=res[0]
        array_count=res[1]
        # print(sum,array_count)
        # теперь нужно со сдвигом в 1 добавить вернувшийся массив в новый
        shift1=0
        for i in range(10):
            shift2=0
            for j in array_count:                
                array[i][shift1+shift2]=j
                shift2=shift2+1
            shift1=shift1+1
        count=[0]*size
        for i in range(size):
            for j in range(10):
                count[i]=count[i]+array[j][i]
        sum=0
        for i in count:
            sum=sum+i*i
        return sum,count
        
    
def calc_lucky(N):
    return lucky(N+1)[0]
    
if __name__ == "__main__":    
    print(1,calc_lucky(1))
    print(2,calc_lucky(2))
    print(3,calc_lucky(3))
    print(4,calc_lucky(4))
    print(5,calc_lucky(5))
    print(6,calc_lucky(6))
    print(7,calc_lucky(7))
    print(8,calc_lucky(8))
    print(9,calc_lucky(9))
    print(10,calc_lucky(10))