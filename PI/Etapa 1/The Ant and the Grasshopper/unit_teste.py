import unittest
from TheAntandtheGrasshopper import testes

class Testant(unittest.TestCase):
        
        def test_testes(self):
                self.assertEqual(testes('teste1.txt'),True)
                self.assertEqual(testes('teste2.txt'),True)


if __name__=='__main__':
        unittest.main()
