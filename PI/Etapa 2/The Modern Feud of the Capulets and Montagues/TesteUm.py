#Teste para The Modern Feud of the Capulets and Montagues

import unittest
from main import matrizes
from main import dividir_familias
from main import to_int
from main import menor

class TesteUm(unittest.TestCase):
	
	def setUp(self):
		self.cases = {
			"teste_um_matrizes.txt": [['9', '0', '0'], ['6', '3', '1'], ['6', '0', '0'], ['9', '3', '1'], ['6', '6', '0'], ['0', '7', '1'], ['3', '1', '0'], ['9', '9', '1'], ['2', '9', '0'], ['0', '9', '0']],
			"teste_dois_matrizes.txt": [['11', '0', '0'], ['6', '25', '1'], ['0', '0', '0'], ['1', '1', '1']],
			"teste_tres_matrizes.txt": [['12', '166', '0'], ['6', '100', '1'], ['242', '0', '0'], ['900', '1', '1']] }

	def test_1(self):
		for file_name, expected in self.cases.items():
			self.assertEqual(matrizes(file_name), expected)

	def tearDown(self):
		self.cases = None
	
	def test_2(self):

		case1_1, case1_2 = dividir_familias([['9', '0', '0'], ['6', '3', '1'], ['6', '0', '0'], ['9', '3', '1'], ['6', '6', '0'], ['0', '7', '1'], ['3', '1', '0'], ['9', '9', '1'], ['2', '9', '0'], ['0', '9', '0']])
		case2_1, case2_2 = dividir_familias([['11', '0', '0'], ['6', '25', '1'], ['0', '0', '0'], ['1', '1', '1']])
		case3_1, case3_2 = dividir_familias([['12', '166', '0'], ['6', '100', '1'], ['242', '0', '0'], ['900', '1', '1']])	
		
		expected1_1 = [['9', '0', '0'], ['6', '0', '0'], ['6', '6', '0'], ['3', '1', '0'], ['2', '9', '0'], ['0', '9', '0']]
		expected1_2 = [['6', '3', '1'], ['9', '3', '1'], ['0', '7', '1'], ['9', '9', '1']]
		expected2_1 = [['11', '0', '0'], ['0', '0', '0']]
		expected2_2 = [['6', '25', '1'], ['1', '1', '1']]
		expected3_1 = [['12', '166', '0'], ['242', '0', '0']] 
		expected3_2 = [['6', '100', '1'], ['900', '1', '1']]

		self.assertEqual(case1_1, expected1_1)
		self.assertEqual(case1_2, expected1_2)
		self.assertEqual(case2_1, expected2_1)
		self.assertEqual(case2_2, expected2_2)
		self.assertEqual(case3_1, expected3_1)
		self.assertEqual(case3_2, expected3_2)

	def test_3(self):

		case1 = menor([[9, 0, 0], [6, 0, 0], [6, 6, 0], [3, 1, 0], [2, 9, 0], [0, 9, 0]], [[6, 3, 1], [9, 3, 1], [0, 7, 1], [9, 9, 1]])
		case2 = menor([[11, 0, 0], [0, 0, 0]], [[6, 25, 1], [1, 1, 1]])
		case3 = menor([[12, 166, 0], [242, 0, 0]], [[6, 100, 1], [900, 1, 1]]) 

		self.assertEqual(case1, 2)
		self.assertEqual(case2, 2)
		self.assertEqual(case3, 72)

	def test_4(self):

		case1_1, case1_2 = to_int([['9', '0', '0'], ['6', '0', '0'], ['6', '6', '0'], ['3', '1', '0'], ['2', '9', '0'], ['0', '9', '0']], [['6', '3', '1'], ['9', '3', '1'], ['0', '7', '1'], ['9', '9', '1']])
		case2_1, case2_2 = to_int([['11', '0', '0'], ['0', '0', '0']], [['6', '25', '1'], ['1', '1', '1']])
		case3_1, case3_2 = to_int([['12', '166', '0'], ['242', '0', '0']], ([['6', '100', '1'], ['900', '1', '1']])) 

		expected1_1 = [[9, 0, 0], [6, 0, 0], [6, 6, 0], [3, 1, 0], [2, 9, 0], [0, 9, 0]]
		expected1_2 = [[6, 3, 1], [9, 3, 1], [0, 7, 1], [9, 9, 1]]
		expected2_1 = [[11, 0, 0], [0, 0, 0]]
		expected2_2 = [[6, 25, 1], [1, 1, 1]]
		expected3_1 = [[12, 166, 0], [242, 0, 0]] 
		expected3_2 = [[6, 100, 1], [900, 1, 1]]

		self.assertEqual(case1_1, expected1_1)
		self.assertEqual(case1_2, expected1_2)
		self.assertEqual(case2_1, expected2_1)
		self.assertEqual(case2_2, expected2_2)
		self.assertEqual(case3_1, expected3_1)
		self.assertEqual(case3_2, expected3_2)

if __name__=="__main__":
	unittest.main()
