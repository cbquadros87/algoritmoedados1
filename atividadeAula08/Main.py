from Desktop import Desktop
from Notebook import Notebook

desktop = Desktop("Lenovo", "Azul", 500.99, 3)
desktop.cadastrar()
desktop.getInformacoes()
print(desktop)

note = Notebook("MacBookAir", "Cinza", 15.99, 1)
print(note)
note.cadastrar()