def print_depth(data):
    lines=data
    level = 0
    for i in range(len(lines)):
        line = lines[i].split()
        for j in range(len(line)):
            if(line[j]=="{"):
                level = level + 1
            x = line[j].split(':')
            if(len(x)>1):
                key = x[0].replace('“','')
                key = x[0].replace('”','')
                print(key," ", level)
                
                
with open('input.txt') as f:
    lines = f.readlines()
print_depth(lines)
