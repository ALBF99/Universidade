#Teste para The Modern Feud of the Capulets and Montagues

import unittest
from main import main1 
class TesteUm(unittest.TestCase):
	
	def selfUp(self):
		pass

	def testeum(self):
	
		n1,n2,n3 = main1("input1.txt")
		self.assertEqual(n1, 2)
		self.assertEqual(n2, 2)
		self.assertEqual(n3, 0)

	def testedois(self):
	
		n1,n2,n3 = main1("input2.txt")
		self.assertEqual(n1, 5)
		self.assertEqual(n2, 2)
		self.assertEqual(n3, 1)

if __name__=="__main__":
	unittest.main()
