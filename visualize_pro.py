import json
from pyvis.network import Network

def generate_pro_viz():
    # 1. Charger les données
    with open("data_resonance.json", "r", encoding="utf-8") as f:
        data = json.load(f)

    # 2. Initialiser le graphe Pyvis (Mode sombre, large)
    # bgcolor="#111111" -> Fond anthracite très pro
    # font_color="white" -> Texte lisible
    net = Network(height="800px", width="100%", bgcolor="#111111", font_color="white", select_menu=True, filter_menu=True)

    # 3. Ajouter les nœuds
    for node in data['nodes']:
        # On calcule la taille selon les citations (min 10, max 50)
        size = 10 + (node['citations_count'] / 100)
        if size > 50: size = 50
        
        # On prépare le texte au survol (Tooltip)
        hover_info = f"<b>{node['title']}</b><br>Auteur: {node['author']}<br>Malaise: {node['score']}<br>Citations: {node['citations_count']}"
        
        net.add_node(
            node['id'], 
            label=node['author'], # On affiche le nom de l'auteur sur le point
            title=hover_info, 
            color=node['color'], 
            size=size,
            borderWidth=2
        )

    # 4. Ajouter les arêtes (Citations vs Vibrations)
    for edge in data['edges']:
        if edge['type'] == "citation":
            # Lien bleu, fin, avec une flèche
            net.add_edge(edge['source'], edge['target'], color="#4a90e2", width=1, arrows="to", alpha=0.3)
        else:
            # Lien rouge/orange, plus épais, en pointillés (dash) pour la vibration
            net.add_edge(edge['source'], edge['target'], color="#ff4b2b", width=3, dashes=True, alpha=0.8, title="Vibration sémantique")

    # 5. Configuration de la physique (Style Force-Directed)
    net.force_atlas_2based() # Un algorithme très organique
    
    # Options interactives (pour pouvoir bouger les points à la main dans le navigateur)
    net.show_buttons(filter_=['physics']) 

    # 6. Génération du fichier final
    print("Génération du graphe interactif...")
    net.show("map_malaise_quantique.html", notebook=False)
    print("Terminé ! Ouvre 'map_malaise_quantique.html' dans ton navigateur.")

if __name__ == "__main__":
    generate_pro_viz()