import requests
import json
import time

def fetch_300_piliers():
    all_articles = []
    headers = {'User-Agent': 'mailto:votre-email@exemple.com'}
    
    # On boucle sur 2 pages de 150 articles pour atteindre 300
    for page in [1, 2]:
        url = f"https://api.openalex.org/works?search=quantum mechanics&sort=cited_by_count:desc&page={page}&per_page=150"
        
        print(f"Extraction de la page {page} (articles les plus cités)...")
        response = requests.get(url, headers=headers)
        
        if response.status_code == 200:
            data = response.json().get('results', [])
            all_articles.extend(data)
            time.sleep(0.5) # Pause de sécurité
        else:
            print(f"Erreur API : {response.status_code}")
            break

    # Stockage brut ligne par ligne (Format JSONL)
    with open("corpus_elite.jsonl", "w", encoding="utf-8") as f:
        for record in all_articles:
            f.write(json.dumps(record) + "\n")
            
    print(f"Terminé ! {len(all_articles)} articles sérieux stockés dans 'corpus_elite.jsonl'.")

if __name__ == "__main__":
    fetch_300_piliers()