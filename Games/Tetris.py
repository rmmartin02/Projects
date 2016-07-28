import pygame
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
		def __init__(self, color):
			self.color = color
			self.x = None
			self.y = None
		def __init__(self, color, x, y):
			self.color = color
			self.x = x
			self.y = y
		def drawTile(self):
			pygame.draw.rect(screen,self.color,[self.x,self.y,28,28])
	class Tetrimino:
		def __init__(self, letter):
			if letter == 'I':
				self.orient1 = [[TetrisBoard.Tile(CYAN),TetrisBoard.Tile(CYAN),TetrisBoard.Tile(CYAN),TetrisBoard.Tile(CYAN)]]
				self.orient2 = [[TetrisBoard.Tile(CYAN)],[TetrisBoard.Tile(CYAN)],[TetrisBoard.Tile(CYAN)],[TetrisBoard.Tile(CYAN)]]
				self.orientation = 1
				self.orientations = [self.orient1, self.orient2]
			if letter == 'J':
				self.orient1 = [[TetrisBoard.Tile(BLUE),TetrisBoard.Tile(BLUE),TetrisBoard.Tile(BLUE)],[None,None,TetrisBoard.Tile(BLUE)]]
				self.orient2 = [[None, TetrisBoard.Tile(BLUE)],[None, TetrisBoard.Tile(BLUE)],[TetrisBoard.Tile(BLUE), TetrisBoard.Tile(BLUE)]]
				self.orient3 = [[TetrisBoard.Tile(BLUE),None,None],[TetrisBoard.Tile(BLUE),TetrisBoard.Tile(BLUE),TetrisBoard.Tile(BLUE)]]
				self.orient4 = [[TetrisBoard.Tile(BLUE),TetrisBoard.Tile(BLUE)],[TetrisBoard.Tile(BLUE),None],[TetrisBoard.Tile(BLUE),None]]
			if letter == 'O':
				self.orient1 = [[TetrisBoard.Tile(YELLOW),TetrisBoard.Tile(YELLOW)],[TetrisBoard.Tile(YELLOW),TetrisBoard.Tile(YELLOW)]]
			if letter == 'L':
				self.orient1 = [[TetrisBoard.Tile(ORANGE),TetrisBoard.Tile(ORANGE),TetrisBoard.Tile(ORANGE)],[TetrisBoard.Tile(ORANGE),None,None]]
				self.orient2 = [[TetrisBoard.Tile(ORANGE),TetrisBoard.Tile(ORANGE)],[None,TetrisBoard.Tile(ORANGE)],[None,TetrisBoard.Tile(ORANGE)]]
				self.orient3 = [[None,None,TetrisBoard.Tile(ORANGE)],[TetrisBoard.Tile(ORANGE),TetrisBoard.Tile(ORANGE),TetrisBoard.Tile(ORANGE)]]
				self.orient4 = [[TetrisBoard.Tile(ORANGE),None],[TetrisBoard.Tile(ORANGE),None],[TetrisBoard.Tile(ORANGE),TetrisBoard.Tile(ORANGE)]]
			if letter == 'S':
				self.orient1 = [[None,TetrisBoard.Tile(GREEN),TetrisBoard.Tile(GREEN)],[TetrisBoard.Tile(GREEN),TetrisBoard.Tile(GREEN),None]]
				self.orient2 = [[TetrisBoard.Tile(GREEN),None],[TetrisBoard.Tile(GREEN),TetrisBoard.Tile(GREEN)],[None,TetrisBoard.Tile(GREEN)]]
			if letter == 'T':
				self.orient1 = [[TetrisBoard.Tile(PURPLE),TetrisBoard.Tile(PURPLE),TetrisBoard.Tile(PURPLE)],[None,TetrisBoard.Tile(PURPLE),None]]
				self.orient2 = [[None,TetrisBoard.Tile(PURPLE)],[TetrisBoard.Tile(PURPLE),TetrisBoard.Tile(PURPLE)],[None,TetrisBoard.Tile(PURPLE)]]
				self.orient3 = [[None,TetrisBoard.Tile(PURPLE),None],[TetrisBoard.Tile(PURPLE),TetrisBoard.Tile(PURPLE),TetrisBoard.Tile(PURPLE)]]
				self.orient4 = [[TetrisBoard.Tile(PURPLE),None],[TetrisBoard.Tile(PURPLE),TetrisBoard.Tile(PURPLE)],[TetrisBoard.Tile(PURPLE),None]]
			if letter == 'Z':
				self.orient1 = [[TetrisBoard.Tile(RED),TetrisBoard.Tile(RED),None],[None,TetrisBoard.Tile(RED),TetrisBoard.Tile(RED)]]
				self.orient2 = [[None,TetrisBoard.Tile(RED)],[TetrisBoard.Tile(RED),TetrisBoard.Tile(RED)],[TetrisBoard.Tile(RED),None]]
		def drawTetrimino(self):
			for tile in self.orientations[self.orientation]:
				print('hi')
	def __init__(self):
		self.score = 0
		self.tiles = [[TetrisBoard.Tile(WHITE, (screen_width/2-150+1)+(i*30), 10+1+(j*30)) for i in range(10)] for j in range(20)]
	def drawTetris(self):
		drawBoard(10,screen_width/2-150,20,10,30,BLACK)
		for row in self.tiles:
			for tile in row:
				tile.drawTile()
		
		

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
			print("User pressed a key.")
		elif event.type == pygame.KEYUP:
			print("User let go of a key.")
		elif event.type == pygame.MOUSEBUTTONDOWN:
			print("User pressed a mouse button")

	# --- Game logic should go here

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