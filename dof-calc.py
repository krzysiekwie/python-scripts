from tkinter import *

root = Tk()
root.minsize(400, 150)

def depth_of_field():
    lens_f = int(lf_value.get())
    s_dist = int(sd_value.get())*1000
    f_stop = float(fs_value.get())

    circle_oc = 0.020

    h_focal = (lens_f**2)/(f_stop * circle_oc) + lens_f
    near_dist = ((s_dist*(h_focal-lens_f))/(h_focal + s_dist - (2 * lens_f))) * 0.001
    far_dist = ((s_dist*(h_focal-lens_f))/(h_focal-s_dist)) * 0.001
    
    t_near.delete(1.0,END)
    t_near.insert(END,"{:.2f}".format(near_dist))
    t_far.delete(1.0,END)
    t_far.insert(END,"{:.2f}".format(far_dist))
    hf.delete(1.0,END)
    hf.insert(END,"{:.2f}".format(h_focal*0.001))

root.wm_title("Depth of Field Calculator")

root.columnconfigure(0, weight=1)
# root.columnconfigure(1, pad=15)

root.columnconfigure(3, weight=1)
root.rowconfigure(0, weight=1)
root.rowconfigure(3, weight=1)

Label(root,text="Lens (mm)").grid(row = 0, column = 0, sticky=SE)
lf_value = StringVar()
Entry(root,textvariable = lf_value).grid(row = 0, column = 1, sticky=SE)

Label(root,text="F-stop (decimal)").grid(row = 1, column = 0, sticky=E)
fs_value = StringVar()
fs = Entry(root,textvariable = fs_value).grid(row = 1, column = 1)

Label(root,text="Distance (m)").grid(row=2,column=0, sticky=E)
sd_value = StringVar()
sd = Entry(root,textvariable = sd_value).grid(row = 2, column = 1)

Label(root,text="Near").grid(row = 0,column = 2, sticky=SE)
t_near = Text(root,height = 1,width = 8).grid(row = 0,column = 3, sticky=SW)

Label(root,text="Far").grid(row = 1,column = 2, sticky=E)
t_far = Text(root,height = 1,width = 8).grid(row = 1,column = 3, sticky=W)

Label(root,text="HyperF").grid(row = 2,column = 2, sticky=E)
hf = Text(root,height = 1,width = 8).grid(row = 2,column = 3, sticky=W)

b1 = Button(root, text="Convert",command = depth_of_field).grid(row=3,column=1 ,)


root.mainloop()
