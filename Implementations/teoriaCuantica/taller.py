from sys import stdin

# vect = [[2, 1], [-1, 2], [0, 1], [1, 0], [3, -1], [2, 0], [0, -2], [-2, 1], [1, -3], [0, -1]]
# vect2 = [[-1, -4], [2, -3], [-7, 6], [-1, 1], [-5, -3], [5, 0], [5, 8], [4, -4], [8, -7], [2, -7]]

from classicalToQuantum import *



def norma( vect ):
    acu = 0
    for x in range( len( vect )):
        acu += (module(vect[x]))**2
    return math.sqrt(acu)
        
def normalizate( vect ):
    Norma = norma( vect)
    for x in range( len( vect ) ):
        vect[ x ] = [vect[x][0]/Norma,vect[x][1]/Norma]
    return vect

def bra( vect  ):
    return adjointVector( vect )
    

def transicion( vect1 ,vect2):
    asnw = internalProduct( bra(vect1 ), vect2)
    
    return asnw 
def main():
    vect1 = normalizate( [[2, 1], [-1, 2], [0, 1], [1, 0], [3, -1], [2, 0], [0, -2], [-2, 1], [1, -3], [0, -1]] )

    vect2 =normalizate( [[-1, -4], [2, -3], [-7, 6], [-1, 1], [-5, -3], [5, 0], [5, 8], [4, -4], [8, -7], [2, -7]] )
    
    print(  transicion(  vect2   ,vect1) ) 
main()




def main():
    x0 = [ [0,0] for x in range( 10 )]
    x1 =x0[:]

    x0[0] = [1,0]; x1[1] = [1,0]
    print(  transicion( span( x0 )  ,x1) )
    
    

