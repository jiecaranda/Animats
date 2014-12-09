from cell import *
from animats import *
from food import *

class Environment():
	def __init__(self, w, h):
		self.width = w
		self.height = h
		self.grids =  [[None for col in range(w)] for row in range(h)]
		self.initGrids(w, h)
		self.animats = []
		self.foods = []
		self.nonfoods = []

	def initGrids(self, w, h):
		for i in range(w):
			for j in range(h):
				if i == 0 or j ==0 or i == w-1 or j == h-1:
					self.grids[i][j] = Wall()
				else:
					self.grids[i][j] = Road()

	def createAnimats(self):
		a = Animat(9,9, self)
		self.animats.append(a)
		#a = Animat(21,21, self)
		#self.animats.append(a)

	def createFoods(self, num):
		for i in range(num):
			self.foods.append(Food(i*5+1, i*5+1))

	def createNonFoods(self, num):
		for i in range(num):
			self.nonfoods.append(NonFood(i*5, self.height - i*5))

	def update(self):
		for i in range(len(self.animats)):
			self.animats[i].update(self.foods, self.nonfoods)

		for i in range(len(self.animats)):
			if i >= len(self.animats):
				break
			if self.animats[i].energy <= 0:
				self.animats[i].ai.printQ()
				self.animats.pop(i)




