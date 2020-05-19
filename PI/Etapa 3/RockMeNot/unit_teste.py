import unittest
from RockMeNot import possivel, count, solve, matriz


def read_file(x):        
        f = open(x, "r")
        a = f.readlines()
        f.close()

        return a

def make_testcase(n):
        x = read_file(f"teste{n}.txt")
        e = int(''.join(read_file(f"res{n}.txt")))
        return (x, e)
                      
class Testrock(unittest.TestCase):

        def setUp(self):
                self.solve_cases = [1, 2]
                self.possivel_cases = [
                        (((['.','.','.'],['.','.','.'],['.','.','.']),1,1,2,2), True),
                        (((['.','.'],['#','#']),0,0,1,1), False)]
                
                self.count_cases = [
                        (((['.','.','.'],['.','.','.'],['.','.','.']),3,3),5),
                        (((['.','.'],['.','#']),2,2),1)]
                
                self.matriz_cases = [
                        (['3 3\n', '...\n', '...\n', '...']),([['.', '.', '.'], ['.', '.', '.'], ['.', '.', '.']], 3, 3)
                        ]
                
        def test_solve(self):
                for n in self.solve_cases:
                        (x, e) = make_testcase(n)
                        self.assertEqual(solve(x), e)

        def test_possivel(self):
                for (x, e) in self.possivel_cases:
                        self.assertEqual(possivel(*x), e)

        def test_count(self):
                for (x, e) in self.count_cases:
                        self.assertEqual(count(*x), e)

        def test_matriz(self):
                #for (x, e) in self.matriz_cases:
                        #self.assertEqual(matriz(*x), e)
                self.assertEqual(matriz(['3 3\n', '...\n', '...\n', '...']),([['.', '.', '.'], ['.', '.', '.'], ['.', '.', '.']], 3, 3))

if __name__=='__main__':
        unittest.main()





