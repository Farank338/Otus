# read input set and output set
from hw2_MIDDLE import calc_lucky
import os

if __name__ == "__main__":    
    path=r'A01_Счастливые_билеты\1.Tickets'
    in_arr=[]
    for file in os.listdir(path):
        if file.endswith(".in"):
            with open(os.path.join(path, file)) as f:                
                in_arr.append(int(f.readline()))
    
    out_arr=[]          
    for file in os.listdir(path):
        if file.endswith(".out"):
            with open(os.path.join(path, file)) as f:                
                out_arr.append(int(f.readline()))
                
    for i in range(len(out_arr)):
        res=calc_lucky(in_arr[i])
        if res==out_arr[i]:
            print("test",i,"passed, input",in_arr[i],"expected",out_arr[i],"result",res)     
        else:
            print("test",i,"NOT passed, input",in_arr[i],"expected",out_arr[i],"result",res)    