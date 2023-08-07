

# Comment lol

import os #imports 'package' os and all of its functions --> refernce by os.FUNCTION()
import id90
import process

#variable a is an empty list/Array
a = [] 

#variable d is an empty Array
d = {}

#CREATE LIST OF HEADERS
header = open('source\\header.txt','r').read().replace('\n','')
headers = [h for h in header.split('|')]

#function main()
def main():
    print('CODE BELOW HERE :D :D : D ')
    # This is where you want to writ your code. YOu want the pair of main() and if __name__ in each file (idk why, just do ig)


    
def add_files(file_count, path):

    sets = id90.Set(file_count)
    sets.write_txts(path)

def clean(str_path: str):

    txt_files = [str_path+'\\'+f for f in os.listdir(str_path) if os.path.isfile(os.path.join(str_path,f))]

    for file in txt_files:
        print(file)    
        process.go(file, headers)


    


#if statement - if the name of the file is equal to (==) the name of the MAIN file (OpenFile)
if __name__ == '__main__':

    gen1_path = 'source\\id90_gen1'
    gen2_path = 'source\\id90_gen2'
    gen3_path = 'source\\id90_gen3'
    gen4_path = 'source\\id90_gen4'
    #add_files(10,gen4_path)
    #mypath = 'source\\id90_gen1'

    clean(gen4_path)

    #main()




