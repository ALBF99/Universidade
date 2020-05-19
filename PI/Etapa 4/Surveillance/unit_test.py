import unittest
from Surveillance import matrizes, recebecalcula, calcula_areaponto, calcula_save_distance, calcula_pontofinal, arrayduplo, solve

class TesteUm(unittest.TestCase):
        
        def setUp(self):

                self.matrizes_cases = [(("teste_um.txt"),([[1,0],[7,0],[5,6],[5,5],[3,3],[4,7],[0,6]], 7)),
                        (("teste_dois.txt"),([[0,0],[1,0],[1,1],[0,1]], 4))]

                self.arrayduplo_cases = [(([[1,0],[7,0],[5,6],[5,5],[3,3],[4,7],[0,6]]),
                        ([[1,0],[7,0],[5,6],[5,5],[3,3],[4,7],[0,6],[1,0],[7,0],[5,6],[5,5],[3,3],[4,7],[0,6]])),
                        (([[0,0],[1,0],[1,1],[0,1]]),
                        ([[0,0],[1,0],[1,1],[0,1],[0,0],[1,0],[1,1],[0,1]]))]

                self.calcula_areaponto_cases = [(([[1,0],[7,0],[5,6],[5,5],[3,3],[4,7],[0,6]],
                        [[1,0],[7,0],[5,6],[5,5],[3,3],[4,7],[0,6],[1,0],[7,0],[5,6],[5,5],[3,3],[4,7],[0,6]], 7),([0, 4])),
                        (([[0,0],[1,0],[1,1],[0,1]], [[0,0],[1,0],[1,1],[0,1],[0,0],[1,0],[1,1],[0,1]], 4), ([0, 1, 2, 3]))]

                self.calcula_save_distance_cases = [(([[1,0],[7,0],[5,6],[5,5],[3,3],[4,7],[0,6],[1,0],[7,0],[5,6],[5,5],[3,3],[4,7],[0,6]], [0,4]), ([0])), 
                        (([[0,0],[1,0],[1,1],[0,1],[0,0],[1,0],[1,1],[0,1]], [0,1,2,3]), ([0]))]

                self.recebecalcula_cases = [(([[0,0],[1,0],[1,1],[0,1]], 4), (1.0)), 
                        (([[1,0],[7,0],[5,6],[5,5],[3,3],[4,7],[0,6],[1,0],[7,0],[5,6],[5,5],[3,3],[4,7],[0,6]], 7), (26.0))]

                self.calcula_pontofinal_cases = [(([[1,0],[7,0],[5,6],[5,5],[3,3],[4,7],[0,6],[1,0],[7,0],[5,6],[5,5],[3,3],[4,7],[0,6]], [0,4]), ([1,0])), 
                        (([[0,0],[1,0],[1,1],[0,1],[0,0],[1,0],[1,1],[0,1]], [0,1,2,3]), ([0,0]))]

                self.solve_cases = [(("teste_um.txt"),([1,0])),
                        (("teste_dois.txt"),([0,0]))]


                       
        def test_matrizes(self):
                for (x, e) in self.matrizes_cases:
                        self.assertEqual(matrizes(x), e)

        def test_arrayduplo(self):
                for (x, e) in self.arrayduplo_cases:
                        self.assertEqual(arrayduplo(x), e)

        def test_calcula_areaponto(self):
                for (x, e) in self.calcula_areaponto_cases:
                        self.assertEqual(calcula_areaponto(*x), e)

        def test_calcula_save_distance(self):
                for (x, e) in self.calcula_save_distance_cases:
                        self.assertEqual(calcula_save_distance(*x), e)

        def test_recebecalcula(self):
                for (x, e) in self.recebecalcula_cases:
                        self.assertEqual(recebecalcula(*x), e)

        def test_calcula_pontofinal(self):
                for (x, e) in self.calcula_pontofinal_cases:
                        self.assertEqual(calcula_pontofinal(*x), e)

        def solve(self):
                for (x, e) in self.solve_cases:
                        self.assertEqual(solve(x), e)



if __name__=="__main__":
        unittest.main()