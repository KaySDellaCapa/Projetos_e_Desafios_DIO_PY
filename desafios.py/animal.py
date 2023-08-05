a = input() 
b = input() 
c = input() 

if a == 'vertebrado': 
  if b == 'ave' and c == 'carnivoro':
    print("aguia")
  if b == 'ave' and c == 'onivoro':
    print('pomba')
  if b == 'mamifero' and c == 'onivoro':
    print('homem')
  if b == 'mamifero' and c == 'herbivoro':
    print('vaca')
    
elif a == 'invertebrado':
  if b == 'inseto' and c == 'hematofago':
    print("pulga")
  if b == 'inseto' and c == 'herbivoro':
    print('lagarta')
  if b == 'analideo' and c == 'hematofago':
    print('sanguessuga')
  if b == 'analideo' and c == 'onivoro':
    print('minhoca')