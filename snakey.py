import tkinter as tk
import random

# Creates a list of frames and initialises them on a grid
gui= tk.Tk()
frame_grid = []
for x in range(0,40):
	frame_grid.append([])
	for y in range(0,40):
		frame_grid[x].append(y)

for x in range(0,40):
	for y in range(0,40):
		frame_grid[x][y] = tk.Frame(width=25,height=25,bg='green')
		frame_grid[x][y].grid(row=x, column=y)


frm_btn_left=tk.Frame()
frm_btn_left.grid(row=43,rowspan=5,column=7,columnspan=8)
frm_btn_down=tk.Frame()
frm_btn_down.grid(row=47,rowspan=5,column=15,columnspan=9)
frm_btn_up=tk.Frame()
frm_btn_up.grid(row=41,rowspan=5,column=15,columnspan=9)
frm_btn_right=tk.Frame()
frm_btn_right.grid(row=43,rowspan=5,column=25,columnspan=8)

def left():
	global mv_dir
	if last_move in ['up','down']:
		mv_dir='left'
	
def right():
	global mv_dir
	if last_move in ['up','down']:
		mv_dir='right'
		
def up():
	global mv_dir
	if last_move in ['left','right']:
		mv_dir='up'		
		
def down():
	global mv_dir
	if last_move in ['left','right']:
		mv_dir='down'		

btn_left=tk.Button(master=frm_btn_left,text='left', command=left)
btn_left.pack()
btn_down=tk.Button(master=frm_btn_down,text='down', command=down)
btn_down.pack()
btn_up=tk.Button(master=frm_btn_up,text='up', command=up)
btn_up.pack()
btn_right=tk.Button(master=frm_btn_right,text='right', command=right)
btn_right.pack()
		
# Adds a border
for x in range(0,40):
	for y in [0,39]:
		frame_grid[x][y].config(bg='black')
for x in [0,39]:
	for y in range(0,40):
		frame_grid[x][y].config(bg='black')		
		
mv_dir= 'up'
last_move='up'




fx=16
fy=16
oy=16
ox=16

def check_collision(xlist, ylist, xcheck, ycheck):
	if xcheck < 1 or xcheck>38 or \
		 ycheck<1 or ycheck>38:
		return True
	for i in range(0,len(xlist)-1):
		if xlist[i] == xcheck and ylist[i]==ycheck:
			return True
	return False		

def check_food_collision(foodx, foody, xcheck, ycheck):
	if foodx == xcheck and foody==ycheck:
		return True
	return False

def place_food(xlist, ylist):
	global fx
	global fy
	global ox
	global oy
	k=0
	while k==0:
		tx = random.randint(2,38)
		ty = random.randint(2,38)
		k=1
		for i in range(0, len(xlist)):
			if tx == xlist[i] and ty == ylist[i]:
				k=0
	ox = fx
	oy = fy
	fx = tx
	fy = ty	
		
class Snake:
	def __init__(self, name='snek?'):
		self.name = name
		self.xcoords = [11,12,13,14,15]
		self.ycoords = [11,11,11,11,11]
		self.oldx = 5
		self.oldy = 5

	def attempt_move(self):
		global last_move
		if mv_dir == 'up':
			new_x = self.xcoords[0] -1
			new_y = self.ycoords[0] 
		if mv_dir == 'down':
			new_x = self.xcoords[0] +1
			new_y = self.ycoords[0] 
		if mv_dir == 'left':
			new_x = self.xcoords[0] 
			new_y = self.ycoords[0] -1
		if mv_dir == 'right':
			new_x = self.xcoords[0]
			new_y = self.ycoords[0] +1		
		last_move = mv_dir
		if check_collision(self.xcoords, self.ycoords, new_x, new_y):
				gui.destroy()
				return #ends this instance of moveloop
		elif check_food_collision(fx, fy, new_x,new_y):
				place_food(self.xcoords,self.ycoords)
				self.xcoords.append(1)
				self.ycoords.append(1)

				##update snake coords with new position
		self.oldx = self.xcoords[-1]
		self.oldy= self.ycoords[-1]
				
		for i in range(len(self.xcoords),1,-1):
			self.xcoords[i-1] = self.xcoords[i-2]
			self.ycoords[i-1] = self.ycoords[i-2]
		self.xcoords[0] = new_x
		self.ycoords[0] = new_y
				
		gui_update(self)
		gui.after(200, self.attempt_move)
	

def gui_update(snake):
	frame_grid[snake.oldx][snake.oldy].config(bg='green')
	frame_grid[ox][oy].config(bg='green')
	gui.update()
	frame_grid[snake.xcoords[0]][snake.ycoords[0]].config(bg='red')	
	for i in range(1, len(snake.xcoords)):
		frame_grid[snake.xcoords[i]][snake.ycoords[i]].config(bg='black')
	frame_grid[fx][fy].config(bg='yellow')

sn = Snake()					
mv_dir='up'


place_food(sn.xcoords, sn.ycoords)

sn.attempt_move()
		
tk.mainloop()		

end_screen =tk.Tk()
death_lbl=tk.Label(text='game over')
death_lbl.pack()

tk.mainloop()
			
			
	
		





