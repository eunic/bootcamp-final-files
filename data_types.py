
def data_type(n=None):

    if n != None:
  
      if type(n) == str:
        
        return len(n)
        
      elif type(n) == bool:
        
        return n
      
      elif type(n) == int:
        
        if n < 100:
          
          return "less than 100"
          
        elif n > 100:
          
          return "more than 100"
          
        else:
          
          return "equal to 100"
      
      elif type(n) == list:
        
        if len(n) >= 3:
          
          return n[2]
        
    else:
          
        return "no value"