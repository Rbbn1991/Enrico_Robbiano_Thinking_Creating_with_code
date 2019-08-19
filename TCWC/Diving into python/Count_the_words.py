file=open('count_exercice.txt')
original=file.read()
file.close()

# start by cleaning the file #

parsed=original.replace('.',"").replace('-'," ").replace(',',"").replace('!',"").replace('\n'," ").strip()

world_count=len(parsed.split(' '))

print(world_count)

text_modified=original.replace('is','should be').upper()

print(text_modified)
