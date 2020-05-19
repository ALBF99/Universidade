import unittest
import sys
from gdp import mediana
from gdp import output
from gdp import soma
from gdp import subsequencia
from gdp import ciclo

class TestGdp(unittest.TestCase):

    def test_mediana(self):
        resultado = mediana([1,2,3,4,5])
        self.assertEqual(resultado,3)
        
        resultado = mediana([6,7])
        self.assertEqual(resultado,7)
        
        resultado = mediana([8,9,10,11])
        self.assertEqual(resultado,10)
    
    def test_soma(self):
        resultado = soma([1,2,3,4,5],[1,2])
        self.assertEqual(resultado,1)

        resultado = soma([1,2],[1,2,3,4,5])
        self.assertEqual(resultado,0)        

    def test_subsequencia(self):
        resultado = subsequencia([1,2,3,4,5],[1,2])
        self.assertEqual(resultado,[1,1,2,2,3,4,5])
  
        resultado = subsequencia([1,2],[1,2,3,4,5])
        self.assertEqual(resultado,[1,2,3,4,5])

    def test_ciclo(self):
        ret = ciclo("input1.txt")
        self.assertEqual(ret,[[0,0,-5],[1,1,0],[2,4,2],[2,5,2]])

        

 
if __name__=='__main__':
        unittest.main()
   

