from dataclasses import dataclass


@dataclass
class Object:
    #Quali informazioni mi servono
    object_id : int
    title : str

    def __str__(self):
        return f"{self.object_id} {self.title}"

    #Serve per poter usare l'oggetto come nodo del grafo
    def __hash__(self):
        return hash(self.object_id)