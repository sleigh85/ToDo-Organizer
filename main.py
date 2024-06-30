import pickle
from tkinter import *
from tkinter.font import Font
from tkinter import filedialog

root = Tk()
root.title("My Organizer")
root.geometry('800x700')
root.configure(bg='dark slate gray')

my_font = Font(family="Brush Script MT", size=30, weight='bold')

#functions
def delete_item():
    my_listbox.delete(ANCHOR)

def add_item():
    my_listbox.insert(END, my_entry.get())
    my_entry.delete(0, END)

def strike_item():
    my_listbox.itemconfig(
        my_listbox.curselection(),
        fg='#dedede'
    )
    my_listbox.selection_clear(0, END)

def unstrike_item():
    my_listbox.itemconfig(
        my_listbox.curselection(),
        fg='#7e685a'
    )
    my_listbox.selection_clear(0, END)

def save_list():
    file_name = filedialog.asksaveasfilename(
        initialdir="data",
        title='Save File',
        filetypes=(("Dat Files", "*.dat"),
                   ("All Files", "*.*")))
    if file_name:
        if file_name.endswith(".dat"):
            pass
        else:
            file_name = f'{file_name}.dat'

    #save stuff from listbox
    stuff = my_listbox.get(0, END)
    #open selected file
    output_file = open(file_name, 'wb')
    #add stuff to file
    pickle.dump(stuff, output_file)


def open_list():
    file_name = filedialog.askopenfilename(initialdir="data",
                                           title='Open File',
                                           filetypes=(("Dat Files", "*.dat"),
                                                      ("All Files", "*.*")))
    if file_name:
        my_listbox.delete(0, END)
        #open file
        input_file = open(file_name, 'rb')
        #load file
        stuff = pickle.load(input_file)
        for item in stuff:
            my_listbox.insert(END, item)

def clear_list():
    my_listbox.delete(0, END)

#create a frame for list
my_frame = Frame(root)
my_frame.pack(pady=40)

#create listbox
my_listbox = Listbox(my_frame,
                     font=my_font,
                     height=8,
                     width=70,
                     bg='lavender',
                     bd=0,
                     fg='slateblue4',
                     justify='center',
                     highlightthickness=0,
                     selectbackground='#c2b9b0',
                     activestyle='none')
my_listbox.pack()
#test list to add to listbox
#kids = ['Gabe', 'Lyla', 'Boon', 'Vida', 'Kya', 'Amira', 'Me']
#for item in kids:
   # my_listbox.insert(END, item)

#create entrybox
my_entry = Entry(root, font=('Helvetica', 24), width=26)
my_entry.pack(pady=10)

#create buttonframe
btn_frame = Frame(root, bg='dark slate gray')
btn_frame.pack(pady=20)

#create buttons
del_btn = Button(btn_frame, text='Delete', command=delete_item, bg='#e7717d')
add_btn = Button(btn_frame, text='Add', command=add_item, bg='#afd275')
strike_btn = Button(btn_frame, text='Strike-thru', command=strike_item, bg='#e7717d')
unstrike_btn = Button(btn_frame, text='Unstrike', command=unstrike_item, bg='#afd275')
#add unstrike all btn

del_btn.grid(row=0, column=1, padx=20, pady=10)
add_btn.grid(row=0, column=0, padx=20, pady=10)
strike_btn.grid(row=0, column=3, padx=20, pady=10)
unstrike_btn.grid(row=0, column=2, padx=20, pady=10)

#create menu
my_menu = Menu(root)
root.config(menu=my_menu)
file_menu = Menu(my_menu, tearoff=False)
my_menu.add_cascade(label='Options', menu=file_menu)
file_menu.add_command(label='Save List', command=save_list)
file_menu.add_command(label='Open List', command=open_list)
file_menu.add_separator()
file_menu.add_command(label='Delete List', command=clear_list)

root.mainloop()
