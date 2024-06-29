import re
import tkinter
import tkinter.ttk
from tkinter import messagebox


def ExactLetters(S):
  Pattern = re.sub("_",".",S)
  L = []
  File = open("AllWordsSplit.txt","r")
  for line in File:
    LS = line.strip()
    if bool(re.search(Pattern,LS)):
      L.append(LS)

  File.close()
  return(L)


def ContainsLetters(T):
  File = open("AllWordsSplit.txt","r")
  L = []
  for line in File:
    LS = line.strip()
    NotIn = False
    for i in T:
      if i not in LS:
        NotIn = True
        break
    if not NotIn:
      L.append(LS)
  File.close()
  return(L)


def InBoth(L1,L2):
  L = []
  for l in L1:
    if l in L2:
      L.append(l)
  return(L)



def RunIt():
  """this is the function that runs once the Tkinter button is pressed.  It will check that each text box has at most one alphabetic character in it, and upon success it will search the words given the conditions of the boxes"""
  Errors = ""

  EL = [EL1,EL2,EL3,EL4,EL5]
  ELString = ""
  for n,l in enumerate(EL,1):
    temp = l.get()
    #we first check if the string has more than one character, which it should not
    if len(temp) > 1:
      Errors += "Top Box Number " + str(n) + "\n"
    else:
      if len(temp) == 0:
        #this means the user left the box blank, so fill it in with an underscore for the ExactLetters function
        ELString += "_"
      else:
        #now we make sure the one character is alphabetic
        if temp.isalpha():
          ELString += temp
        else:
          Errors += "Top Box Number " + str(n) + "\n"

  CL = [CL1,CL2,CL3,CL4,CL5]
  CLString = ""
  for n,l in enumerate(CL,1):
    temp = l.get()
    #the bottom boxes can contain at most one character, so check that
    if len(temp) > 1:
      Errors += "Bottom Box Number " + str(n) + "\n"
    else:
      if len(temp) == 1:
        #we only allow alphabetic characters in the boxes, so check that
        if temp.isalpha():
          CLString += temp
        else:
          Errors += "Bottom Box Number " + str(n) + "\n"


  #if the Errors variable is not blank, then there is an error in one of the boxes, so display the error
  if (len(Errors) > 0):
    messagebox.showerror("Error!", "You have an error in the following box(es):\n" + Errors)
  else:
    L1 = ExactLetters(ELString)
    L2 = ContainsLetters(CLString)
    L = InBoth(L1,L2)
    if len(L) == 0:
      InfoString = "There are no words that fit your criteria."
    else:
      InfoString = "The words that fit the criteria are:\n"
      for l in L:
        InfoString += l + "\n"
    
    messagebox.showinfo("Possible Words",InfoString)
    
    
    
    
  

"""
the part below here is for the Tkinter GUI
"""

pg = tkinter.Tk()
pg.title("Wordle Help!")

#this command increases the original size of the window to 500x200 pixels
pg.geometry("500x200")

tkinter.ttk.Label(pg, text="If you know which location a letter should be in, type that letter in the corresponding box below.  If you don't know which letter goes in a specific location, then leave that box blank.  Enter at most one letter per box below.", wraplength=500, justify="left").grid(row=1, column=1, columnspan=5)

#create the labels for the first set of text boxes:
EL1 = tkinter.StringVar()
EL2 = tkinter.StringVar()
EL3 = tkinter.StringVar()
EL4 = tkinter.StringVar()
EL5 = tkinter.StringVar()

tkinter.ttk.Entry(pg, textvariable=EL1, width=5).grid(row=2, column=1, padx=5, pady=2, sticky="ew")
tkinter.ttk.Entry(pg, textvariable=EL2, width=5).grid(row=2, column=2, padx=5, pady=2, sticky="ew")
tkinter.ttk.Entry(pg, textvariable=EL3, width=5).grid(row=2, column=3, padx=5, pady=2, sticky="ew")
tkinter.ttk.Entry(pg, textvariable=EL4, width=5).grid(row=2, column=4, padx=5, pady=2, sticky="ew")
tkinter.ttk.Entry(pg, textvariable=EL5, width=5).grid(row=2, column=5, padx=5, pady=2, sticky="ew")






#pady=(30,0) adds padding only to the top
tkinter.ttk.Label(pg, text="In the boxes below, enter the letters you know are in the word.  The order in which you list them in the boxes does not matter.  Enter at most one letter per box below.", wraplength=500, justify="left").grid(row=3, column=1, columnspan=5, pady=(30,0))


#create the labels for the second set of text boxes:
CL1 = tkinter.StringVar()
CL2 = tkinter.StringVar()
CL3 = tkinter.StringVar()
CL4 = tkinter.StringVar()
CL5 = tkinter.StringVar()

tkinter.ttk.Entry(pg, textvariable=CL1, width=5).grid(row=4, column=1, padx=5, pady=2, sticky="ew")
tkinter.ttk.Entry(pg, textvariable=CL2, width=5).grid(row=4, column=2, padx=5, pady=2, sticky="ew")
tkinter.ttk.Entry(pg, textvariable=CL3, width=5).grid(row=4, column=3, padx=5, pady=2, sticky="ew")
tkinter.ttk.Entry(pg, textvariable=CL4, width=5).grid(row=4, column=4, padx=5, pady=2, sticky="ew")
tkinter.ttk.Entry(pg, textvariable=CL5, width=5).grid(row=4, column=5, padx=5, pady=2, sticky="ew")


tkinter.ttk.Button(pg, text="Find Me Some Words!", command=RunIt).grid(row=5,column=2, columnspan=3)


pg.mainloop()


