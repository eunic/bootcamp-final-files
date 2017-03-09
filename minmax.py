list2 = []

def find_max_min(lista):
  
  min_num = min(lista)
  max_num = max(lista)
  
  if(min_num == max_num):
    
    list2=[min_num]
      
  else:
    
    list2 = [min_num,max_num]
    
  return list2