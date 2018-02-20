# Felipe Pazos
# 2/19/2018

class Fraction: 
     def __init__(self, a, b):
          g = self.gcd( a, b )
          self.frac = (a//g, b//g)
     
     def gcd( self, a, b ):
          if a == 0:
               return b
          if b == 0:
               return a
          
          r = a%b
          return self.gcd( b, r )

     def __str__( self ):
          return str( self.frac[0] ) + "/" + str( self.frac[1] )
     
     def __add__( self, b ):

          newA = self.frac[0] * b.frac[1] + self.frac[1]*b.frac[0]
          newB = self.frac[1] * b.frac[1]

          g = self.gcd( newA, newB )
          
          return Fraction( newA // g, newB //g )
     def __sub__( self, b ):
          c = Fraction( b.frac[0]* -1 , b.frac[1] )
          return self + c    
     
     def __mul__( self, b ):
          newA = self.frac[0]*b.frac[0]
          newB = self.frac[1]*b.frac[1]

          g = self.gcd( newA, newB )
          return Fraction( newA // g, newB // g ) 
x = Fraction( 6, 8 )
y = Fraction( 2, 3 )

print( x + y )
print( x - y )
print( x * y )
print( x )
