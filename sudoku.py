#Sudoku
import time
import pandas as pd
import numpy as np

#empty coordinate index
indexList = []

#original sudoku
sudoku_data=pd.read_excel("E:\钧资料3\大学资料\课程\LN3109运筹学\LINGO\sudoku.xlsx",sheet_name="Given",header=None,names=None,verbose=True,engine="openpyxl")
sudoku = np.array(
    [[8,0,0,0,0,0,0,0,0],
          [0,0,3,6,0,0,0,0,0],
          [0,7,0,0,9,0,2,0,0],
          [0,5,0,0,0,7,0,0,0],
          [0,0,0,0,4,5,7,0,0],
          [0,0,0,1,0,0,0,3,0],
          [0,0,1,0,0,0,0,6,8],
          [0,0,8,5,0,0,0,1,0],
          [0,9,0,0,0,0,4,0,0],
          ]
    )
sudoku=np.array(sudoku_data)
sudoku.astype(np.int_)

#find the first empty coordinate
def firstEmpty()->None:
    for i in range(0,9):
        for j in range(0,9):
            if sudoku[i,j] == 0:
                myPush([i,j])
                return None #end this function

#find the last empty coordinate                
def lastEmpty()->list:
    for i in range(8,-1,-1):
        for j in range(8,-1,-1):
            if sudoku[i,j] == 0:
                return [i,j]

#append
def myPush(coordinate:list)->None:
    indexList.append(coordinate)

#pop
def myPop()->None:
    indexList.pop()

#find the next empty coordinate, and append
def nextEmpty()->None:
    #last coordinate
    a,b = indexList[-1]
    #next one
    b += 1
    for i in range(a,9):
        #next row
        if i != a:
            b = 0
        for j in range(b,9):
            if sudoku[i,j] == 0:
                myPush([i,j])
                return None #end this function

#add 1
def myAdd()->None:
    #last coordinate
    a,b = indexList[-1]
    sudoku[a,b] += 1

#check the last coordinate if it's legal
def isLegal()->bool:
    #last coordinate
    a,b = indexList[-1]
    temp = sudoku[a,b]

    #row
    for i in range(9):
        if sudoku[a,i] == temp and i != b:
            return False

    #column
    for i in range(9): 
        if sudoku[i,b] == temp and i != a:
            return False
    
    #block
    xx = int(a / 3)
    yy = int(b / 3)
    for i in range(3):
        for j in range(3):
            if sudoku[xx * 3 + i,yy * 3 + j] == temp and (xx * 3 + i) != a and (yy * 3 + j) != b:
                return False

    #otherwise, it's legal
    return True

#check the any coordinate if it's legal
def OneisLegal(a:int,b:int)->bool:
    temp = sudoku[a,b]

    #row
    for i in range(9):
        if sudoku[a,i] == temp and i != b:
            return False

    #column
    for i in range(9): 
        if sudoku[i,b] == temp and i != a:
            return False
    
    #block
    xx = int(a / 3)
    yy = int(b / 3)
    for i in range(3):
        for j in range(3):
            if sudoku[xx * 3 + i,yy * 3 + j] == temp and (xx * 3 + i) != a and (yy * 3 + j) != b:
                return False

    #otherwise, it's legal
    return True

#go back to 0 and delete from list
def myReturn()->None:
    #last coordinate
    a,b = indexList[-1]
    sudoku[a,b] = 0
    myPop()

#output
def myOutput()->None:    
    for i in range(9):
        print(sudoku[i])
    print("\n")

#begin
begin_time=time.time()
print("Question:")
myOutput()
print("Processing ...")

#append first coordinate
firstEmpty()

#last coordinate
last_a, last_b=lastEmpty()

#loop until last one is not empty or illegal
while sudoku[last_a,last_b] == 0 or OneisLegal(last_a,last_b)==False:
    #last coordinate
    a,b = indexList[-1]
    if isLegal()==True and sudoku[a,b]>=1 and sudoku[a,b]<=9:
        message="({},{})={} legal".format(a,b,sudoku[a,b])
        print(message,end="")
        print("\b"*len(message),end="",flush=True)
        nextEmpty()
    elif sudoku[a,b]>9:
        #deal with the second last coordinate first
        myReturn()
        myAdd()
    else:
        myAdd()

#end
print("\n\nAnswer:")
myOutput()
end_time=time.time()
print('Finished in {:.3f} s!\n'.format(end_time-begin_time))

"""
首先，从第一行开始寻找第一个待填写的元素位置，并压入用于记录每次操作位置的栈中；
然后，判断此时该位置元素是否合法（合法：即该数字位于0-9之间，并且与该数字所在行、所在列、所在宫内的数字均不重复）。
当该数字合法时，则继续寻找下一个待填写的位置，并压入栈中；
当该数字不合法时，若该数字还没有大于9则自增，若该数字已大于9则退回至上一位置（当前位置归零并弹出）；
最后，当最后一个待填写的元素合法且不等于0之前，重复执行上述步骤。
"""