# keywords in the language
keywords=['.',',','>','<','[',']','-','+']

# enviroment of the language
array=[0]*100000
pointer=0

def reset():
    array=[0]*100000
    pointer=0


# function to get tokens from the input file
def tokenize( Input ):
    l=[]
    for i in Input:
        l.append(i)
    return l

# function to parse the tokens
def parse( Input ):
    if(len(Input) is 0):
        raise SyntaxError('EOF while reading file')
    l=[]
    while(len(Input) > 0):
        token=Input[0]
        if(token is '['):
            temp=[]
            Input.pop(0)
            while(Input[0] != ']'):
                temp.append(Input[0])
                Input.pop(0)
            Input.pop(0)
            l.append(temp)
        else:
            l.append(token)
            Input.pop(0)
    return l

# function to evaluate the program
def evaluate( program ):

    global pointer
    global array
    
    while(len(program)>0):
        cmd=program[0]
        if(isinstance(cmd,list)):
            while(array[pointer]>0):
                evaluate(cmd)
                array[pointer]-=1
        else:
            if(cmd=='.'):
                array[pointer]=int(input())
            elif(cmd==','):
                print(array[pointer],end="")
            elif(cmd=='-'):
                array[pointer]-=1
            elif(cmd=='+'):
                array[pointer]+=1
            elif(cmd=='>'):
                pointer+=1
            elif(cmd=='<'):
                pointer-=1
            program.pop(0)

        
input_file=input()
evaluate(parse(tokenize(input_file)))

            
            

