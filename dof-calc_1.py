from tkinter import *

window = Tk()

# def km_to_miles():
#     miles = float(e1_value.get())*1.6
#     t1.insert(END,miles)

def depth_of_field():
    lens_f = int(lf_value.get())
    s_dist = int(sd_value.get())*1000
    #  f_stop = 2**i/2 , where i = 1, 2, 3,... for f/1.4, f/2, f/2.8,...
    f_stop = 2**(3/2)
    
    circle_oc = 0.020

    h_focal = (lens_f**2)/(f_stop * circle_oc) + lens_f
    print(h_focal)
    near_dist = ((s_dist*(h_focal-lens_f))/(h_focal + s_dist - (2 * lens_f))) * 0.001
    far_dist = ((s_dist*(h_focal-lens_f))/(h_focal-s_dist)) * 0.001
    
    t_near.delete(1.0,END)
    t_near.insert(END,"{:.2f}".format(near_dist))
    t_far.delete(1.0,END)
    t_far.insert(END,"{:.2f}".format(far_dist))
    hf.delete(1.0,END)
    hf.insert(END,"{:.2f}".format(h_focal*0.001))

window.wm_title("Depth of Field Calculator")


lf_label = Label(window,text="Lens (mm)")
lf_label.grid(row = 0,column = 0)
lf_value = StringVar()
lf = Entry(window,textvariable = lf_value)
lf.grid(row = 0,column = 1)

sd_label = Label(window,text="Distance (m)")
sd_label.grid(row=1,column=0)
sd_value = StringVar()
sd = Entry(window,textvariable = sd_value)
sd.grid(row = 1,column = 1)

tn_label = Label(window,text="Near")
tn_label.grid(row = 0,column = 2)
t_near = Text(window,height = 1,width = 8)
t_near.grid(row = 0,column = 3)

tf_label = Label(window,text="Far")
tf_label.grid(row = 1,column = 2)
t_far = Text(window,height = 1,width = 8)
t_far.grid(row = 1,column = 3)

hf_label = Label(window,text="HyperF")
hf_label.grid(row = 2,column = 2)
hf = Text(window,height = 1,width = 8)
hf.grid(row = 2,column = 3)

b1 = Button(window, text="Convert",command = depth_of_field)
b1.grid(row=3,column=1)


window.mainloop()
