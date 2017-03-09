def find_missing(lista,listb):

	seta = set(lista) ^ set(listb)

	if len(lista) !=0 and  len(listb) != 0:

		if lista == listb:

			return 0
		else:

			listc = list(seta)[0]

			return listc
        
			#return [x for x in lista+listb if (x not in lista) or (x not in listb)]	
	else:

		return 0