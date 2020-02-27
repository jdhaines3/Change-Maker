""" Change Maker GUI edition """

#import tkinter and make App class
from tkinter import * 

class App(Tk):
    def __init__(self):
        Tk.__init__(self)

        #create header and label fonts
        self.headerFont = ("Calibri", "18", "bold underline")
        self.lblFont = ("Arial", "11", "italic")

        #set window title and app header
        self.title("Change maker")
        Label(self, text = "Change Maker",
              font = self.headerFont).grid(columnspan = 3)

        #---display---#
        #add app elements for price, tender, total change, and money denominations
        #split up for easier debugging
        self.addPrice()
        self.addTender()
        self.addMoneyBack()
        self.addBills()
        self.addCoins()
        self.addButtons()


    #define app elements methods
    def addPrice(self):
        """ add price elements """
        #price label(s)
        Label(self, text = "Price of item:",
              font = self.lblFont).grid(row = 1, column = 0)
        Label(self, text = "$",
              font = self.lblFont).grid(row = 1, column = 1, sticky = "e")

        #price entry box
        self.txtPrice = Entry(self, relief = "sunken")
        self.txtPrice.grid(row = 1, column = 2)
        self.txtPrice.insert(0, "0.00")


    def addTender(self):
        """ add cash tendered elements """
        #Tender labels
        Label(self, text = "Cash tendered:",
              font = self.lblFont).grid(row = 2, column = 0)
        Label(self, text = "$",
              font = self.lblFont).grid(row = 2, column = 1, sticky = "e")

        #tender entry box
        self.txtTender = Entry(self, relief = "sunken")
        self.txtTender.grid(row = 2, column = 2)
        self.txtTender.insert(0, "0.00")


    def addMoneyBack(self):
        """ add total change recieved elements and results header """
        #add Results header and total change label
        Label(self, text = """
---Results---""",
              font = self.headerFont).grid(row = 3, columnspan = 3)
        Label(self, text = "Total change:",
              font = self.lblFont).grid(row = 4, column = 0)
        Label(self, text = "$",
              font = self.lblFont).grid(row = 4, column = 1, sticky = "e")

        #add read-only text box
        self.lblMoneyBack = Label(self, bg = "#C6E2FF", anchor = "w", relief = "flat")
        self.lblMoneyBack.grid(row = 4, column = 2, sticky = "we")


    def addBills(self):
        """ add change (bills) elements: each money denomination 20's to 1's """
        #add section divide
        #add labels for each monetary denomination
        Label(self, text = """
---Bills and Coins---""",
              font = self.lblFont).grid(row = 5, columnspan = 3)
        #bills labels
        Label(self, text = "Twenties:",
              font = self.lblFont).grid(row = 6, column = 0)
        Label(self, text = "Tens:",
              font = self.lblFont).grid(row = 7, column = 0)
        Label(self, text = "Fives:",
              font = self.lblFont).grid(row = 8, column = 0)
        Label(self, text = "Ones:",
              font = self.lblFont).grid(row = 9, column = 0)

        #bills entry boxes
        self.lblTwenties = Label(self, bg = "#C6E2FF", anchor = "w", relief = "flat")
        self.lblTwenties.grid(row = 6, column = 1, columnspan = 2, sticky = "we")

        self.lblTens = Label(self, bg = "#C6E2FF", anchor = "w", relief = "flat")
        self.lblTens.grid(row = 7, column = 1, columnspan = 2, sticky = "we")

        self.lblFives = Label(self, bg = "#C6E2FF", anchor = "w", relief = "flat")
        self.lblFives.grid(row = 8, column = 1, columnspan = 2, sticky = "we")

        self.lblOnes = Label(self, bg = "#C6E2FF", anchor = "w", relief = "flat")
        self.lblOnes.grid(row = 9, column = 1, columnspan = 2, sticky = "we")


    def addCoins(self):
        """ add change (coins) elements: each money denom. from qtrs to pennies """
        
        #coins labels
        Label(self, text = "Quarters:",
              font = self.lblFont).grid(row = 10, column = 0)
        Label(self, text = "Dimes:",
              font = self.lblFont).grid(row = 11, column = 0)
        Label(self, text = "Nickels:",
              font = self.lblFont).grid(row = 12, column = 0)
        Label(self, text = "Pennies:",
              font = self.lblFont).grid(row = 13, column = 0)

        #bills entry boxes
        self.lblQtrs = Label(self, bg = "#C6E2FF", anchor = "w", relief = "flat")
        self.lblQtrs.grid(row = 10, column = 1, columnspan = 2, sticky = "we")

        self.lblDimes = Label(self, bg = "#C6E2FF", anchor = "w", relief = "flat")
        self.lblDimes.grid(row = 11, column = 1, columnspan = 2, sticky = "we")

        self.lblNkls = Label(self, bg = "#C6E2FF", anchor = "w", relief = "flat")
        self.lblNkls.grid(row = 12, column = 1, columnspan = 2, sticky = "we")
        
        self.lblPens = Label(self, bg = "#C6E2FF", anchor = "w", relief = "flat")
        self.lblPens.grid(row = 13, column = 1, columnspan = 2, sticky = "we")


    def addButtons(self):
        """ add buttons on bottom """
        #add calculate button
        self.btnCalc = Button(self, text = "Calculate!")
        self.btnCalc.grid(row = 15, column = 0)
        self.btnCalc["command"] = self.calculate

        #add Reset button
        self.btnReset = Button(self, text = "Reset")
        self.btnReset.grid(row = 15, column = 1)
        self.btnReset["command"] = self.reset

        #add exit button
        self.btnExit = Button(self, text = "Exit")
        self.btnExit.grid(row = 15, column = 2)
        self.btnExit["command"] = self.close


    #---add non-element methods: calculate, reset, exit
    def calculate(self):
        """ calculate change and get denominations """
        #calculate base change back
        price = float(self.txtPrice.get())
        tender = float(self.txtTender.get())

        change = tender - price
        #put change into lblMoneyBack with two decimal points
        self.lblMoneyBack["text"] = "%.2f" % change

        #create integer for change
        intchange = int((tender - price) * 100)
        #create arrays for types of coins and temp results for 'for loop'
        coins = [2000, 1000, 500, 100, 25, 10, 5, 1]
        results = [0] * len(coins)

        #updated change maker algorith using coins array and divmod and for loop
        for i in range(len(coins)):
            results[i], intchange = divmod(intchange, coins[i])
            #results[i] get intchange/coins[i]
            #intchange gets intchange%coins[i]

        self.lblTwenties["text"] = "{}".format(results[0])
        self.lblTens["text"] = "{}".format(results[1])
        self.lblFives["text"] = "{}".format(results[2])
        self.lblOnes["text"] = "{}".format(results[3])
        self.lblQtrs["text"] = "{}".format(results[4])
        self.lblDimes["text"] = "{}".format(results[5])
        self.lblNkls["text"] = "{}".format(results[6])
        self.lblPens["text"] = "{}".format(results[7])
        

    def reset(self):
        """ method to reset height and weight to 0 """
        #delete entry boxes and insert 0.00
        self.txtPrice.delete(0, END)
        self.txtPrice.insert(0, "0.00")

        self.txtTender.delete(0, END)
        self.txtTender.insert(0, "0.00")

        #clear all read-only results boxes
        self.lblMoneyBack["text"] = ""
        self.lblTwenties["text"] = ""
        self.lblTens["text"] = ""
        self.lblFives["text"] = ""
        self.lblOnes["text"] = ""
        self.lblQtrs["text"] = ""
        self.lblDimes["text"] = ""
        self.lblNkls["text"] = ""
        self.lblPens["text"] = ""


    def close(self):
        """add exit button"""
        #destroy yourself
        self.destroy()



#run main
def main():
    app = App()
    app.mainloop()

if __name__ == "__main__":
    main()
    
        
        
