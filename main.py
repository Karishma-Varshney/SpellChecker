from tkinter import *
from textblob import TextBlob


# -------------------------------SPELLING CHECK----------------------------#
def check():
    get_entry = entry1.get()
    corr = TextBlob(get_entry)
    ans = corr.correct()
    entry2.delete(0, END)
    entry2.insert(0, ans)


# -------------------------------UI SETUP----------------------------#
window = Tk()
window.title('SPELL CHECK✅')
window.minsize(width=500, height=500)
window.config(bg='#AEDEFC', padx=50, pady=50)

pic = PhotoImage(file='logo.png')
c = Canvas(width=148, height=150, bg='#AEDEFC', highlightthickness=0)
c.create_image(74, 75, image=pic)
c.grid(row=0, column=0, columnspan=2, pady=50)

label1 = Label(text='Incorrect Spelling : ', font=('Times New Roman', 20, 'italic'), bg='#AEDEFC')
label1.grid(row=1, column=0)

entry1_frame = Frame(relief='ridge')
entry1_frame.grid(row=1, column=1)
entry1 = Entry(entry1_frame, width=20, font=('Arial', 20, 'italic'))
entry1.focus()
entry1.grid()

button = Button(text='CHECK', width=10, height=2, font=('Times New Roman', 10, 'bold'), bg='#F875AA', command=check)
button.grid(row=2, column=1, padx=30, pady=30)


label2 = Label(text='Correct Spelling : ', font=('Times New Roman', 20, 'italic'), bg='#AEDEFC')
label2.grid(row=3, column=0)

entry2_frame = Frame(relief='ridge')
entry2_frame.grid(row=3, column=1)
entry2 = Entry(entry2_frame, width=20, font=('Arial', 20, 'italic'))
entry2.grid()

window.mainloop()
