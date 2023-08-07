


def go(file_name: str, headers: [str]):
    #if(no_head(open(file_name,"r"))):
        #do this
    header = '|'.join(headers)
    #print('JOINED: '+header)
    with open(file_name,"r+") as file:

        content = file.read()
        content = content.replace('*|','').replace('|#|','')
        print(repr(file.read()))


        if no_head(file,headers):
            file.truncate(0)
            file.seek(0)
            file.write(header.rstrip('|') + '\n'+content)
            print ('updated - w head')
        else:
            file.truncate(0)
            file.seek(0)
            file.write(content)
            print ('updated - no head')
            

#Check for header - if empty, add
def check_head(file, headers: [str]):
    file.seek(0)
    first_row = file.readline()
    if '*|' in first_row:
        first_row = first_row.replace('*|','')
    
    vals = [fr for fr in first_row.split('|')]
    miss = [x for x in headers if not x in vals]

    if(len(miss) < len(headers)-5):
        print('yay')
    else:
        print('nay')
        

def no_head(file, headers: [str]):
    file.seek(0)
    first_line = file.readline().replace('*|','')
    vals = [v for v in first_line.split('|') if not v in headers]
    #print(vals)
    return(len(vals) > len(headers)-5)
    






    













