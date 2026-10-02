#  uživatel zadá znak a program rozhodne, jestli je to písmeno

pismeno = input()
pismeno_kod = ord(pismeno)

if pismeno_kod >= ord("A") and pismeno_kod <= ord("Z"):
    print("tvůj znak je velké písmeno")

elif pismeno_kod  >= ord("a") and pismeno_kod <= ord("z"):
    print("tvůj znak je malé písmeno")
