import unittest
from classicalToQuantum import *


class classicalToQuantum(unittest.TestCase):
    
    def testExperimentBooleanMatrix( self  ):
        booleanMatrix = [[False, False, False, False, False, False], [True, False, False, False, False, True],
                         [True, False, False, False, False, False], [False, False, True, False, False, False],
                         [False, False, False, True, False, False], [False, False, False, False, True, False]]

        vectIni = [True, False, False, False, False, False]

        self.assertEqual(experimentBooleanMatrix( 1 ,booleanMatrix[:], vectIni[:]  ),
                         [False, True, True, False, False, False] )

        self.assertEqual(experimentBooleanMatrix( 3 ,booleanMatrix[:], vectIni[:]   ),
                         [False, False, False, False, True, False] )

        self.assertEqual(experimentBooleanMatrix( 5 ,booleanMatrix[:], vectIni[:]   ),
                         [False, True, False, False, False, False] )

    def testMultipleSlitExperiment( self ):
        matrix = [[[0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0]],
                  [[0.3333333333333333, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0]],
                  [[0.3333333333333333, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0]],
                  [[0.3333333333333333, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0]],
                  [[0, 0], [0.5, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0]],
                  [[0, 0], [0.5, 0], [0.5, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0]],
                  [[0, 0], [0, 0], [0.5, 0], [0.5, 0], [0, 0], [0, 0], [0, 0], [0, 0]],
                  [[0, 0], [0, 0], [0, 0], [0.5, 0], [0, 0], [0, 0], [0, 0], [0, 0]]]

        vectIni = [[1, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0]]
        self.assertEqual( probabilisticSystem( matrix[:], vectIni[:], 1 ), [[0, 0], [0.3333333333333333, 0.0],
                                                                            [0.3333333333333333, 0.0], [0.3333333333333333, 0.0],
                                                                            [0.0, 0.0], [0.0, 0.0],[0.0, 0.0], [0.0, 0.0]] )



        matrix = [[[0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0]],
                  [[0.5, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0]],
                  [[0.5, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0]],
                  [[0, 0], [0.3333333333333333, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0]],
                  [[0, 0], [0.3333333333333333, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0]],
                  [[0, 0], [0.3333333333333333, 0], [0.3333333333333333, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0]],
                  [[0, 0], [0, 0], [0.3333333333333333, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0]],
                  [[0, 0], [0, 0], [0.3333333333333333, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0]]]
        
        vectIni = [[1, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0]]
        self.assertEqual( probabilisticSystem(  matrix[:], vectIni[:], 2 ),  [[0.0, 0.0], [0.0, 0.0], [0.0, 0.0], [0.16666666666666666, 0.0],
                                                    [0.16666666666666666, 0.0], [0.3333333333333333, 0.0],
                                                    [0.16666666666666666, 0.0], [0.16666666666666666, 0.0]] )
        
    def testMultipleSlitQuantumExperiment( self ):
        pass

    def testGraphProbabilitiesVector( self ):
         graphProbabilitiesVector( [ [0,0] ,[0,0]  ,[0,0] ,
                                     [1/6,0],[1/6,0], [1/3,0],
                                     [1/6,0],[1/6,0] ]  )
        
        
if __name__ == '__main__':
    unittest.main()


#Author : Iván Camilo Rincón Saavedra