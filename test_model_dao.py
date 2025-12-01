from database.DAO import DAO
from model.model import Model

risultato = DAO.read_objects()
print(len(risultato)) #ci sono 85 581 dati
print(risultato[5])

model = Model()
print(model._object_dict[1234])


model.buildGrafo()
print(model._grafo)