import json
import hashlib
import re
import math
import pandas as pd

# =================================================================
# 1. LE LEXIQUE DE HAUTE PRÉCISION (REGEX)
# =================================================================
LEXIQUE = {
    "CAUSALITE": r"(causal|determin|local|realis|mechanis|intuitiv|visualiz|trajectory|ontology)",
    "RUPTURE": r"(non-local|bell|aspect|entangle|superpos|indetermin|random|collapse|jump|uncertainty)",
    "MALAISE": r"(paradox|myster|crisi|interpret|problem|inintel|incomplet|discomfort|puzzl|obscur|anomaly)",
    "SUCCES": r"(accura|predict|success|agree|precis|experimen|result|perform|utility)",
    "INTELLIGIBILITE": r"(understand|grasp|comprehen|insight|intelligib|explanation|picture|meaning)"
}

# =================================================================
# 2. LE MOTEUR DE SCORING (ZONE-SENSITIVE & COLLISION)
# =================================================================
def calculate_extreme_finesse(title, abstract):
    if not title: title = ""
    if not abstract: abstract = ""
    
    title = title.lower()
    abstract = abstract.lower()
    total_score = 0
    
    # --- ZONE A : LE TITRE (Multiplicateur d'Intention) ---
    for cat, pattern in LEXIQUE.items():
        if re.search(pattern, title):
            total_score += 10.0 

    # --- ZONE B : LE RÉSUMÉ (Analyse par phrase) ---
    sentences = abstract.split('.')
    for sentence in sentences:
        has_c = bool(re.search(LEXIQUE["CAUSALITE"], sentence))
        has_r = bool(re.search(LEXIQUE["RUPTURE"], sentence))
        has_m = bool(re.search(LEXIQUE["MALAISE"], sentence))
        has_s = bool(re.search(LEXIQUE["SUCCES"], sentence))
        has_i = bool(re.search(LEXIQUE["INTELLIGIBILITE"], sentence))

        # Logique de collision (Tensions épistémologiques)
        if has_s and has_i: total_score += 4.0   # Succès vs Compréhension
        if has_r and has_i: total_score += 3.5   # Rupture vs Compréhension
        if has_c and has_r: total_score += 3.0   # Choc Causalité vs Quantique
        if has_m and has_i: total_score += 3.0   # Aveu de malaise intelligible
        if has_s and has_m: total_score += 2.0   # Efficacité aveugle
        
        # Poids de base
        if has_i: total_score += 1.0
        if has_m: total_score += 0.5

    return total_score

def get_color(name):
    """Génère une couleur hexadécimale unique par auteur."""
    return "#" + hashlib.md5(name.encode()).hexdigest()[:6]

# =================================================================
# 3. EXPORT POUR GEPHI (CSV FORMAT)
# =================================================================
def export_for_gephi(nodes, edges):
    # Export des Nœuds (gephi_nodes.csv)
    nodes_df = pd.DataFrame(nodes)
    # Gephi exige "Id" et "Label"
    nodes_gephi = nodes_df.rename(columns={'id': 'Id', 'title': 'Label'})
    nodes_gephi.to_csv("gephi_nodes.csv", index=False)

    # Export des Arêtes (gephi_edges.csv)
    edges_df = pd.DataFrame(edges)
    # Gephi exige "Source" et "Target"
    edges_gephi = edges_df.rename(columns={'source': 'Source', 'target': 'Target'})
    edges_gephi.to_csv("gephi_edges.csv", index=False)
    
    print("\n--- EXPORT GEPHI RÉUSSI ---")
    print("Fichiers générés : gephi_nodes.csv, gephi_edges.csv")

# =================================================================
# 4. TRAITEMENT PRINCIPAL
# =================================================================
def parse_and_score():
    nodes = []
    print("--- Lancement du Parser Multiplexe (Citations + Vibrations) ---")

    try:
        with open("corpus_elite.jsonl", "r", encoding="utf-8") as f:
            for line in f:
                art = json.loads(line)
                
                title = art.get('title', '')
                abstract = art.get('full_abstract', '')
                score = calculate_extreme_finesse(title, abstract)
                
                author = "Unknown"
                if art.get('authorships'):
                    author = art['authorships'][0]['author']['display_name']
                
                nodes.append({
                    "id": art['id'],
                    "title": title,
                    "author": author,
                    "color": get_color(author),
                    "score": round(score, 2),
                    "citations_count": art.get('cited_by_count', 0),
                    "referenced_works": art.get('referenced_works', [])
                })
    except FileNotFoundError:
        print("Erreur : Fichier 'corpus_elite.jsonl' manquant.")
        return

    edges = []
    seuil_resonance = 0.1
    
    for i in range(len(nodes)):
        for j in range(len(nodes)):
            if i == j: continue
            
            node_a = nodes[i]
            node_b = nodes[j]
            
            # --- COUCHE 1 : CITATION (Généalogie) ---
            if node_b['id'] in node_a['referenced_works']:
                edges.append({
                    "source": node_a['id'],
                    "target": node_b['id'],
                    "type": "citation",
                    "weight": 1.0
                })

            # --- COUCHE 2 : VIBRATION (Résonance) ---
            if i < j:
                s1, s2 = node_a['score'], node_b['score']
                if s1 > 1.0 and s2 > 1.0: 
                    diff = abs(s1 - s2)
                    if diff < seuil_resonance:
                        edges.append({
                            "source": node_a['id'],
                            "target": node_b['id'],
                            "type": "vibration",
                            "weight": round(2.0 - diff, 3) # Poids plus fort pour la vibration
                        })

    # Nettoyage et Export Final
    temp_nodes = [dict(n) for n in nodes]
    for n in temp_nodes: del n['referenced_works']
    
    # On génère le JSON (pour Neo4j/D3) et les CSV (pour Gephi)
    output = {"nodes": temp_nodes, "edges": edges}
    with open("data_resonance.json", "w", encoding="utf-8") as f:
        json.dump(output, f, indent=4)
        
    export_for_gephi(temp_nodes, edges)
    
    print(f"\n--- ANALYSE TERMINÉE ---")
    print(f"Articles traités : {len(nodes)}")
    print(f"Liens de CITATION : {len([e for e in edges if e['type'] == 'citation'])}")
    print(f"Liens de VIBRATION : {len([e for e in edges if e['type'] == 'vibration'])}")

if __name__ == "__main__":
    parse_and_score()

    