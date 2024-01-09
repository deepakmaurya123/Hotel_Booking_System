from tkinter import *
from PIL import Image, ImageTk

from customer import Cust_window
from booking import Book_window
from detail import detail_window


class HotelManagementSystem:
    def __init__(self, root):
        self.root = root
        self.root.title("Hotel Booking System")
        self.root.geometry("1280x720+0+0")
        self.root.state("zoomed")

        # title label
        title_lbl = Label(self.root, text="Hotel   Booking   System", font=("times new roman", 28, "bold"), bg="black",
                          fg="white")
        title_lbl.place(x=0, y=0, width=1550, height=55)

        # background image
        img = Image.open(r"C:\Users\deepa\OneDrive\Desktop\RSMT major project\bg.png")
        img = img.resize((1300, 760))
        self.photoimg = ImageTk.PhotoImage(img)

        bg_img = Label(self.root, image=self.photoimg)
        bg_img.place(x=250, y=55, width=1300, height=760)

        # logo image (royal hotel)
        logo = Image.open(r"C:\Users\deepa\OneDrive\Desktop\RSMT major project\logo1.jpg")
        logo = logo.resize((270, 170))
        self.photoimg3 = ImageTk.PhotoImage(logo)

        logo = Label(self.root, image=self.photoimg3)
        logo.place(x=0, y=55, width=250, height=170)

        # menu label
        menu_label = Label(self.root, text="{ MENU }", font=("times new roman", 28, "bold"), bg="black", fg="yellow")
        menu_label.place(x=0, y=225, width=250, height=70)

        # customer button
        customer = Button(self.root, text="Customer", command=self.cust_details, cursor="hand2",
                          font=("times new roman", 25, "bold"), bg="black", fg="yellow")
        customer.place(x=0, y=295, width=250, height=50)

        # booking button
        booking = Button(self.root, text="Booking", command=self.book_details, cursor="hand2",
                         font=("times new roman", 25, "bold"), bg="black", fg="yellow")
        booking.place(x=0, y=345, width=250, height=50)

        # details button
        details = Button(self.root, text="Details", command=self.details, cursor="hand2",
                         font=("times new roman", 25, "bold"), bg="black", fg="yellow")
        details.place(x=0, y=395, width=250, height=50)

        # logout button
        logout = Button(self.root, text="Exit", command=self.logout, cursor="hand2",
                        font=("times new roman", 25, "bold"), bg="black", fg="yellow")
        logout.place(x=0, y=445, width=250, height=50)

        # side 1 image
        img1 = Image.open(r"C:\Users\deepa\OneDrive\Desktop\RSMT major project\image.jpg")
        img1 = img1.resize((250, 160))
        self.photoimg1 = ImageTk.PhotoImage(img1)

        bg_img = Label(self.root, relief=RIDGE, image=self.photoimg1)
        bg_img.place(x=0, y=495, width=250, height=160)

        # side 2 image
        img2 = Image.open(r"C:\Users\deepa\OneDrive\Desktop\RSMT major project\images2.jpg")
        img2 = img2.resize((250, 160))
        self.photoimg2 = ImageTk.PhotoImage(img2)

        bg_img = Label(self.root, relief=RIDGE, image=self.photoimg2)
        bg_img.place(x=0, y=645, width=250, height=160)

    def cust_details(self):
        self.new_window = Toplevel(self.root)
        self.app = Cust_window(self.new_window)

    def book_details(self):
        self.new_window = Toplevel(self.root)
        self.app = Book_window(self.new_window)

    def details(self):
        self.new_window = Toplevel(self.root)
        self.app = detail_window(self.new_window)

    def logout(self):
        self.root.destroy()


if __name__ == "__main__":
    root = Tk()
    obj = HotelManagementSystem(root)
    root.mainloop()
