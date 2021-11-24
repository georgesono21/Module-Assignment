#Name: George Sono
#Class: CSE20 (Module Review Assignment)
#Prof: Harikishna Kuttivelli
#Description of program:
  #My application for Tkinter is a four function calculator (add, subtract, multiply, divide) that is in the form of a GUI. It combines all the elements of Tkinter explained in the report and also incorporates other methods that are associated with the classes of each widget.

#importing Tkinter
from tkinter import *

#Setting the root window
window = Tk()
window.geometry("400x500")
window.title("George's Calculator")

#creating the program as class
class Calculator:
  def __init__(self,window):
    #using the Frame function
    window = Frame(window)
    window.pack()
    #we do window.pack() so it exists within the Tkinter Frame

    #creating the display button on zeroth row (first row technicaly)
    numberscreen = Entry(window, width= 30,font=(13))
    numberscreen.grid(row = 0,columnspan = 3, padx = 5, pady = 5)

    #creating a label that gives credit to the creator
    credit = Label(window, text ="Created by George Sono")
    credit.grid(columnspan = 5, row = 6)
    #positioning number screen

    #defining what each button does
    def buttons(num):
      temp = str(numberscreen.get())
      #the .get method gets the current numbers on the number screen
      num = str(num)
      numberscreen.delete(0,END)
      #the .delete method deletes whatever is on the numberscreen
      numberscreen.insert(0,temp+num)
      #this function takes in a parameter and adds it to the end of whatever is already on the display. to update the display, we have to clear whatever is on it, and then update it with the old info + new number

    def clear():
      numberscreen.delete(0,END)
    #this function deletes whatever is on the number screen, in case of a syntax error or if theyre trying to perform a new calculation

    #this function executes when the equals sign is pressed
    def performoperation():
      #if there are any errors during calculation, we throw a syntax error in the number screen display
      try:
        temp = str(numberscreen.get())

        #for each operation, we follow the same syntax, if * exists in what was on the number display, then we identify the operation as multiplication. we do the same case for dividing, adding and subtracting.

        if " * " in temp:
          numbers = temp.split(" * ")
          numberleft = float(numbers[0])
          numberright = float(numbers[1])
          product = numberright * numberleft
          numberscreen.delete(0,END)
          numberscreen.insert(0,str(product))

        #to perform the calculation, we string split it at the operation symbol and then perform the operation by index. 


        elif " / " in temp:
          numbers = temp.split(" / ")
          numberleft = float(numbers[0])
          numberright = float(numbers[1])
          quotient = numberleft / numberright
          numberscreen.delete(0,END)
          numberscreen.insert(0,str(quotient))

        elif " - " in temp:
          numbers = temp.split(" - ")
          numberleft = float(numbers[0])
          numberright = float(numbers[1])
          difference = numberleft - numberright
          numberscreen.delete(0,END)
          numberscreen.insert(0,str(difference))

        elif " + " in temp:
          numbers = temp.split(" + ")
          numberleft = float(numbers[0])
          numberright = float(numbers[1])
          sum = numberright + numberleft
          numberscreen.delete(0,END)
          numberscreen.insert(0,str(sum))

      except ValueError:
          numberscreen.delete(0,END)
          numberscreen.insert(0,"SYNTAX ERROR")
      
  
    #creating the clear button on zeroth row (first row technicalyl)
    buttonclear = Button(window,text = "CLEAR",padx=15,pady=15,command = clear, activebackground = "red")
    buttonclear.grid(row = 0, column = 3)
    #as we don't have any parameters for the clear function, we don't need to the parentheses and thus no lambda function

    #creating the buttons of the first row (second row technically)
    button1 = Button(window,text = "1",padx=30,pady=30,command = lambda: buttons(1),activebackground = "yellow")
    button1.grid(row = 1, column = 0)
    button2 = Button(window,text = "2",padx=30,pady=30,command = lambda: buttons(2),activebackground = "yellow")
    button2.grid(row = 1, column = 1)
    button3 = Button(window,text = "3",padx=30,pady=30,command = lambda: buttons(3),activebackground = "yellow")
    button3.grid(row = 1, column = 2)
    buttondivide = Button(window,text = "/",padx=30,pady=30,command = lambda: buttons(" / "),activebackground = "magenta")
    buttondivide.grid(row = 1, column = 3)
    #as the buttons function uses a parameter, we have to make them into lambda functions



    #creating the buttons of the second row (third row technically)
    button1 = Button(window,text = "4",padx=30,pady=30,command = lambda: buttons(4),activebackground = "yellow")
    button1.grid(row = 2, column = 0)
    button2 = Button(window,text = "5",padx=30,pady=30,command = lambda: buttons(5),activebackground = "yellow")
    button2.grid(row = 2, column = 1)
    button3 = Button(window,text = "6",padx=30,pady=30,command = lambda: buttons(6),activebackground = "yellow")
    button3.grid(row = 2, column = 2)
    buttonmultiply = Button(window,text = "*",padx=30,pady=30,command = lambda: buttons(" * "),activebackground = "magenta")
    buttonmultiply.grid(row = 2, column = 3)
    #as the buttons function uses a parameter, we have to make them into lambda functions

    #creating the buttons of the third row (fourth row technically)
    button1 = Button(window,text = "7",padx=30,pady=30,command = lambda: buttons(7),activebackground = "yellow")
    button1.grid(row = 3, column = 0)
    button2 = Button(window,text = "8",padx=30,pady=30,command = lambda: buttons(8),activebackground = "yellow")
    button2.grid(row = 3, column = 1)
    button3 = Button(window,text = "9",padx=30,pady=30,command = lambda: buttons(9),activebackground = "yellow")
    button3.grid(row = 3, column = 2)
    buttonsubtract = Button(window,text = "-",padx=30,pady=30,command = lambda: buttons(" - "),activebackground = "magenta")
    buttonsubtract.grid(row = 3, column = 3)
    #as the buttons function uses a parameter, we have to make them into lambda functions

    #creating the buttons of the fourth row (fifth row technically)
    button0 = Button(window,text = "0", padx = 30, pady = 30,command = lambda: buttons(0),activebackground = "yellow")
    button0.grid(row=4, column = 1)
    buttonexit = Button(window,text = "(-/+)",padx = 20, pady = 20, command = lambda: buttons("-"),activebackground = "cyan")
    buttonexit.grid(row=4,column = 0)
    buttonequals = Button(window, text = "=",padx = 30, pady = 30, command = lambda: performoperation(),activebackground = "green")
    buttonequals.grid(row = 4, column = 2)
    buttonadd = Button(window, text = "+",padx = 30, pady = 30,command = lambda: buttons(" + "),activebackground = "magenta")
    buttonadd.grid(row = 4,column = 3)
    window.mainloop()
    #as the buttons function uses a parameter, we have to make them into lambda functions

#creating the Calcualor object
program = Calculator(window)
#running the mainloop
program.mainloop()

