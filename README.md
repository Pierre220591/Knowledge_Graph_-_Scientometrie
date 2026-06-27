### 3. Ton Rapport Personnel (`rapport.md`)
Ce document est ton espace d'étude privé. Il est conçu pour t'aider à réviser la théorie des graphes, la scientométrie, et à préparer tes futurs entretiens ou présentations.

```markdown
# Journal d'Étude Personnel : Topographie du Malaise Quantique

Ce rapport documente les concepts scientifiques, mathématiques et informatiques assimilés durant la conception de ce pipeline d'épistémologie computationnelle.

---

## I. Cahier de Révision : Théorie des Graphes & Réseaux

### 1. Le Concept de Graphe Multiplexe (Multiplex Network)
Dans l'analyse de données classique, un réseau est simple (une seule relation lie deux entités). Ce projet met en œuvre un modèle de **graphe multiplexe (ou multicouche)** : les nœuds restent les mêmes (les articles de physique), mais les arêtes (les liens) appartiennent à des dimensions parallèles.

* **La dimension sociologique (Orientation : Directed) :** Représentée par les citations. C'est un flux fléché, asymétrique ($A \rightarrow B$ ne signifie pas $B \rightarrow A$). Elle cartographie l'arbre généalogique officiel de la science.
* **La dimension cognitive (Orientation : Undirected) :** Représentée par la résonance du malaise. C'est un lien symétrique ($A \leftrightarrow B$), non fléché, basé sur la proximité métrique de deux scores. Elle cartographie une affinité élective inconsciente.

### 2. Physique des Graphes : L'algorithme ForceAtlas2
La forme "stellaire" de notre réseau n'est pas un dessin aléatoire, c'est le résultat d'une simulation de forces physiques équilibrées à l'aide de deux lois fondamentales :

* **Force de Répulsion (Modèle Électrostatique de Coulomb) :** Deux nœuds se repoussent systématiquement. Plus ils sont proches, plus la force de rejet est forte. Cela évite les superpositions illisibles et aère le graphe.
* **Force d'Attraction (Modèle Élastique / Loi de Hooke) :** Les liens agissent comme des ressorts. Plus le poids (`weight`) attribué par notre parser est élevé, plus le ressort est rigide et contracte la distance entre les nœuds.

**Leçon analytique :** Si le "Soleil Rouge" s'est formé de manière aussi compacte, c'est parce que la force d'attraction sémantique (nos scores de vibration ultra-proches) a écrasé la force de répulsion de l'algorithme. La topologie valide l'hypothèse.

---

## II. Cahier de Révision : Scientométrie & Traitement du Langage (NLP)

### 1. La Scientométrie Sémantique
La scientométrie quantitative traditionnelle compte le nombre de publications ou l'indice h-index d'un auteur. Ce projet pratique une **scientométrie cognitive**. On ne cherche pas à savoir *combien* l’élite publie, mais *comment la structure de son langage trahit une friction épistémologique*.

### 2. Ingénierie des Caractéristiques (Feature Engineering) du Parser
Pour transformer de la philosophie kantienne en données mathématiques exploitables, le code applique trois règles strictes de NLP :

* **La Segmentation de Contexte (Sentence Split) :** Scanner un résumé entier crée du bruit (l'auteur peut parler de succès au début et de paradoxe à la fin, sans lien entre les deux). En coupant le texte par des points (`.`), on force l'algorithme à chercher des **collisions** au sein d'une seule unité de pensée (la phrase).
* **La Capture Morphologique (Regex) :** L'usage de patterns comme `causal*` ou `mechanis*` permet de s'affranchir des variations grammaticales (adjectifs, verbes, pluriels) pour capturer l'essence du concept.
* **La Hiérarchie Informationnelle (Title Weighting) :** Le titre est traité comme une métadonnée à forte densité d'intention. Un concept qui y apparaît reçoit un bonus massif de $+10.0$, isolant les manifestes épistémologiques de la littérature de routine.

---

## III. Interprétation Phénoménologique du "Soleil Rouge"

Face à un examinateur, ce graphique est l'arme absolue pour prouver que l'intuition de départ n'était pas un biais cognitif personnel :

1. **Si le malaise était superficiel :** Le cluster rouge n'existerait pas. Les points exprimant du malaise seraient dispersés aléatoirement au gré des réseaux de citations (liens bleus).
2. **La structure observée :** On constate l'existence d'un noyau rouge hyper-dense, largement déconnecté de l'arborescence des citations. **Conclusion :** Des physiciens qui n'appartiennent pas aux mêmes écoles de pensée, qui ne se citent pas et ne collaborent pas, finissent par converger vers la même signature textuelle de l'inconfort. Le besoin de causalité (Kant) agit comme une structure rigide de l'esprit humain : quand la réalité physique la refuse, l'appareil linguistique des chercheurs s'ajuste partout sur la même fréquence de détresse.

---

## IV. Notes techniques pour l'avenir (Pistes de scaling)
Si je devais pousser ce projet à un niveau d'ingénierie supérieur :
1. **Remplacer le Lexique Fixe par des LLM Embeddings :** Utiliser des vecteurs de similarité cosinus pour détecter le malaise sous-jacent, même si l'auteur n'utilise aucun des mots exacts de notre lexique.
2. **Ajouter la Centralité de Proximité (Closeness Centrality) :** Calculer mathématiquement quel article est le plus proche de tous les autres dans la dimension du malaise pour identifier l'épicentre historique de la crise de l'entendement.