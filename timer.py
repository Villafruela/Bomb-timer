from tkinter import *
import time
tick = 0

class App(Frame):
    def __init__(self,master=None):
        Frame.__init__(self, master)
        self.master = master
        self.label = Label(text="", fg="white", bg="red", font=("Helvetica", 100))
        self.label.place(x=70,y=120)
        self.update_clock()

    def update_clock(self):
        global timer
        global tick
        mins, secs = divmod(tick, 60)
        #print("minutes : %s / secondes : %s" % (mins,secs))
        timer = '{:02d}:{:02d}'.format(mins, secs)
        self.label.configure(text=str(timer))
        #print("timer a %i secondes" % (tick))
        self.after(1000, self.update_clock)
        if tick == 0:
            self.label.configure(text="BOUM !")
        else:
            tick -= 1

tick = input ("Décompte de combien de minutes ? :")
tick = int(tick) * 60

root = Tk()
app=App(root)
root.wm_title("Bomb Timer")
root.geometry("400x400")
root.configure(bg='red')
root.mainloop()
