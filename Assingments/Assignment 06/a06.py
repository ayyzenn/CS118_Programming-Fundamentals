## IMPORTS GO HERE
import os
## END OF IMPORTS


#### YOUR CODE FOR text_count FUNCTION GOES HERE ####
def text_count(directory,filename,condition=".",char=","):
    filename=os.path.join(directory,filename)
    with open(filename,"r") as f:
        f = f.read()
        words = f.split()
        if condition==True:
            l=[]
            for i in words:
                if i.islower():
                    l.append(i)
            return len(l)
        elif char==True:
            return len(f)
        else:
            return len(words)

#### End OF MARKER

#### YOUR CODE FOR copy_lines FUNCTION GOES HERE ####
def copy_lines(input_path, output_path, lines):
    l=0
    output= ""
    with open(input_path, "r") as f:
        for line in f:
            l+=1
            if l != line:
                output += line
            else:
                output +=line.strip()
                break
    with open(output_path, "w") as f:
        f.write(output)

#### End OF MARKER



