import pygame
import random
pygame.init()

BLACK = (0,0,0)
WHITE = (255,255,255)
GREEN = (0,255,0)
RED = (255,0,0)
BLUE = (0,0,255)
YELLOW = (255,255,0)
CYAN = (0,255,255)
PURPLE = (76,0,153)
ORANGE = (204,102,0)


screen_width = 500
screen_height = 620
screen = pygame.display.set_mode([screen_width, screen_height])

pygame.display.set_caption("Makoa's Tetris")

def drawSquare(x,y,s,color):
	pygame.draw.rect(screen, color, [x,y,s,s])
	
def drawBoard(top,left,height,width,s,color):
	height
	width
	#vertical
	for w in range(width):
		pygame.draw.line(screen, color , [left + w*s, top], [left + w*s, height*s+top])
	pygame.draw.line(screen, color , [left + (width)*s, top], [left + (width)*s, height*s+top])
	#horizontal
	for h in range(height):
		pygame.draw.line(screen, color, [left, top + h*s], [width*s+left, top + h*s])
	pygame.draw.line(screen, color, [left, top + height*s], [width*s+left, top + height*s])
	
class TetrisBoard:
	class Tile:
		def __init__(self, color, x = None, y = None):
			self.color = color
			self.x = x
			self.y = y
		def draw(self):
			pygame.draw.rect(screen,self.color,[(screen_width/2-150+1)+(self.x*30),10+1+(self.y*30),28,28])
	class Tetrimino:
		def __init__(self):
			letterList = ['I', 'J', 'O', 'L', 'S', 'T', 'Z']
			letter = letterList[random.randint(0,len(letterList)-1)]
			if letter == 'I':
				self.orient1 = [[TetrisBoard.Tile(CYAN),TetrisBoard.Tile(CYAN),TetrisBoard.Tile(CYAN),TetrisBoard.Tile(CYAN)]]
				
				self.orient2 = [[TetrisBoard.Tile(CYAN)],
									[TetrisBoard.Tile(CYAN)],
									[TetrisBoard.Tile(CYAN)],
									[TetrisBoard.Tile(CYAN)]]
				self.orientation = 0
				self.x = 3
				self.y = 0
				self.orientations = [self.orient1, self.orient2]
				for orientation in self.orientations:
					for i in range(len(orientation)):
						for j in range(len(orientation[i])):
							if orientation[i][j] is not None:
								orientation[i][j].x = self.x + i
								orientation[i][j].y = self.y + j
			if letter == 'J':
				self.orient1 = [[TetrisBoard.Tile(BLUE),TetrisBoard.Tile(BLUE),TetrisBoard.Tile(BLUE)],
									[None,None,TetrisBoard.Tile(BLUE)]]
									
				self.orient2 = [[None, TetrisBoard.Tile(BLUE)],
									[None, TetrisBoard.Tile(BLUE)],
									[TetrisBoard.Tile(BLUE), TetrisBoard.Tile(BLUE)]]
									
				self.orient3 = [[TetrisBoard.Tile(BLUE),None,None],
									[TetrisBoard.Tile(BLUE),TetrisBoard.Tile(BLUE),TetrisBoard.Tile(BLUE)]]
									
				self.orient4 = [[TetrisBoard.Tile(BLUE),TetrisBoard.Tile(BLUE)],
									[TetrisBoard.Tile(BLUE),None],
									[TetrisBoard.Tile(BLUE),None]]
				self.orientation = 0
				self.x = 3
				self.y =0
				self.orientations = [self.orient1, self.orient2, self.orient3, self.orient4]
				for orientation in self.orientations:
					for i in range(len(orientation)):
						for j in range(len(orientation[i])):
							if orientation[i][j] is not None:
								orientation[i][j].x = self.x + i
								orientation[i][j].y = self.y + j
			if letter == 'O':
				self.orient1 = [[TetrisBoard.Tile(YELLOW),TetrisBoard.Tile(YELLOW)],
									[TetrisBoard.Tile(YELLOW),TetrisBoard.Tile(YELLOW)]]
				self.orientation = 0
				self.x = 3
				self.y = 0
				self.orientations = [self.orient1]
				for orientation in self.orientations:
					for i in range(len(orientation)):
						for j in range(len(orientation[i])):
							if orientation[i][j] is not None:
								orientation[i][j].x = self.x + i
								orientation[i][j].y = self.y + j
			if letter == 'L':
				self.orient1 = [[TetrisBoard.Tile(ORANGE),TetrisBoard.Tile(ORANGE),TetrisBoard.Tile(ORANGE)],
									[TetrisBoard.Tile(ORANGE),None,None]]
								
				self.orient2 = [[TetrisBoard.Tile(ORANGE),TetrisBoard.Tile(ORANGE)],
									[None,TetrisBoard.Tile(ORANGE)],
									[None,TetrisBoard.Tile(ORANGE)]]
									
				self.orient3 = [[None,None,TetrisBoard.Tile(ORANGE)],
									[TetrisBoard.Tile(ORANGE),TetrisBoard.Tile(ORANGE),TetrisBoard.Tile(ORANGE)]]
									
				self.orient4 = [[TetrisBoard.Tile(ORANGE),None],
									[TetrisBoard.Tile(ORANGE),None],
									[TetrisBoard.Tile(ORANGE),TetrisBoard.Tile(ORANGE)]]
				self.orientation = 0
				self.x = 3
				self.y = 0
				self.orientations = [self.orient1, self.orient2, self.orient3, self.orient4]
				for orientation in self.orientations:
					for i in range(len(orientation)):
						for j in range(len(orientation[i])):
							if orientation[i][j] is not None:
								orientation[i][j].x = self.x + i
								orientation[i][j].y = self.y + j
			if letter == 'S':
				self.orient1 = [[None,TetrisBoard.Tile(GREEN),TetrisBoard.Tile(GREEN)],
									[TetrisBoard.Tile(GREEN),TetrisBoard.Tile(GREEN),None]]
									
				self.orient2 = [[TetrisBoard.Tile(GREEN),None],
									[TetrisBoard.Tile(GREEN),TetrisBoard.Tile(GREEN)],
									[None,TetrisBoard.Tile(GREEN)]]
				self.orientation = 0
				self.x = 3
				self.y = 0
				self.orientations = [self.orient1, self.orient2]
				for orientation in self.orientations:
					for i in range(len(orientation)):
						for j in range(len(orientation[i])):
							if orientation[i][j] is not None:
								orientation[i][j].x = self.x + i
								orientation[i][j].y = self.y + j
			if letter == 'T':
				self.orient1 = [[TetrisBoard.Tile(PURPLE),TetrisBoard.Tile(PURPLE),TetrisBoard.Tile(PURPLE)],
									[None,TetrisBoard.Tile(PURPLE),None]]
									
				self.orient2 = [[None,TetrisBoard.Tile(PURPLE)],
									[TetrisBoard.Tile(PURPLE),TetrisBoard.Tile(PURPLE)],
									[None,TetrisBoard.Tile(PURPLE)]]
									
				self.orient3 = [[None,TetrisBoard.Tile(PURPLE),None],
									[TetrisBoard.Tile(PURPLE),TetrisBoard.Tile(PURPLE),TetrisBoard.Tile(PURPLE)]]
									
				self.orient4 = [[TetrisBoard.Tile(PURPLE),None],
									[TetrisBoard.Tile(PURPLE),TetrisBoard.Tile(PURPLE)],
									[TetrisBoard.Tile(PURPLE),None]]
				self.orientation = 0
				self.x = 3
				self.y = 0
				self.orientations = [self.orient1, self.orient2, self.orient3, self.orient4]
				for orientation in self.orientations:
					for i in range(len(orientation)):
						for j in range(len(orientation[i])):
							if orientation[i][j] is not None:
								orientation[i][j].x = self.x + i
								orientation[i][j].y = self.y + j
			if letter == 'Z':
				self.orient1 = [[TetrisBoard.Tile(RED),TetrisBoard.Tile(RED),None],
									[None,TetrisBoard.Tile(RED),TetrisBoard.Tile(RED)]]
				self.orient2 = [[None,TetrisBoard.Tile(RED)],
									[TetrisBoard.Tile(RED),TetrisBoard.Tile(RED)],
									[TetrisBoard.Tile(RED),None]]
				self.orientation = 0
				self.x = 3
				self.y = 0
				self.orientations = [self.orient1, self.orient2]
				for orientation in self.orientations:
					for i in range(len(orientation)):
						for j in range(len(orientation[i])):
							if orientation[i][j] is not None:
								orientation[i][j].x = self.x + i
								orientation[i][j].y = self.y + j
		def updatePosition(self,x,y):
			if (self.x + x) >= 0 and (self.x+len(self.orientations[self.orientation]) + x) <=  10:
				self.x = self.x + x
			self.y = self.y + y
			for orientation in self.orientations:
				for i in range(len(orientation)):
					for j in range(len(orientation[i])):
						if orientation[i][j] is not None:
							orientation[i][j].x = self.x + i 
							orientation[i][j].y = self.y + j
		def updateOrientation(self):
			orientation = (self.orientation+1) % len(self.orientations)
			if (self.x+len(self.orientations[orientation])) <= 10:
				self.orientation = orientation
			for orientation in self.orientations:
				for i in range(len(orientation)):
					for j in range(len(orientation[i])):
						if orientation[i][j] is not None:
							orientation[i][j].x = self.x + i 
							orientation[i][j].y = self.y + j
		def draw(self):
			for row in self.orientations[self.orientation]:
				for tile in row:
					if tile is not None:
						tile.draw()
	def __init__(self):
		self.score = 0
		self.tetrimino = self.Tetrimino()
		self.tiles = [[TetrisBoard.Tile(WHITE, i, j) for i in range(10)] for j in range(20)]
	def hasHit(self):
		for tile in self.tetrimino.orientations[self.tetrimino.orientation]:
			if tile is not None:
				if tile.y == 20:
					return True
				else:
					print(len(self.tetrimino.orientations[self.tetrimino.orientation][-1]))
					for next in range(tile.x, tile.x + len(self.tetrimino.orientations[self.tetrimino.orientation])):
						if self.tiles[tile.y+1][next] is not None:
							if self.tiles[tile.y+1][next].color is not WHITE:
								return True
		return False
	def updateBoard(self):
		if self.hasHit():
			for i in range(len(self.tetrimino.orientations[tetrimino.orientation])):
				for j in range(len(self.tetrimino.orientations[tetrimino.orientation][i])):
					self.tiles[i][j] = self.tetrimino.orientations[tetrimino.orientation][i][j]
			self.tetrimino = self.Tetrimino()
	def drawTetris(self):
		drawBoard(10,screen_width/2-150,20,10,30,BLACK)
		for row in self.tiles:
			for tile in row:
				tile.draw()
		self.tetrimino.draw()
		

# Loop until the user clicks the close button.
done = False
 
# Used to manage how fast the screen updates
clock = pygame.time.Clock()
 
Tetris = TetrisBoard()
# -------- Main Program Loop -----------
while not done:
	# --- Main event loop
	for event in pygame.event.get(): # User did something
		if event.type == pygame.QUIT:
			print("User asked to quit.")
			pygame.quit()
		elif event.type == pygame.KEYDOWN:
			if event.key == pygame.K_LEFT:
				Tetris.tetrimino.updatePosition( -1, 0)
			elif event.key == pygame.K_RIGHT:
				Tetris.tetrimino.updatePosition(1, 0)
			elif event.key == pygame.K_UP:
				Tetris.tetrimino.updateOrientation()
			elif event.key == pygame.K_DOWN:
				print("User pressed a key.")
				Tetris.tetrimino.updatePosition(0, 1)
		elif event.type == pygame.KEYUP:
			print("User let go of a key.")
		elif event.type == pygame.MOUSEBUTTONDOWN:
			print("User pressed a mouse button")

	# --- Game logic should go here
	Tetris.updateBoard()
	# --- Drawing code should go here
	# First, clear the screen to white. Don't put other drawing commands
	# above this, or they will be erased with this command.
	screen.fill(BLACK)
	drawBoard(10,screen_width/2-150,20,10,30,WHITE)
	Tetris.drawTetris()

	# --- Go ahead and update the screen with what we've drawn.
	pygame.display.flip()

	# --- Limit to 60 frames per second
	clock.tick(60)