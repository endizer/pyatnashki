import random
class Map:
	"""docstring for Map"""
	def __init__(self, size = 4):
		#Инициализация переменных
		super(Map, self).__init__()
		self.size = size
		self.time = 0
		self.moveCount = 0
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
			
		self.out()
		self.index(inputNum(0, self.size**2 - 1, 'Введите число '))
	
	def search(self, numb):
		#Ищет координаты числа numb
		return self.map.index(numb)%self.size, int(self.map.index(numb)/self.size)
		

	def index(self, numb):
		if len(numb) == 1:
			numb = '0'+numb
		return self.move(self.search(numb))
		

	def move(self, coord):
		#Сдвиг ячейки/цифры
		print (coord)
		zero = self.search('00')
		if (zero[0] == coord[0] or zero[1] == coord[1]) and zero != coord:
			if zero[1] == coord[1]:
				#Сдвиг по x (строка)
				del self.mapDuo[zero[1]][zero[0]]
				self.mapDuo[coord[1]].insert(coord[0], '00')
				self.out()
			else:
				#Сдвиг по y (столбец)
				y = zero[1]
				slide = 0
				if y < coord[1]:
					slide = 1
				else:
					slide = -1
				while y != coord[1]:
					self.mapDuo[y][coord[0]] = self.mapDuo[y + slide][coord[0]]
					y += slide
				else:
					self.mapDuo[coord[1]][coord[0]] = '00'
				self.out()
		else:
			print('Данное число нельзя сдвинуть')

		self.index(inputNum(0, self.size**2 - 1, 'Введите число '))

	def out(self):
		#Вывод на экран
		print('\n\n\n')
		self.map = []
		for i in range(0, self.size):
			print(self.mapDuo[i])
			self.map += self.mapDuo[i]
		self.winner()

	def winner(self):
		for i in range(0, self.size - 1):
			if self.map[i] != i + 1:
				return 0
		print("Победа!")



def start():
	size = inputNum(3, 10, 'Введите размерность поля (от 3 до 10)\n')
	map = Map(int(size))

def inputNum(a, b, text):
	#Ввод чисел с проверкой
	numb = input(text)
	try:
		numb = int(numb)
		if numb < a or numb > b:
			print('Введите другое число')
			return inputNum(a, b, text)
		else:
			return str(numb)
	except ValueError:
		print('Вы ввели не число')
		return inputNum(a, b, text)
	
start()
input()