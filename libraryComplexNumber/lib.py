import math

def suma(  complexNumber1, complexNumber2 ):
	answ = ( complexNumber1[ 0 ] + complexNumber2[ 0 ],
			 complexNumber1[ 1 ] + complexNumber2[ 1 ]) 		 
	return answ


def sub( complexNumber1, complexNumber2 ):
	answ = ( complexNumber1[ 0 ] - complexNumber2[ 0 ],
			 complexNumber1[ 1 ] - complexNumber2[ 1 ] )
	
	return answ

def multComplexNumber(  complexNumber1, complexNumber2 ):
	answ = ( complexNumber1[ 0 ] * complexNumber2[ 0 ] - complexNumber1[ 1 ] * complexNumber2[ 1 ],
			  complexNumber1[ 1 ] * complexNumber2[ 0 ] + complexNumber1[ 0 ] * complexNumber2[ 1 ])
	
	return answ

def divComplexNumber(   complexNumber1, complexNumber2 ):
	div = complexNumber2[0]**2 + complexNumber2[1]**2
	
	try :
		answ =( ( complexNumber1[ 0 ] * complexNumber2[ 0 ] + complexNumber1[ 1 ] * complexNumber2[ 1 ] )/div,
			   ( complexNumber1[ 0 ] * complexNumber2[ 0 ] - complexNumber1[ 1 ] * complexNumber2[ 1 ] ) /div )

		return answ
		
	except ZeroDivisionError as error :
		print('Se produjo el siguiente error',error)
	
def conjugated( complexNumber ):
	answ = ( complexNumber[ 0 ], 
			 -complexNumber[ 1 ] )

	return answ

def module( complexNumber ):
	answ = math.sqrt( complexNumber[ 0 ]**2 + complexNumber[ 1 ] **2 )
	
	return answ

def cartesianToPolar( complexnumber ):
	angle = math.degrees( ( math.atan( complexNumber[ 1 ] / complexNumber[ 0 ] ) ) )
	answ = ( module( complexNumber) ,
			angle )
	
	return answ      
