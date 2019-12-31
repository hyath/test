import re
#re.match(r"^!MAISON!$, !MAISON!)
N=str(input("Donner un numero de telephone: "))

print(re.match(r"^(\+212|00212|0)(5|6|7){1}(([/-_\\])?[0-9]){8}$",N))
