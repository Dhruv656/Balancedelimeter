class bnode:
    def __init__(self,b):
        self.b=b
        self.nextbrace=None

    def showInfo(self):
        print("Brace: ",self.b)

class MyStack:
    def __init__(self):
        self.tos=None
    
    def push(self,newbrace):
        if self.tos==None:
            self.tos=newbrace
        else:
            newbrace.nextbrace=self.tos
            self.tos=newbrace

    def pop(self):
        if self.tos==None:
            return None
        else:
            s=self.tos
            self.tos=self.tos.nextbrace
            return s

    
    def isEmpty(self):
        if (self.tos==None):
            return True
        else:
            return False

def BraceStacks():
    mystack=MyStack()
    expr=input("Enter Arithmatic Equation: ")

    for i in expr:
        if i in "{[(":
            bnd=bnode(i)
            mystack.push(bnd)
           
        elif i in "]})":
            try:
                x=mystack.pop().b           
                if (i=='(' and x!=')') or (i=='{' and x!='}') or (i=='[' and x!=']' ):
                    return False
            except:
                return False

    return mystack.isEmpty()

if BraceStacks():
    print('Balanced')
else:
    print('Imbalanced')





























    