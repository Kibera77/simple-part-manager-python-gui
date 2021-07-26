# creating a part manager application
from tkinter import *
from tkinter import messagebox

import dbss

# create window object

app = Tk()

app.title('Part Manager')
app.geometry('700x350')


# functions


def populate_list():
    parts_list.delete(0, END)
    for row in dbss.fetch():
        parts_list.insert(END, row)
    # print('populate')


def add_item():
    if part_text.get() == "" or customer_text.get() == "" or retailer_text.get() == "" or price_text.get() == "":
        messagebox.showerror('Required Fields', 'Please include all fields.')
        return
    dbss.insert(part_text.get(), customer_text.get(), retailer_text.get(), price_text.get())
    parts_list.delete(0, END)
    parts_list.insert(END, (part_text.get(), customer_text.get(), retailer_text.get(), price_text.get()))
    clear_text()
    populate_list()


def select_item(event):
    try:
        global selected_item
        index = parts_list.curselection()[0]
        selected_item = parts_list.get(index)
        # print('selected')

        part_entry.delete(0, END)
        selected_item = parts_list.get(index)

        part_entry.delete(0, END)
        part_entry.insert(END, selected_item[1])
        customer_entry.delete(0, END)
        customer_entry.insert(END, selected_item[2])
        retailer_entry.delete(0, END)
        retailer_entry.insert(END, selected_item[3])
        price_entry.delete(0, END)
        price_entry.insert(END, selected_item[4])
    except IndexError:
        pass


def remove_item():
    try:
        dbss.remove(selected_item[0])
        clear_text()
        populate_list()
    except NameError:
        pass


def update_item():
    try:
        dbss.update(selected_item[0], part_text.get(), customer_text.get(), retailer_text.get(), price_text.get())
        populate_list()
    except NameError:
        pass


def clear_text():
    part_entry.delete(0, END)

    customer_entry.delete(0, END)

    retailer_entry.delete(0, END)

    price_entry.delete(0, END)


# the menus
menu_bar = Menu(app)
file = Menu(menu_bar, tearoff=0)
file.add_command(label='New')
file.add_command(label='Open Folder')
file.add_command(label='Save')
file.add_command(label='Save As')

file.add_separator()
file.add_command(label='Exit', command=app.quit)
menu_bar.add_cascade(label='File', menu=file)

# display the menu
app.config(menu=menu_bar)

# parts


part_text = StringVar()

part_label = Label(app, text='Part Name', font=('courier', 14, 'bold'), pady=20)
part_label.grid(row=0, column=0, sticky=W)
part_entry = Entry(app, textvariable=part_text)
part_entry.grid(row=0, column=1)

# customer
customer_text = StringVar()

part_label = Label(app, text='Customer', font=('courier', 14, 'bold'), pady=20)
part_label.grid(row=0, column=2, sticky=W)
customer_entry = Entry(app, textvariable=customer_text)
customer_entry.grid(row=0, column=3)

# retailer
retailer_text = StringVar()

part_label = Label(app, text='Retailer', font=('courier', 14, 'bold'), pady=20)
part_label.grid(row=1, column=0, sticky=W)
retailer_entry = Entry(app, textvariable=retailer_text)
retailer_entry.grid(row=1, column=1)

# price
price_text = StringVar()

part_label = Label(app, text='Price', font=('courier', 14, 'bold'), pady=20)
part_label.grid(row=1, column=2, sticky=W)
price_entry = Entry(app, textvariable=price_text)
price_entry.grid(row=1, column=3)

# scrollbar

scrollbar = Scrollbar(app)
scrollbar.grid(row=3, column=3)

# part list : list box

parts_list = Listbox(app, height=8, width=50, border=0, bg='#ecf3f4',
                     cursor='arrow', font=('Helvetica', 10, 'normal'))
parts_list.grid(row=3, column=0, columnspan=3, rowspan=6, pady=20, padx=25)

# set scrollbar to listbox
parts_list.configure(yscrollcommand=scrollbar.set)
scrollbar.config(command=parts_list.yview)

# bind select
parts_list.bind('<<ListboxSelect>>', select_item)

# buttons
add_btn = Button(app, text='Add part', activeforeground=('#07bafc'), activebackground=('#d8f2e7'),
                 width=12, relief=RIDGE, bg='#0091f9', command=add_item)
add_btn.grid(row=2, column=0, pady=20)

remove_btn = Button(app, text='Remove part', activeforeground=('#07bafc'),
                    activebackground=('#d8f2e7'), width=12, relief=RIDGE, bg='#0091f9', command=remove_item)
remove_btn.grid(row=2, column=1, pady=20)

update_btn = Button(app, text='Update part', activeforeground=('#07bafc'),
                    activebackground=('#d8f2e7'), width=12, relief=RIDGE, bg='#0091f9', command=update_item)
update_btn.grid(row=2, column=2, pady=20)

clear_btn = Button(app, text='Clear Input', activeforeground=('#07bafc'),
                   activebackground=('#d8f2e7'), width=12, relief=RIDGE, bg='#0091f9', command=clear_text)
clear_btn.grid(row=2, column=3, pady=20)

# populate data

populate_list()

# start program
app.mainloop()
