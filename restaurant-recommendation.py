import tkinter.filedialog
import readrestaurant
file_name=tkinter.filedialog.askopenfilename()
thisfile=open(file_name,"r")


readrestaurant.read_restaurant(thisfile)




