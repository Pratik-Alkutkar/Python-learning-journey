# 1 
class X1: 
	a = 10 
	b = 20 
	c = a + b 
	L = [10, 20, 30, 40]
	for x in L: 
		print(x) 

print(X1.__dict__)
# 'a':10, 'b':20, 'c':30, 'L':[10,20,30,40], 'x':40

#2 
class X2: 
	def f1(): 
		print("In X2.f1()")

	def f2(): 
		print("In X2.f2()")

	num = 100 
	n = 500 

print(X2.__dict__)

# 'f1': function object, 'f2': function object 
# 'num': 100, 'n':500

# 3 
class Date: 
	def __init__(self, init_day, init_month, init_year): 
		self.day = init_day 
		self.month = init_month 
		self.year = init_year 

	def get_day(self): 
		return self.day 

	def get_month(self): 
		return self.month 

	def get_year(self): 
		return self.year 

	def set_day(self, new_day): 
		self.day = new_day 

	def set_month(self, new_month): 
		self.month = new_month 

	def set_year(self, new_year): 
		self.year = new_year 

print(Date.__init__)
# '__init__' : function object 
# 'get_day' : function object
# 'get_month' : function object
# 'get_year': function object
# 'set_day': function object
# 'set_month': function object
# 'set_year': : function object

# 4 

class X3: 
	a = 100 
	b = 200 
	def func(): 
		print("In X3.func")

	def test(msg): 
		print(msg)

print("X3.__dict__")
# 'a': 100, 'b':200, 'func': function object 
# 'test' : function object 

# 5 

class list: 
	class node: 
		def __init__(self, new_data): 
			self.data = new_data 
			self.prev = None 
			self.next = None 

	def __init__(self): 
		self.head_node = list.node(-1)
		self.head_node.prev = self.head_node 
		self.head_node.next = self.head_node 

	@staticmethod 
	def generic_insert(beg, mid, end): 
		mid.next = end 
		mid.prev = beg 
		beg.next = mid 
		end.prev = mid 

	def insert_end(self, new_data): 
		list.generic_insert(self.head_node.prev,
							list.node(new_data), 
							self.head_node)
		return True 

print(list.__dict__)

# 'node': type object 
# '__init__' : function object 
# 'generic_insert' : function object 
# 'insert_end' : function object 