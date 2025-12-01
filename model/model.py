from database.DAO import DAO
import networkx as nx

class Model:
    def __init__(self):
        self._objects_list = []
        self._getObjects()
        # mi posso creare anche un dizionario di Object
        self._object_dict = {}
        for o in self._objects_list:
            self._object_dict[o.object_id] = o
        #grafo semplice non diretto ma pesato
        self._grafo = nx.Graph()

    def _getObjects(self):
        self._objects_list = DAO.read_objects()

    def buildGrafo(self):
        #nodi
        self._grafo.add_nodes_from(self._objects_list)
        #archi
        #------ MODO 1 (80k x 80k query SQL, dove 80k sono i nodi
        #for u in self._objects_list:
        #     for v in self._objects_list:
        #        DAO.readEdges(u,v) # questa operazione viene + lenta

        #----- MODO 2 (usare una query sola per estrarre le connessioni)
        connessioni = DAO.readConnessioni(self._object_dict)
        #leggo le connessioni dal DAO
        for c in connessioni:
            self._grafo.add_edge(c.o1, c.o2, peso = c.peso)

    def calcolaConnessa(self, id_nodo):
        #una componente connessa in un grafo orientato è l'insieme dei nodi raggiungibili da un nodo di partenza

        nodo_sorgente = self._object_dict[id_nodo] #prende il nodo scelto dall'utente

        #1. Usando i successori
        successori = nx.dfs_successors(self._grafo, nodo_sorgente)
        print(f"Successori: {len(successori)}")

        #2. Usando i predecessori
        predecessori = nx.dfs_predecessors(self._grafo, nodo_sorgente)
        print(f"Prededessori: {len(predecessori)}")

        #3. Ottenendo l'albero di visita
        albero = nx.dfs_tree(self._grafo, nodo_sorgente)
        print(f"Albero: {albero}")
        return len(albero.nodes)


