class RingBuffer:
  def __init__(self, capacity):
    self.capacity = capacity
    self.current = 0
    self.storage = [None]*capacity

  def append(self, item):
    self.storage[self.current] = item
    if self.current +1  == self.capacity:
      self.current = 0
    else:
      self.current += 1
    # if self.current == self.storage:
    #   self.current = 0
    # self.storage[0] = item
    # self.current += 1

    

  def get(self):
    # if self.storage:
    #   return self.storage
    ar= []
    for i in range(self.capacity):
      if self.storage[i] != None:
        ar.append(self.storage[i])
    return ar
  

  # class RingBuffer:
	# def __init__(self,size_max):
	# 	self.max = size_max
	# 	self.data = []
	# def append(self,x):
	# 	"""append an element at the end of the buffer"""
	# 	self.data.append(x)
	# 	if len(self.data) == self.max:
	# 		self.cur=0
	# 		self.__class__ = RingBufferFull
	# def get(self):
  # 		""" return a list of elements from the oldest to the newest"""
	# 	return self.data


# class RingBufferFull:
# 	def __init__(self,n):
# 		raise "you should use RingBuffer"
# 	def append(self,x):		
# 		self.data[self.cur]=x
# 		self.cur=(self.cur+1) % self.max
# 	def get(self):
# 		return self.data[self.cur:]+self.data[:self.cur]
