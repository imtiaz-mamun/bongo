class Person(object):
    def __init__(self, first_name, last_name, father):
        self.first_name = first_name
        self.last_name = last_name
        self.father = father
person_a = Person("User", "1", "")
person_b = Person("User", "2", person_a)
def print_depth(data):
    print("Current Parameter and Level:")
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
    my_data = lines
print_depth(lines)
def add_my_object(data, add_obj,add_level,keys,val):
    linesa=data
    level = 0
    for i in range(len(linesa)):
        linea = linesa[i].split()
        for j in range(len(linea)):
            if(linea[j]=="{"):
                level = level + 1
                if(level==add_level):
                    for k in range(len(keys)):
                        if(k==0):
                            linesa[i] = linesa[i].append('\n“')
                            linesa[i] = linesa[i].append(add_obj)
                            linesa[i] = linesa[i].append('”')
                            linesa[i] = linesa[i].append(':')
                            linesa[i] = linesa[i].append('{\n')
                            linesa[i] = linesa[i].append('“')
                            linesa[i] = linesa[i].append(keys[k])
                            linesa[i] = linesa[i].append('”')
                            linesa[i] = linesa[i].append(':')
                            linesa[i] = linesa[i].append(val[k])
                            linesa[i] = linesa[i].append(',')
                            print(linesa)
                        if(k==len(keys)-1):
                            linesa[i] = linesa[i].append('\n}')
                            
                        else:
                            linesa[i] = linesa[i].append('“')
                            linesa[i] = linesa[i].append(keys[k])
                            linesa[i] = linesa[i].append('”')
                            linesa[i] = linesa[i].append(':')
                            linesa[i] = linesa[i].append(val[k])
                            if(k+1!=len(keys)-1):
                                linesa[i] = linesa[i].append(',')
    print_depth(linesa)
                
add_obj = input("\nObject Addition to the dictionary:\nInsert Object Name?")

if(add_obj):
    add_param_key = "y"
    count=0
    while(add_param_key=="y" or add_param_key=="Y"):
        add_param_key = input("Add new parameter?(Y/N)")
        if(add_param_key=="y" or add_param_key=="Y"):
            print("yes")
            keys.append(input("Parameter name?"))
            val.append(input("Parameter value?"))
            count = count + 1;
        if(add_param_key=="n" or add_param_key=="N"):
            add_level = input("Insert Object level?")
            add_my_object(my_data,add_obj, add_level,keys,val)
            break
        else:
            add_param_key = input("Add new parameter?(Y/N)")
