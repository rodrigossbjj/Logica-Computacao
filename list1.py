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
        return 1 + number_of_connectives(a.inner)
    if isinstance(a, (Implies, And, Or)):
        return 1 + number_of_connectives(a.left) + number_of_connectives(a.right)
    

# Defina recursivamente um pseudoc ́odigo para a fun ̧c ̃ao atoms(A) que retorna o
# conjunto de todas as f ́ormulas atˆomicas que ocorrem em A. Por exemplo,
# atoms(p ∧ ¬(p → ¬q) ∨ ¬q) = {p, q}.
# Em seguida, vocˆe deve usar o reposit ́orio dispon ́ıvel em
# https://github.com/thiagoalvesifce/logicomp
# e escrever um c ́odigo para definir a fun ̧c ̃ao atoms(formula). Por exemplo,
# atoms(Or(Not(And(Atom('p'), Atom('choveu_ontem'))), Atom('p')))
# deve retornar um conjunto com as atˆomicas Atom('p') e Atom('choveu_ontem').
def atoms(a):
    if isinstance(a, Atom):
        return { a }
    elif isinstance(a, Not):
        return atoms(a.inner)
    elif isinstance(a, (Implies, And, Or)):
        return atoms(a.left) | atoms(a.right)
     

# Defina recursivamente um pseudoc ́odigo para a fun ̧c ̃ao number of atoms(A) que
# retorna o n ́umero de ocorrˆencias de atˆomicas em A. Por exemplo,
# number of atoms((p ∧ ¬(p → ¬q)) ∨ ¬q) = 4.
# Em seguida, vocˆe deve escrever uma defini ̧c ̃ao para a fun ̧c ̃ao
# number_of_atoms(formula) no contexto do reposit ́orio dispon ́ıvel em
# https://github.com/thiagoalvesifce/logicomp
def number_of_atoms(a):
    if isinstance(a,Atom):
        return 1 
    elif isinstance(a, Not):
        return number_of_atoms(a.inner)
    elif isinstance(a, (Implies, And, Or)):
        return number_of_atoms(a.left) + number_of_atoms(a.right)
    

