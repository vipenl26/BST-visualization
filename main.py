import pygame


pygame.init()
pygame.display.set_mode((1280,680))
pygame.display.set_caption('BST Visualization')
screen=pygame.display.get_surface()

screen.fill((255,255,255))
clock = pygame.time.Clock()
class Node:
	def __init__(self,n):
		self.data=n
		self.left=None
		self.right=None

class BST:
	def __init__(self):
		self.head=None
	def push_util(self,current,data):
		if(current==None):
			return Node(data)

		if current.data>data:
			self.moveLeft(data)
			current.left=self.push_util(current.left,data)
		elif current.data<data:
			self.moveRight(data)
			current.right=self.push_util(current.right,data)
		return current

	def push(self,data):
		self.px=640
		self.py=30
		self.a=0
		self.b=1280
		self.head=self.push_util(self.head,data)

	def moveLeft(self,data):
		self.b=(self.a+self.b)//2
		nx=(self.a+self.b)//2
		ny=self.py+150
		moveNode(data,self.px,self.py,nx,ny)
		self.px=nx
		self.py=ny
	def moveRight(self,data):
		self.a=(self.a+self.b)//2
		nx=(self.a+self.b)//2
		ny=self.py+150
		moveNode(data,self.px,self.py,nx,ny)
		self.px=nx
		self.py=ny



def draw(n,x,y):
	shift_x=12
	shift_y=18
	if n>9: shift_x+=10
	
	pygame.draw.circle(screen,(0,0,255),(x,y),30)
	font=pygame.font.SysFont(None,60)
	screen_text=font.render(str(n),True,(0,0,0))
	screen.blit(screen_text,[x-shift_x,y-shift_y])

def frame_update():
	screen.fill((255,255,255))
	drawBST(0,1280,bt.head)
	pygame.display.update()

def moveNode(n,sx,sy,fx,fy):
	m=(fy-sy)/(fx-sx)
	c=sy - m*sx
	step=5 if sx<fx else -5
	for x in range(sx,fx,step):
		y=m*x+c
		draw(n,x,y)
		pygame.display.update()
		clock.tick(30)
		frame_update()



def drawBST(a,b,node,prex=0,prey=0,y=30):
	if(node==None):
		return
	if y!=30:
		pygame.draw.line(screen,(0,0,0),(prex,prey),((a+b)//2,y))
	draw(node.data,(a+b)//2,y)
	drawBST(a,(a+b)//2,node.left,(a+b)//2,y,y+150)
	drawBST((a+b)//2,b,node.right,(a+b)//2,y,y+150)


bt = BST()
bt.push(5)
bt.push(4)
bt.push(8)
bt.push(7)
bt.push(9)
bt.push(6)
bt.push(2)
bt.push(1)
bt.push(3)
bt.push(10)
# bt.push(-1)
drawBST(0,1280,bt.head)

while 1:
	for event in pygame.event.get():
		if event.type==pygame.QUIT:
			pygame.quit()
			exit()
	pygame.display.update()