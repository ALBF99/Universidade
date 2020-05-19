import unittest
from problemSetter import leitura, divisao, ordenar, verificar_abertos, remover_equipas, deadline_maisProximo, verificar_data, decrementar, main

def read_file(x):
	f = open(x, "r")
	a = f.read().splitlines()
	f.close()
	return a

def make_testcase(n):
	x = read_file(n)
	return x
	

class problemSetterTests(unittest.TestCase):
	def setUp(self):
		self.leitura_cases = ["input1.txt","input2.txt"]

		self.divisao_cases = [((['6', '2 9 11', '2 5 13', '3 2 7', '1 11 16', '1 4 9', '3 1 6']),
			([[6], [2, 9, 11], [2, 5, 13], [3, 2, 7], [1, 11, 16], [1, 4, 9], [3, 1, 6]]))]

		self.ordenar_cases = [(([[2,9,11],[2,5,13],[3,2,7],[1,11,16],[1,4,9],[3,1,6]]),
			([[3,1,6],[3,2,7],[1,4,9],[2,5,13],[2,9,11],[1,11,16]])),
			(([[1,20,20],[2,5,7],[1,7,9],[2,4,8],[1,3,5],[1,2,3],[1,9,10],[4,15,18]]),
			([[1,2,3],[1,3,5],[2,4,8],[2,5,7],[1,7,9],[1,9,10],[4,15,18],[1,20,20]]))]

		self.verificar_abertos_cases = [((1, ([[3,1,6],[3,2,7],[1,4,9],[2,5,13],[2,9,11],[1,11,16]]), ([])),([[3,1,6]])),
			((2,([[1,2,3],[1,3,5],[2,4,8],[2,5,7],[1,7,9],[1,9,10],[4,15,18],[1,20,20]]),([])),([[1,2,3]]))]

		self.remover_equipas_cases = [
			((([3,1,6]),([[3,1,6],[3,2,7],[1,4,9],[2,5,13],[2,9,11],[1,11,16]])),([[3,2,7],[1,4,9],[2,5,13],[2,9,11],[1,11,16]])),
			((([1,2,3]),([[1,2,3],[1,3,5],[2,4,8],[2,5,7],[1,7,9],[1,9,10],[4,15,18],[1,20,20]])),([[1,3,5],[2,4,8],[2,5,7],[1,7,9],[1,9,10],[4,15,18],[1,20,20]]))]

		self.deadline_maisProximo_cases = [(([[3,1,6],[3,2,7]]),([3,1,6])),
			(([[1,2,3]]),([1,2,3]))]

		self.verificar_data_cases = [((1,[[3,1,6]]),(0)),
			((3,[[1,2,3]]),(1))]

		self.decrementar_cases = [(([[3,1,6],[3,2,7],[1,4,9]]),([[2,1,6],[2,2,7],[0,4,9]])),
			(([[1,2,3]]),([[0,2,3]]))]

		self.main_cases = [(("input1.txt"),(5)),(("input2.txt"),(9))]


	def test_leitura(self):
		for n in self.leitura_cases:
			x = make_testcase(n)
			self.assertEqual(leitura(n), x)

	def test_divisao(self):
		for (x, e) in self.divisao_cases:
			self.assertEqual(divisao(x), e)

	def test_ordenar(self):
		for (x, e) in self.ordenar_cases:
			self.assertEqual(ordenar(x), e)

	def test_verificar_abertos(self):
		for (x, e) in self.verificar_abertos_cases:
			self.assertEqual(verificar_abertos(*x), e)

	def test_remover_equipas(self):
		for (x, e) in self.remover_equipas_cases:
			self.assertNotEqual(remover_equipas(*x), e)

	def test_deadline_maisProximo(self):
		for (x, e) in self.deadline_maisProximo_cases:
			self.assertEqual(deadline_maisProximo(x), e)

	def test_verificar_data(self):
		for (x, e) in self.verificar_data_cases:
			self.assertEqual(verificar_data(*x), e)

	def test_decrementar(self):
		for (x, e) in self.decrementar_cases:
			self.assertEqual(decrementar(x), e)

	def test_main(self):
		for (x, e) in self.main_cases:
			self.assertEqual(main(x), e)

if __name__=='__main__':
	unittest.main()