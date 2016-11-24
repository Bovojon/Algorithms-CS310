class Node:
	__slots__ = '_city', '_index'

	def __init__(self, city, index):
		self._city = city
		self._index = index

	def city(self):
		return self._city

	def index(self):
		return self._index

	def newCity(self, city):
		self._city = city
		return self._city



class Edge:
	__slots__ = '_origin', '_destination', '_value'

	
	def __init__(self, u, v, value):
	self._origin = u
	self._destination = v
	self._value = value

	def endpoints(self):
		return (self._origin, self._destination)

	def opposite(self, v):
		return self._destination.index if v is self._origin else self._origin.index

	def value(self):
		return self._value





