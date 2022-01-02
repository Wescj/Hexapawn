# Hexapawn
This program finds the most optimal move by using a minimax algorithm.

hexapawn(["www","---","bbb"],3,'w',2)

  The first argument is an n-element list,  
  and each of these elements represents      
  a row of the board.  The first element    
  is the first or "top" row, the second     
  element is the next row, and so on.        
  Each of these elements is itself a         
  n-character string.  The characters in      
  the strings are either 'w' to indicate     
  a white pawn on that square, 'b' to         
  indicate a black pawn, or '-' to indicate   
  an empty square. The leftmost character     
  in one of these strings represents the    
  leftmost square in the row represented by  
  that square, and so on. 
  
  The second argument is an integer to 
  indicate the size of the board being       
  played on (or the number of pawns each     
  player begins with).  Thus, 3 here        
  indicates a 3 x 3 board.         

  The third argument will always be 'w' or 'b',
  to indicate whether your function is playing     
  the side of the white pawns or the side of       
  the black pawns.  There will never be any        
  other color of pawns. 
  
  The fourth argument is an integer to indicate
  how many moves ahead your minimax search is to      
  look ahead.  In this example, the 2 indicates  
  that the function should look at white's move and  
  black's move in reply, but no further.  Your  
  function must not look ahead any further than 
  the number of moves given as this argument.
                              
