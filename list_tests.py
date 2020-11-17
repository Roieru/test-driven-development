import unittest

#Rogelio Felix - A01634386
#Tarea Test Driven Development

class ListTest(unittest.TestCase):
	
    #Get the size of the list - Test 1
	def test_size_empty(self):
		list = []
		self.assertEqual(len(list), 0)
    
    #Get the size of the list - Test 2
	def test_size_normal(self):
		list = [1, 2, 3]
		self.assertEqual(len(list), 3)

    #Get the size of the list - Test 3
	def test_size_none(self):
		list = None
		with self.assertRaises(TypeError):
			len(list)

    #Clear the list - Test 1
	def test_clear_normal(self):
		list = [1, 2, 3]
		list.clear()
		self.assertEqual(len(list), 0)

    #Clear the list - Test 2
	def test_clear_empty(self):
		list = []
		list.clear()
		self.assertEqual(len(list), 0)

    #Clear the list - Test 3
	def test_clear_none(self):
		list = None
		with self.assertRaises(AttributeError):
			list.clear()

    #Add items - Test 1
	def test_append_normal(self):
		list = []
		list.append(1)
		list.append(2)
		list.append(3)
		self.assertEqual(len(list), 3)

    #Add items - Test 2
	def test_append_noneElement(self):
		list = []
		list.append(None)
		self.assertEqual(len(list), 1)

    #Add items - Test 3
	def test_append_none(self):
		list = None
		with self.assertRaises(AttributeError):
			list.append(1)

    #Item exists - Test 1
	def test_exists_normal(self):
		list = [1, 2, 3]
		self.assertTrue(list.count(1) > 0)

    #Item exists - Test 2
	def test_exists_notPresent(self):
		list = [1, 2, 3]
		self.assertFalse(list.count(4) > 0)

    #Item exists - Test 3
	def test_exists_none(self):
		list = None
		with self.assertRaises(AttributeError):
			list.count(1) > 0

    #Get element by index - Test 1
	def test_getByIndex_normal(self):
		list = [0, 1, 2]
		self.assertEqual(list[0], 0)

    #Get element by index - Test 2
	def test_getByIndex_notValid(self):
		list = [0, 1, 2]
		with self.assertRaises(TypeError):
			list['a']

    #Get element by index - Test 3
	def test_getByIndex_none(self):
		list = None
		with self.assertRaises(TypeError):
			list[0]

    #Get index of object - Test 1
	def test_index_normal(self):
		list = [0, 1, 2]
		self.assertEqual(list.index(0), 0)

    #Get index of object - Test 2
	def test_index_multiple(self):
		list = [0, 0, 0]
		self.assertEqual(list.index(0), 0)

    #Get index of object - Test 3
	def test_index_notPresent(self):
		list = [0, 1, 2]
		with self.assertRaises(ValueError):
			list.index(3)

    #Remove by index - Test 1
	def test_pop_normal(self):
		list = [0, 1, 2]
		list.pop(0)
		self.assertEqual(len(list), 2)
		self.assertFalse(list.count(0) > 0)
		self.assertNotEqual(list[0], 0)

    #Remove by index - Test 2
	def test_pop_invalid(self):
		list = [0]
		with self.assertRaises(TypeError):
			list.pop('a')

    #Remove by index - Test 3
	def test_pop_none(self):
		list = None
		with self.assertRaises(AttributeError):
			list.pop(0)


if __name__ == '__main__':
	unittest.main()