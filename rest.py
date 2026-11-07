def fibunnacci(n):
    a, b = 0, 1
    #mise à jour du programme fibunnacci
    fic = [a]
    while (b<n):
        a, b = b, a + b
        fic.append(a)
    return fic
    
fibunnacci(1000)








# =================================================================================
classeur = {
  "positive":[],
  "negatives":[]
  
}
#================================================================================

#ici la fonction trier vas permettre de voir
def trier(classeur,nombre):
  # tier un nombre positive et négative
  # vasvoir si un nombre est positive le classe la value positive(liste) dans le dictionnaire classeur 
  if nombre >0:
    classeur['positive'].append(nombre)
  else : 
    classeur['negatives'].append(nombre)
  return classeur




