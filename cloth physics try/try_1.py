import pygame
dis = (500,500)
win = pygame.display.set_mode(dis)
white = (255,255,255)
black = (0,0,0)

class points:
	nodes = []
	def __init__(self,x,y,nodes):
		points.nodes.append(self)
		self.x = x
		self.y = y
		self.nodes = nodes
		self.size = 2
		self.pos = (self.x,self.y)
		for node in self.nodes:
			found = False
			for i in node.nodes:
				if i == self:
					found = True
			if found != True:
				node.nodes.append(self)

	def draw(self):
		pygame.draw.circle(win,white,(self.pos),self.size)

	def drawall():
		for node in points.nodes:
			node.draw()
			node.connector()

	def connector(self):
		for node in self.nodes:
			pygame.draw.line(win, white, (self.pos), (node.pos), 1)
	
	def movement(self, pos):
		self.x = pos[0]
		self.y = pos[1]
		self.pos = (self.x,self.y)
		for node in self.node():

def main():
	p0 = points(20,20,[]) #primary
	p1 = points(20,0,[p0])
	p2 = points(0,20,[p0])
	p3 = points(0,0,[p1,p0,p2])
	count = 0
	while True:
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				pygame.quit()
				quit()
			if pygame.mouse.get_pressed()[0]:
				p0.movement(pygame.mouse.get_pos())
		win.fill(black)
		points.drawall()
		pygame.display.update()

main()