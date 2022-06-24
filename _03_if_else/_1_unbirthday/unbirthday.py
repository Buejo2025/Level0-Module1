import turtle
from tkinter import messagebox, simpledialog, Tk
if __name__ == '__main__':
    window = Tk()
    window.withdraw()
    # Ask the user for their birthday (mm/dd), e.g. 06/09
    simpledialog.askinteger(title='Happy birthday game1', prompt='What is your birthday?')
    #If it matches today's date, wish them a happy birthday

    # otherwise, wish them a very merry unbirthday
    simpledialog.askinteger(title='Happy birthday game1', prompt='I wish you a unbirthday!')
    # Call turtle.done
    turtle.done()
