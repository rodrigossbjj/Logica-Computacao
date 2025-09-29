from formula import * 

# Defina um pseudoc ́odigo recursivo para a fun ̧c ̃ao number_of_connectives(A) que
# retorna a quantidade de conectivos da f ́ormula de entrada A. Por exemplo,
# number_of_connectives(((¬p) → (¬q))) = 3.
# Em seguida, vocˆe deve usar o c ́odigo dispon ́ıvel em
# https://github.com/thiagoalvesifce/logicomp
# e escrever um c ́odigo para a fun ̧c ̃ao number_of_connectives(formula).

def number_of_connectives(a):
    if isinstance(a,Atom):
        return 0
    if isinstance(a, Not): 
        return 1 + number_of_connectives(a.left) + number_of_connectives(a.right)
    if isinstance(a, Implies) or isinstance(a, And) or isinstance(a, Or):
        return 1 + number_of_connectives(a.left) + number_of_connectives(a.right)