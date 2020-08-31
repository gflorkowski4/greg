from tkinter import *
from add_function import add
from sit_rep_function import create_sit_rep




root= Tk()
root.title("Sage Brush")
#root.wm_iconbitmap('data/bush.ico')
root.configure(background='blue')


def add_mission():
	add()

def sit_report():
	create_sit_rep()


#button frame
button_frame = Frame(root)
button_frame.grid(row=0, column=0)
button_frame.configure(background='blue')

name_label = Label(button_frame, text="""Welcome to Sage Brush: 
Click a button to get started""")
name_label.configure(background='white',relief='raised')
name_label.grid(row=0, column=0, padx=5, pady=5)
add_mission_button = Button(button_frame, text="Add Mission", command= add_mission)
add_mission_button.grid(row=0, column=1, padx=10, pady=10)

sit_button = Button(button_frame,text="Create Sit-Rep",command=sit_report)
sit_button.grid(row=1,column=1,padx=10,pady=10)



root.mainloop()