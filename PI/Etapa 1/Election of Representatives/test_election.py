import unittest
import StringIO
import sys
from election import mais_votos
from election import menos_votos
from election import algoritmo
from election import empate_votos
from election import empate_cotacao
from election import output
from election import ciclo

class ElectionTests(unittest.TestCase):

	def test_mais_votos(self):
		n_partidos = 4
		rslt_mais_votos = mais_votos(n_partidos)
		self.assertEqual(0, rslt_mais_votos)

	def test_menos_votos(self):
		n_partidos = 4
		rslt_menos_votos = menos_votos(n_partidos)
		self.assertEqual(3, rslt_menos_votos)

	#def test_algoritmo(self):
		#idx = 0
		#rslt_algoritmo = algoritmo(idx)
		#self.assertEqual(20, rslt_algoritmo)

	def test_empate_votos(self):
		n_partidos = 4
		rslt_menos_votos = menos_votos(n_partidos)
		rslt_empate_votos = empate_votos(n_partidos, rslt_menos_votos)
		self.assertEqual(-1, rslt_empate_votos)

	def test_empate_cotacao(self):
		n_partidos = 4
		quociente_idx = 0
		rslt_empate_cotacao = empate_cotacao(n_partidos, quociente_idx)
		self.assertEqual(-1, rslt_empate_cotacao)

	def test_output(self):
		capturedOutput = StringIO.StringIO()
		sys.stdout = capturedOutput
		output()
		sys.stdout = sys.__stdout__
		print(capturedOutput.getvalue())

	def test_ciclo(self):
		n_partidos = 4
		rslt_ciclo = ciclo(n_partidos)
		self.assertEqual(0, rslt_ciclo)
