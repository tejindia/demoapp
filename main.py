from tkinter import *
from tkinter import messagebox
from db import Database

db = Database()


def populate_list():
    parts_list.delete(0, END) 
    for row in db.fetch():
        parts_list.insert(END, row)
    # print('populate')


def add_item():
    if part_text.get() == '' or customer_text.get() == '' or retailer_text.get() == '' or price_text.get() == '':
        messagebox.showerror('Required Fields', 'Please include all fields')
        return
    db.insert(part_text.get(), customer_text.get(), retailer_text.get(), price_text.get())
    parts_list.delete(0, END)
    parts_list.insert(END, (part_text.get(), customer_text.get(), retailer_text.get(), price_text.get()))
    clear_text()
    populate_list()
    # print('Add')


def select_item(event):
    try:
        global selected_item
        index = parts_list.curselection()[0]
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
    # print(selected_item)
    # print('select')


def remove_item():
    db.remove(selected_item[0])
    clear_text()
    populate_list()
    # print('Remove')


def update_item():
    db.update(selected_item[0], part_text.get(), customer_text.get(), retailer_text.get(), price_text.get())
    clear_text()
    populate_list()
    # print('Update')


def clear_text():
    part_entry.delete(0, END)
    customer_entry.delete(0, END)
    retailer_entry.delete(0, END)
    price_entry.delete(0, END)
    # print('Clear')


# create window object
app = Tk()

# part
part_text = StringVar()
part_label = Label(app, text='Part Name', font=('Arial', 14), pady=10, padx=10)
part_label.grid(row=0, column=0, sticky=W)
part_entry = Entry(app, text=part_text)
part_entry.grid(row=0, column=1)
# customer
customer_text = StringVar()
customer_label = Label(app, text='Customer', font=('Arial', 14), pady=10, padx=10)
customer_label.grid(row=0, column=2, sticky=W)
customer_entry = Entry(app, text=customer_text)
customer_entry.grid(row=0, column=3)
# retailer
retailer_text = StringVar()
retailer_label = Label(app, text='Retailer', font=('Arial', 14), pady=10, padx=10)
retailer_label.grid(row=1, column=0, sticky=W)
retailer_entry = Entry(app, text=retailer_text)
retailer_entry.grid(row=1, column=1)
# price
price_text = StringVar()
price_label = Label(app, text='Price', font=('Arial', 14), pady=10, padx=10)
price_label.grid(row=1, column=2, sticky=W)
price_entry = Entry(app, text=price_text)
price_entry.grid(row=1, column=3)

# parts list (list box)
parts_list = Listbox(app, height=8, width=96, border=0)
parts_list.grid(row=3, column=0, columnspan=4, rowspan=6)
# create scrollbar
scrollbar = Scrollbar(app)
scrollbar.grid(row=3, column=4)
# set scroll to listbox
parts_list.config(yscrollcommand=scrollbar.set)
scrollbar.config(command=parts_list.yview)
# bind select
parts_list.bind('<<ListboxSelect>>', select_item)

# button
add_btn = Button(app, text='Add Part', width=12, command=add_item)
add_btn.grid(row=2, column=0, pady=10)

remove_btn = Button(app, text='Remove Part', width=12, command=remove_item)
remove_btn.grid(row=2, column=1, pady=10)

update_btn = Button(app, text='Update Part', width=12, command=update_item)
update_btn.grid(row=2, column=2, pady=10)

clear_btn = Button(app, text='Clear Input', width=12, command=clear_text)
clear_btn.grid(row=2, column=3, pady=10)

app.title('Part Manager')
app.geometry('600x350+300+150')
app.resizable(False, False)

# background image
# bg = PhotoImage(file="img/bg_shapes.png")
# bg_image = Label(app, image=bg).place(x=0, y=0, relwidth=1, relheight=1)

# populate data
populate_list()

# start program
app.mainloop()
