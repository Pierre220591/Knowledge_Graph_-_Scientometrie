import json
import networkx as nx
import matplotlib.pyplot as plt

def generer_visu():
    # 1. Charger les données que tu viens de parser
    with open("data_resonance.json", "r", encoding="utf-8") as f:
        data = json.load(f)

    # 2. Créer le graphe
    G = nx.Graph()

    # Ajouter les articles (nœuds) avec leur couleur d'auteur
    node_colors = []
    for node in data['nodes']:
        G.add_node(node['id'], title=node['title'])
        node_colors.append(node['color'])

    # Ajouter les liens de résonance (arêtes)
    for edge in data['edges']:
        G.add_edge(edge['source'], edge['target'])

    print(f"Préparation du graphe : {G.number_of_nodes()} nœuds et {G.number_of_edges()} liens.")

    # 3. Calculer la disposition des points (Force-directed layout)
    # Les articles connectés vont se rapprocher, les autres s'écarter
    pos = nx.spring_layout(G, k=0.15, iterations=50)

    # 4. Dessiner
    plt.figure(figsize=(12, 10))
    nx.draw_networkx_nodes(G, pos, node_size=50, node_color=node_colors, alpha=0.8)
    nx.draw_networkx_edges(G, pos, width=0.5, alpha=0.3)

    plt.title("Visualisation de la Résonance du Malaise (Couleurs par Auteur)")
    plt.axis('off')
    print("Affichage du graphe... Fermez la fenêtre pour arrêter.")
    plt.show()

if __name__ == "__main__":
    generer_visu()
    
    