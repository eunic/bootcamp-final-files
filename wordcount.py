def words(stringofwords):
  

  dict_of_words = {}
  
  list_of_words = stringofwords.split()
  
  for word in list_of_words:
    
    if word  in dict_of_words:
      
      if word.isdigit():
        
        dict_of_words[int(word)] += 1
        
      else:
        
        dict_of_words[word] += 1

    else:
      
      if word.isdigit():
        
        dict_of_words[int(word)] = 1
        
      else:
        
        dict_of_words[word] = 1
        
        
  return dict_of_words