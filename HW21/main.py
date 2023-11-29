import sys
if __name__ == "__main__":
    if len(sys.argv)<4 or ('decode' not in sys.argv[1] and 'encode' not in sys.argv[1]):
        print('Usage')
        print('\tdecode <in_path> <out_path>')
        print('\tencode <in_path> <out_path>')
        exit(1)

    with open(sys.argv[2], 'rb') as in_file:
        with open(sys.argv[3], 'wb') as out_file:
            if 'encode' in sys.argv[1]:
                data_in=in_file.read(1)
                byte=-1
                count=0
                while len(data_in)!=0:
                    
                    if data_in[0]==byte:
                        count=count+1
                        if count==255:
                            out:bytearray=[byte,count]
                            out_file.write(bytes(out))
                            byte=data_in[0]
                            count=1
                    if data_in[0]!=byte:
                        if byte!=-1:
                            out:bytearray=[byte,count]
                            out_file.write(bytes(out))
                        byte=data_in[0]
                        count=1
                        
                        

                    if byte==-1:
                        byte=data_in[0]
                        count=1

                    data_in=in_file.read(1)

            if 'decode' in sys.argv[1]:
                data_in=in_file.read(2)
                while len(data_in)!=0:
                    for i in range(data_in[1]):
                        out:bytearray=[data_in[0]]
                        out_file.write(bytes(out))
                    
                    data_in=in_file.read(2)