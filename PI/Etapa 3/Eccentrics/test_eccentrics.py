import unittest
from eccentrics import leitura, criar_camadas, main

def read_file(x):
	f = open(x, "r")
	a = f.read().splitlines()
	f.close()
	return a

def make_testcase(n):
	x = read_file(f"input{n}.txt")
	e = read_file(f"output{n}.txt")
	return (x, e)


class EccentricsTests(unittest.TestCase):
	def setUp(self):
		self.leitura_cases = 1

		self.criar_camadas_cases =(((['9','1','8 7','5','2 3','4 10 11']), 6, 3),
			(([[9,-1,-1,-1,-1,-1],[1,-1,-1,-1,-1,-1],[8,7,-1,-1,-1,-1],[5,-1,-1,-1,-1,-1],[2,3,-1,-1,-1,-1],[4,10,11,-1,-1,-1]]), 10))
		
		self.main_cases = 1

	def test_leitura(self):
		n = self.leitura_cases
		(x, e) = make_testcase(n)
		self.assertEqual(leitura(f"input{n}.txt"), x)

	def test_criar_camadas(self):
		(x, e) = self.criar_camadas_cases
		self.assertEqual(criar_camadas(*x), e)
	
	def test_main(self):
		n = self.main_cases
		(x, e) = make_testcase(n)
		self.assertEqual(main(f"input{n}.txt"), e)

if __name__=='__main__':
        unittest.main()

		


