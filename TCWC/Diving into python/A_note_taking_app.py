import glob
import pandas as pd
directory=list(glob.glob("*.txt"))

n_files=len(directory)



i=0


print( "what to you want to do?")
print('Press 1 to add a note')
print('Press 2 to search a note')
order=input()

if order=='1':
    print('Note Name:')
    note_name=input()
    note_name=note_name+".txt"
    print('Note content:')
    note_content=input()

    file=open(note_name,'w')
    file.write(note_content)
    file.close()

if order=='2':
    print('what are you searching?')

    search_term=input()
    while i!=n_files:
        search=0
        text_file=open('{0}'.format(directory[i]))
        content=text_file.read()
        search=content.find(search_term)
        
        i=i+1
        
        #print(content)
        #print("")
        
        
        if search>=0:
            print('-----')
            
            print(content)
            print('-----')

if (order !='1' and  order !='2'):
    
    print('Exiting the program')
    quit()