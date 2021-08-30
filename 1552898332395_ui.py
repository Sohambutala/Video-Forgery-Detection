from tkinter import *
from tkinter import filedialog
import diff
import time
import cv2
import matplotlib
import matplotlib.pyplot as plt
from tkinter import ttk

r1 = 1920
rr = 1290



window = Tk()
window.title("Video Forgery Detection Tool ")
window.geometry('1600x1000')


def exit(event):
    window.quit()
 
# pp = ttk.Progressbar(window, orient='horizontal', length=200, mode='determinate')
# pp.place(x=710, y= 120)

lbl1 = Label(window, text="Hello , Welcome to Video Forgery Detection Tool ")
def leb():
	global r1, rr
	# lbl1.grid(column=0, row=1)
	lbl1.place(x=r1%rr, y=45)
	r1+=40
	window.after(1000, leb)

window.after(1000, leb)

lbl2 = Label(window, text=" DIFF ")
lbl2.place(x=300, y=200)

lbl3 = Label(window, text=" OPTIMAL ")
lbl3.place(x=1200, y=200)

txt = Entry(window,width=50)
txt.place(x=600, y=360)

txt2 = Entry(window,width=50)
txt2.place(x=200, y=504)

txt3 = Entry(window,width=50)
txt3.place(x=1200, y=504)

files, plots1,plots2, val1, val2 = [],[],[],[],[]

def browse_button():
    filename = filedialog.askopenfilename()
    files.append(filename)
    temp = txt.get()
    txt.delete(0, len(temp))
    txt.insert(0, filename)
    return filename

def display(filename):
	print(filename, "a" )
	if filename == None:
		return
	# pp.start()
	print('starting')
	# an1['state'] ='disabled'
	r, mean, ranges = diff.dif(filename)
	# pp.stop()
	print('stopping')
	plots1.append((ranges, mean))
	val1.append(r[1])
	# temp = txt2.get()
	# txt2.delete(0, len(temp))
	# txt2.insert(0, r[1])
	# print(v)

def clicked(event):
	display(files[-1])

def display2(filename):
	print(filename, "b" )
	if filename == None:
		return
	# pp.start()
	print('starting')
	r, norm, ranges = diff.optical(filename)
	print('stopping')
	# pp.stop()
	plots2.append((ranges, norm))
	# temp = txt3.get()
	# txt3.delete(0, len(temp))
	# txt3.insert(0, r[1])
	val2.append(r[1])
	# print(v)


def clicked1(event):
	display2(files[-1])
	# print("working")


#new changes
def pre1():
	if len(files) == 0:
		return
	ved = cv2.VideoCapture(files[-1])
	while(ved.isOpened()):
		ret, frame = ved.read()
		print(ret)
		if ret == False:
			break
		gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
		cv2.imshow('Video1', gray)
		if cv2.waitKey(1) & 0xFF == ord('q'):
			break
	ved.release()
	cv2.destroyAllWindows()
	print("working")

def an1():
	print(val1[-1])
	temp = txt2.get()
	txt2.delete(0, len(temp))
	txt2.insert(0, val1[-1])

def an2():
	print(val2[-1])
	temp = txt3.get()
	txt3.delete(0, len(temp))
	txt3.insert(0, val2[-1])
	# print(val[-1])

def pop1():
	if len(plots1) == 0:
		return
	plt.bar(plots1[-1][0], plots1[-1][1],color="blue")
	# plt.figure(figsize=(4, 4))
	# thismanager = pylab.get_current_fig_manager()
	# thismanager.window.SetPosition((500, 0))
	plt.show()

def pop2():
	if len(plots2) == 0:
		return
	plt.bar(plots2[-1][0], plots2[-1][1],color="blue")
	# plt.figure(figsize=(4, 4))
	# thismanager = pylab.get_current_fig_manager()
	# thismanager.window.SetPosition((500, 0))
	plt.show()

pre1 = Button(window, text=" Preprocessing ", bg="cyan", fg="red", command=pre1)
pre1.place(x=710, y=90)

an1 = Button(window, text=" Analysis 1 ", bg="cyan", fg="red", command=an1)
an1.place(x=100, y=500)

an2 = Button(window, text=" Analysis 2 ", bg="cyan", fg="red", command=an2)
an2.place(x=1100, y=500)


pop1 = Button(window, text=" POPUP   1 ", bg="cyan", fg="red", command=pop1)
pop1.place(x=100, y=550)

pop2 = Button(window, text=" POPUP   2 ", bg="cyan", fg="red", command=pop2)
pop2.place(x=1100, y=550)

#end

v = StringVar()
button2 = Button(text="Browse ", command=browse_button).place(x=930, y=355)

btn2 = Button(window, text="Check for Forgery 2", bg="cyan", fg="red")
btn2.place(x=700, y=440)
btn2.bind('<Button-1>',clicked1)
# print("Yes")

btn = Button(window, text="Check for Forgery 1", bg="cyan", fg="red")
# btn.grid(column=6, row=6)
btn.place(x=700, y=400)
btn.bind('<Button-1>', clicked)

lbl = Label(window, text="")
# lbl.grid(column=0, row=1)
lbl.place(x=700, y=150)
# print(lbl, btn)

def update_time():
	lbl['text'] = time.strftime('Current time: %H:%M:%S')
	lbl.place(x=700,y=10)
	window.after(1000, update_time)

window.after(1000, update_time)
window.mainloop()