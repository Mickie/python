import tkinter.filedialog
import readgrade
file_name=tkinter.filedialog.askopenfilename()
thisfile=open(file_name,"r")

his_file_name=tkinter.filedialog.askopenfilename()
hisfile=open(his_file_name,"w")

#read the file and get a list of grade
grades=readgrade.read_grades(thisfile)

#account the mumber of its grade range,
#for example ,[0-9]:1

count_number=readgrade.count_number(grades)

#print out the hisprogram based on the count_number and write in a new file

for i in range(0,10):
    grade_low=i*10
    grade_high=i*10+9
    pic="*"*count_number[i]
    hisfile.write(str(grade_low)+"-"+str(grade_high)+" :" )
    hisfile.write(pic)
    hisfile.write("\n")

hisfile.write("100   :")
hisfile.write("*"*count_number[10])
hisfile.write("\n")
thisfile.close()
hisfile.close()

print("complete")
