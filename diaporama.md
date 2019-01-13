## Imagerie numérique
### Projet inpainting


## Rapide état de l'art


### Méthodes usuelles

 - lignes de niveaux
 - méthodes par patchs
 - context encoder


### Caractéristiques

|				| Patch-based   | Context Encoder  | Network |
| -----------------------------:| -------------:| ----------------:| -------:|
| Image size   		  	| Any		| Fixed		   | Any     |
| Local Conistsency	   	| Yes		| No		   | Yes     |
| Semantics		   	| No		| Yes		   | Yes     |
| Creates objects	   	| No		| Yes		   | Yes     |


### Structure du réseau
<image src="https://perso.crans.org/bricout/Intronum/network_overview.png" controls style="width:90%"></image>


## Tests sur le réseau


### Différentes formes de masks
Images


### Zero-padding
Artefacts dus au 0-padding
<image src="https://perso.crans.org/bricout/Intronum/padding_no_cap.png" controls style="width:80%" ></image>


### Visages
Images


### Visages
Pas accès à l'optimisation des visages
<image src="https://perso.crans.org/petrovich/imnum/face_model.png" controls style="width:80%" ></image>


### Images non naturelles
Style pastel
<image src="https://perso.crans.org/bricout/Intronum/Col_no_cap.png" controls style="width:90%" ></image>


### Images non naturelles
Style très particulier (impressionnisme)
<image src="https://perso.crans.org/bricout/Intronum/gogh.png" controls style="width:70%" ></image>


## Expérimentations sur le réseau


### Entraînement du réseau
<image src="https://perso.crans.org/petrovich/imnum/no_more_training.png" controls style="width:60%" ></image>


### Bidouilles du réseau
Images