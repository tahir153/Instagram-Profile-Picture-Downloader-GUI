import instaloader
from tkinter import *
from tkinter import ttk
from tkinter import filedialog

def DP_downloader():
    ig = instaloader.Instaloader()
    dp = text_entry_box_var.get()
    # dp = input("Enter insta user name: ")
    ig.download_profile(dp, profile_pic_only=True)

root = Tk()
root.title('Insta DP Downloader | By Tahir Habib')
root.geometry("420x400")
root['bg'] = "#17202A"
root.columnconfigure(0, weight=1)


blank_line = Label(root, text="\n", fg="red", bg="#17202A", font=("Helvetica", 10))
blank_line.grid()

label_heading = Label(root, text="Enter insta Username Here!", font=("Helvetica", 20), fg="white",
                           bg="#17202A")
label_heading.grid()

text_entry_box_var = StringVar()
text_entry_box = Entry(root,font = ("Roboto", 16), width=25, textvariable=text_entry_box_var)
text_entry_box.grid()

blank_line = Label(root, text="\n", fg="red", bg="#17202A", font=("Helvetica", 10))
blank_line.grid()

Check_button = Button(root, text="Download DP",font = ("Roboto", 11),width=10, bg="blue4", fg="white", command=DP_downloader)
Check_button.grid()

root.mainloop()




