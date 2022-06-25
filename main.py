# If you want to use regex to filter out the digit lines and empty lines, you can use this:

import re
import os


PATH = "./SRT"

def getAllDir(path):
    
    return  os.listdir(path)
    


def main():


    dir_list = getAllDir(PATH)
    count = 1
    for  fl  in dir_list :

        pth =  PATH + "/" +fl 
        file = open( pth, "r")
        f = open(str(count)+".txt", "a")
        lines = file.readlines()
        file.close()

        text = ''
        for line in lines:
            if re.search('^[0-9]+$', line) is None and re.search('^[0-9]{2}:[0-9]{2}:[0-9]{2}', line) is None and re.search('^$', line) is None:
                f.write(line.rstrip('\n') + "\n")

        f.close()
        count +=1




      

    
    

main()

