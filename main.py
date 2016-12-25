import random
from tkinter import *


class Map:
	"""docstring for Map"""
	def __init__(self, size = 4):
		#Инициализация переменных
		super(Map, self).__init__()
		self.size = size
		self.map = []
		#Инициализация поля
		for i in range(0, self.size**2):
			if i < 10:
				self.map.append('0' + str(i))
			else:
				self.map.append(str(i))
		#Перемешка
		random.shuffle(self.map)
		#Создание двумерного массива
		self.mapDuo = []
		for i in range(0, self.size):
			self.mapDuo.append(self.map[i*self.size:(i+1)*self.size])
		self.zero = self.search('00')	
		

	def search(self, numb):
		#Ищет координаты числа numb
		return int(self.map.index(numb)/self.size), self.map.index(numb)%self.size
		

def swap(x, y):
	global zeroX
	global zeroY
	if not((x < 0 or x >= map.size) or (y < 0 or y >= map.size)):
		massButt[zeroY][zeroX]['text'] = massButt[y][x]['text']
		massButt[y][x]['text'] = '00'
		massButt[zeroY][zeroX].grid()
		massButt[y][x].grid_remove()
		zeroX = x
		zeroY = y
		


def up(Event):
	swap(zeroX, zeroY - 1)

def down(Event):
	swap(zeroX, zeroY + 1)

def left(Event):
	swap(zeroX - 1, zeroY)

def right(Event):
	swap(zeroX + 1, zeroY)


map = Map(4)

#Создание визуальной формы
root = Tk()
massButt = []
#Выставление на визуальную форму кнопок
for i in range(0, map.size):
	massButt.append([])
	for j in range(0, map.size):
		massButt[i].append(Button(root, 
			text = map.mapDuo[i][j], 
			width=10, height=5))
		massButt[i][j].grid(row = i, column = j)

#Скрытие элемента "00"
zeroX = map.zero[1]
zeroY = map.zero[0]

massButt[zeroY][zeroX].grid_remove()
#Цвет поля
root['background'] = 'grey'
#Движение
root.bind("<Up>", up)
root.bind("<Down>", down)
root.bind("<Left>", left)
root.bind("<Right>", right)
root.mainloop()



exit()
