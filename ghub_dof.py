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

lf_label = Label(root,text="Lens (mm)")
lf_label.grid(row = 0, column = 0, sticky=SE)
lf_value = StringVar()
lf = Entry(root,textvariable = lf_value)
lf.grid(row = 0, column = 1, sticky=SE)

sd_label = Label(root,text="F-stop (decimal)")
sd_label.grid(row = 1, column = 0, sticky=E)
fs_value = StringVar()
fs = Entry(root,textvariable = fs_value)
fs.grid(row = 1, column = 1)

sd_label = Label(root,text="Distance (m)")
sd_label.grid(row=2,column=0, sticky=E)
sd_value = StringVar()
sd = Entry(root,textvariable = sd_value)
sd.grid(row = 2, column = 1)

tn_label = Label(root,text="Near")
tn_label.grid(row = 0,column = 2, sticky=SE)
t_near = Text(root,height = 1,width = 8)
t_near.grid(row = 0,column = 3, sticky=SW)

tf_label = Label(root,text="Far")
tf_label.grid(row = 1,column = 2, sticky=E)
t_far = Text(root,height = 1,width = 8)
t_far.grid(row = 1,column = 3, sticky=W)

hf_label =Label(root,text="HyperF")
hf_label.grid(row = 2,column = 2, sticky=E)
hf = Text(root,height = 1,width = 8)
hf.grid(row = 2,column = 3, sticky=W)

b1 = Button(root, text="Convert",command = depth_of_field)
b1.grid(row=3,column=1 ,)


root.mainloop()