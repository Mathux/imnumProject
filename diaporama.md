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



#### Différents masques

|																   |																       |																  |
| -------------------------------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------- |
| <p align="center"><image src="https://perso.crans.org/bricout/Intronum/Masks/bateau_in_triangle.png" controls style="width:80%" ></image></p>| <p align="center"><image src="https://perso.crans.org/bricout/Intronum/Masks/bateau_in_square.png" controls style="width:80%" ></image></p> | <p align="center"><image src="https://perso.crans.org/bricout/Intronum/Masks/bateau_in_circle.png" controls style="width:80%" ></image></p>|
| <p align="center"><image src="https://perso.crans.org/bricout/Intronum/Masks/bateau_out_triangle_noise_0.000.png" controls style="width:80%" ></image></p>| <p align="center"><image src="https://perso.crans.org/bricout/Intronum/Masks/bateau_out_square_noise_0.000.png" controls style="width:80%" ></image></p> | <p align="center"><image src="https://perso.crans.org/bricout/Intronum/Masks/bateau_out_circle_noise_0.000.png" controls style="width:80%" ></image></p>|



#### Différents masques

|																   |																       |																  |
| -------------------------------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------- |
| <p align="center"><image src="https://perso.crans.org/bricout/Intronum/Masks/montagne_in_triangle.png" controls style="width:80%" ></image></p>| <p align="center"><image src="https://perso.crans.org/bricout/Intronum/Masks/montagne_in_square.png" controls style="width:80%" ></image></p> | <p align="center"><image src="https://perso.crans.org/bricout/Intronum/Masks/montagne_in_circle.png" controls style="width:80%" ></image></p>|
| <p align="center"><image src="https://perso.crans.org/bricout/Intronum/Masks/montagne_out_triangle_noise_0.000.png" controls style="width:80%" ></image></p>| <p align="center"><image src="https://perso.crans.org/bricout/Intronum/Masks/montagne_out_square_noise_0.000.png" controls style="width:80%" ></image></p> | <p align="center"><image src="https://perso.crans.org/bricout/Intronum/Masks/montagne_out_circle_noise_0.000.png" controls style="width:80%" ></image></p>|


### Zero-padding
Artefacts dus au 0-padding

0 pixels												       | 3 pixels													| 6 pixels													 |
-------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------- |
<image src="https://perso.crans.org/bricout/Intronum/Padding/0_input.png" controls style="width:100%" ></image>| <image src="https://perso.crans.org/bricout/Intronum/Padding/3_input.png" controls style="width:100%" ></image>| <image src="https://perso.crans.org/bricout/Intronum/Padding/6_input.png" controls style="width:100%" ></image>|
<image src="https://perso.crans.org/bricout/Intronum/Padding/0_out.png" controls style="width:100%" ></image>  | <image src="https://perso.crans.org/bricout/Intronum/Padding/3_out.png" controls style="width:100%" ></image>  | <image src="https://perso.crans.org/bricout/Intronum/Padding/6_out.png" controls style="width:100%" ></image>  |


### Images non naturelles

|																   |																       |																  |																      |
| -------------------------------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------- |
| <p align="center"><image src="https://perso.crans.org/bricout/Intronum/CoL/input_1.png" controls style="width:100%" ></image></p>| <p align="center"><image src="https://perso.crans.org/bricout/Intronum/CoL/input_2.png" controls style="width:100%" ></image></p> | <p align="center"><image src="https://perso.crans.org/bricout/Intronum/CoL/input_3.png" controls style="width:100%" ></image></p>| <p align="center"><image src="https://perso.crans.org/bricout/Intronum/CoL/input_4.png" controls style="width:100%" ></image></p> |
| <p align="center"><image src="https://perso.crans.org/bricout/Intronum/CoL/out_1.png" controls style="width:100%" ></image></p>  | <p align="center"><image src="https://perso.crans.org/bricout/Intronum/CoL/out_2.png" controls style="width:100%" ></image></p>   | <p align="center"><image src="https://perso.crans.org/bricout/Intronum/CoL/out_3.png" controls style="width:100%" ></image></p>  | <p align="center"><image src="https://perso.crans.org/bricout/Intronum/CoL/out_4.png" controls style="width:100%" ></image></p>   |


### Images non naturelles

|																   |																       |																  |
| -------------------------------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------- |
| <p align="center"><image src="https://perso.crans.org/bricout/Intronum/Gogh/input_1.png" controls style="width:90%" ></image></p>| <p align="center"><image src="https://perso.crans.org/bricout/Intronum/Gogh/input_2.png" controls style="width:90%" ></image></p> | <p align="center"><image src="https://perso.crans.org/bricout/Intronum/Gogh/input_3.png" controls style="width:90%" ></image></p>|
| <p align="center"><image src="https://perso.crans.org/bricout/Intronum/Gogh/out_1.png" controls style="width:90%" ></image></p>  | <p align="center"><image src="https://perso.crans.org/bricout/Intronum/Gogh/out_2.png" controls style="width:90%" ></image></p>   | <p align="center"><image src="https://perso.crans.org/bricout/Intronum/Gogh/out_3.png" controls style="width:90%" ></image></p>  |


#### Architecture
<image src="https://perso.crans.org/bricout/Intronum/Archi.png" controls style="width:45%" ></image>


#### Résultats : couches de convolution (1,4)

|																   |																       |																  |																      |
| -------------------------------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------- |
| <p align="center"><image src="https://perso.crans.org/bricout/Intronum/Convolution/01/bateau_in.png" controls style="width:100%" ></image></p>| <p align="center"><image src="https://perso.crans.org/bricout/Intronum/Convolution/01/bateau_out_noise_0.00.png" controls style="width:100%" ></image></p> | <p align="center"><image src="https://perso.crans.org/bricout/Intronum/Convolution/01/bateau_out_noise_0.14.png" controls style="width:100%" ></image></p>| <p align="center"><image src="https://perso.crans.org/bricout/Intronum/Convolution/01/bateau_out_noise_0.28.png" controls style="width:100%" ></image></p> |
| <p align="center"><image src="https://perso.crans.org/bricout/Intronum/Convolution/04/bateau_in.png" controls style="width:100%" ></image></p>| <p align="center"><image src="https://perso.crans.org/bricout/Intronum/Convolution/04/bateau_out_noise_0.00.png" controls style="width:100%" ></image></p> | <p align="center"><image src="https://perso.crans.org/bricout/Intronum/Convolution/04/bateau_out_noise_0.14.png" controls style="width:100%" ></image></p>| <p align="center"><image src="https://perso.crans.org/bricout/Intronum/Convolution/04/bateau_out_noise_0.28.png" controls style="width:100%" ></image></p> |


#### Résultats : couches de convolution (7,10)

|																   |																       |																  |																      |
| -------------------------------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------- |
| <p align="center"><image src="https://perso.crans.org/bricout/Intronum/Convolution/07/bateau_in.png" controls style="width:100%" ></image></p>| <p align="center"><image src="https://perso.crans.org/bricout/Intronum/Convolution/07/bateau_out_noise_0.00.png" controls style="width:100%" ></image></p> | <p align="center"><image src="https://perso.crans.org/bricout/Intronum/Convolution/07/bateau_out_noise_0.14.png" controls style="width:100%" ></image></p>| <p align="center"><image src="https://perso.crans.org/bricout/Intronum/Convolution/07/bateau_out_noise_0.28.png" controls style="width:100%" ></image></p> |
| <p align="center"><image src="https://perso.crans.org/bricout/Intronum/Convolution/10/bateau_in.png" controls style="width:100%" ></image></p>| <p align="center"><image src="https://perso.crans.org/bricout/Intronum/Convolution/10/bateau_out_noise_0.00.png" controls style="width:100%" ></image></p> | <p align="center"><image src="https://perso.crans.org/bricout/Intronum/Convolution/10/bateau_out_noise_0.14.png" controls style="width:100%" ></image></p>| <p align="center"><image src="https://perso.crans.org/bricout/Intronum/Convolution/10/bateau_out_noise_0.28.png" controls style="width:100%" ></image></p> |


#### Résultats : couches de convolution (13,16)

|																   |																       |																  |																      |
| -------------------------------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------- |
| <p align="center"><image src="https://perso.crans.org/bricout/Intronum/Convolution/13/bateau_in.png" controls style="width:100%" ></image></p>| <p align="center"><image src="https://perso.crans.org/bricout/Intronum/Convolution/13/bateau_out_noise_0.00.png" controls style="width:100%" ></image></p> | <p align="center"><image src="https://perso.crans.org/bricout/Intronum/Convolution/13/bateau_out_noise_0.14.png" controls style="width:100%" ></image></p>| <p align="center"><image src="https://perso.crans.org/bricout/Intronum/Convolution/13/bateau_out_noise_0.28.png" controls style="width:100%" ></image></p> |
| <p align="center"><image src="https://perso.crans.org/bricout/Intronum/Convolution/16/bateau_in.png" controls style="width:100%" ></image></p>| <p align="center"><image src="https://perso.crans.org/bricout/Intronum/Convolution/16/bateau_out_noise_0.00.png" controls style="width:100%" ></image></p> | <p align="center"><image src="https://perso.crans.org/bricout/Intronum/Convolution/16/bateau_out_noise_0.14.png" controls style="width:100%" ></image></p>| <p align="center"><image src="https://perso.crans.org/bricout/Intronum/Convolution/16/bateau_out_noise_0.28.png" controls style="width:100%" ></image></p> |


#### Résultats : couches de convolution (46,49)

|																   |																       |																  |																      |
| -------------------------------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------- |
| <p align="center"><image src="https://perso.crans.org/bricout/Intronum/Convolution_late/46/bateau_in.png" controls style="width:100%" ></image></p>| <p align="center"><image src="https://perso.crans.org/bricout/Intronum/Convolution_late/46/bateau_out_noise_0.00.png" controls style="width:100%" ></image></p> | <p align="center"><image src="https://perso.crans.org/bricout/Intronum/Convolution_late/46/bateau_out_noise_0.14.png" controls style="width:100%" ></image></p>| <p align="center"><image src="https://perso.crans.org/bricout/Intronum/Convolution_late/46/bateau_out_noise_0.28.png" controls style="width:100%" ></image></p> |
| <p align="center"><image src="https://perso.crans.org/bricout/Intronum/Convolution_late/49/bateau_in.png" controls style="width:100%" ></image></p>| <p align="center"><image src="https://perso.crans.org/bricout/Intronum/Convolution_late/49/bateau_out_noise_0.00.png" controls style="width:100%" ></image></p> | <p align="center"><image src="https://perso.crans.org/bricout/Intronum/Convolution_late/49/bateau_out_noise_0.14.png" controls style="width:100%" ></image></p>| <p align="center"><image src="https://perso.crans.org/bricout/Intronum/Convolution_late/49/bateau_out_noise_0.28.png" controls style="width:100%" ></image></p> |


#### Résultats : couches de convolution dilatées (19,22)

|																   |																       |																  |																      |
| -------------------------------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------- |
| <p align="center"><image src="https://perso.crans.org/bricout/Intronum/Dilated/19/bateau_in.png" controls style="width:100%" ></image></p>| <p align="center"><image src="https://perso.crans.org/bricout/Intronum/Dilated/19/bateau_out_noise_0.00.png" controls style="width:100%" ></image></p> | <p align="center"><image src="https://perso.crans.org/bricout/Intronum/Dilated/19/bateau_out_noise_0.14.png" controls style="width:100%" ></image></p>| <p align="center"><image src="https://perso.crans.org/bricout/Intronum/Dilated/19/bateau_out_noise_0.28.png" controls style="width:100%" ></image></p> |
| <p align="center"><image src="https://perso.crans.org/bricout/Intronum/Dilated/22/bateau_in.png" controls style="width:100%" ></image></p>| <p align="center"><image src="https://perso.crans.org/bricout/Intronum/Dilated/22/bateau_out_noise_0.00.png" controls style="width:100%" ></image></p> | <p align="center"><image src="https://perso.crans.org/bricout/Intronum/Dilated/22/bateau_out_noise_0.14.png" controls style="width:100%" ></image></p>| <p align="center"><image src="https://perso.crans.org/bricout/Intronum/Dilated/22/bateau_out_noise_0.28.png" controls style="width:100%" ></image></p> |


#### Résultats : couche de convolution dilatée (25,28)

|																   |																       |																  |																      |
| -------------------------------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------- |
| <p align="center"><image src="https://perso.crans.org/bricout/Intronum/Dilated/25/bateau_in.png" controls style="width:100%" ></image></p>| <p align="center"><image src="https://perso.crans.org/bricout/Intronum/Dilated/25/bateau_out_noise_0.00.png" controls style="width:100%" ></image></p> | <p align="center"><image src="https://perso.crans.org/bricout/Intronum/Dilated/25/bateau_out_noise_0.14.png" controls style="width:100%" ></image></p>| <p align="center"><image src="https://perso.crans.org/bricout/Intronum/Dilated/25/bateau_out_noise_0.28.png" controls style="width:100%" ></image></p> |
| <p align="center"><image src="https://perso.crans.org/bricout/Intronum/Dilated/28/bateau_in.png" controls style="width:100%" ></image></p>| <p align="center"><image src="https://perso.crans.org/bricout/Intronum/Dilated/28/bateau_out_noise_0.00.png" controls style="width:100%" ></image></p> | <p align="center"><image src="https://perso.crans.org/bricout/Intronum/Dilated/28/bateau_out_noise_0.14.png" controls style="width:100%" ></image></p>| <p align="center"><image src="https://perso.crans.org/bricout/Intronum/Dilated/28/bateau_out_noise_0.28.png" controls style="width:100%" ></image></p> |


#### Résultats : SpatialBatchNormalization (2,11)

|																   |																       |																  |																      |
| -------------------------------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------- |
| <p align="center"><image src="https://perso.crans.org/bricout/Intronum/Batch_norm/02/bateau_in.png" controls style="width:100%" ></image></p>| <p align="center"><image src="https://perso.crans.org/bricout/Intronum/Batch_norm/02/bateau_out_noise_0.00.png" controls style="width:100%" ></image></p> | <p align="center"><image src="https://perso.crans.org/bricout/Intronum/Batch_norm/02/bateau_out_noise_0.14.png" controls style="width:100%" ></image></p>| <p align="center"><image src="https://perso.crans.org/bricout/Intronum/Batch_norm/02/bateau_out_noise_0.28.png" controls style="width:100%" ></image></p> |
| <p align="center"><image src="https://perso.crans.org/bricout/Intronum/Batch_norm/11/bateau_in.png" controls style="width:100%" ></image></p>| <p align="center"><image src="https://perso.crans.org/bricout/Intronum/Batch_norm/11/bateau_out_noise_0.00.png" controls style="width:100%" ></image></p> | <p align="center"><image src="https://perso.crans.org/bricout/Intronum/Batch_norm/11/bateau_out_noise_0.14.png" controls style="width:100%" ></image></p>| <p align="center"><image src="https://perso.crans.org/bricout/Intronum/Batch_norm/11/bateau_out_noise_0.28.png" controls style="width:100%" ></image></p> |


#### Résultats : SpatialBatchNormalization (20,29)

|																   |																       |																  |																      |
| -------------------------------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------- |
| <p align="center"><image src="https://perso.crans.org/bricout/Intronum/Batch_norm/20/bateau_in.png" controls style="width:100%" ></image></p>| <p align="center"><image src="https://perso.crans.org/bricout/Intronum/Batch_norm/20/bateau_out_noise_0.00.png" controls style="width:100%" ></image></p> | <p align="center"><image src="https://perso.crans.org/bricout/Intronum/Batch_norm/20/bateau_out_noise_0.14.png" controls style="width:100%" ></image></p>| <p align="center"><image src="https://perso.crans.org/bricout/Intronum/Batch_norm/20/bateau_out_noise_0.28.png" controls style="width:100%" ></image></p> |
| <p align="center"><image src="https://perso.crans.org/bricout/Intronum/Batch_norm/29/bateau_in.png" controls style="width:100%" ></image></p>| <p align="center"><image src="https://perso.crans.org/bricout/Intronum/Batch_norm/29/bateau_out_noise_0.00.png" controls style="width:100%" ></image></p> | <p align="center"><image src="https://perso.crans.org/bricout/Intronum/Batch_norm/29/bateau_out_noise_0.14.png" controls style="width:100%" ></image></p>| <p align="center"><image src="https://perso.crans.org/bricout/Intronum/Batch_norm/29/bateau_out_noise_0.28.png" controls style="width:100%" ></image></p> |


#### Résultats : SpatialBatchNormalization (38,47)

|																   |																       |																  |																      |
| -------------------------------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------- |
| <p align="center"><image src="https://perso.crans.org/bricout/Intronum/Batch_norm/38/bateau_in.png" controls style="width:100%" ></image></p>| <p align="center"><image src="https://perso.crans.org/bricout/Intronum/Batch_norm/38/bateau_out_noise_0.00.png" controls style="width:100%" ></image></p> | <p align="center"><image src="https://perso.crans.org/bricout/Intronum/Batch_norm/38/bateau_out_noise_0.14.png" controls style="width:100%" ></image></p>| <p align="center"><image src="https://perso.crans.org/bricout/Intronum/Batch_norm/38/bateau_out_noise_0.28.png" controls style="width:100%" ></image></p> |
| <p align="center"><image src="https://perso.crans.org/bricout/Intronum/Batch_norm/47/bateau_in.png" controls style="width:100%" ></image></p>| <p align="center"><image src="https://perso.crans.org/bricout/Intronum/Batch_norm/47/bateau_out_noise_0.00.png" controls style="width:100%" ></image></p> | <p align="center"><image src="https://perso.crans.org/bricout/Intronum/Batch_norm/47/bateau_out_noise_0.14.png" controls style="width:100%" ></image></p>| <p align="center"><image src="https://perso.crans.org/bricout/Intronum/Batch_norm/47/bateau_out_noise_0.28.png" controls style="width:100%" ></image></p> |


#### Résultats : bruit sur les couches batch

|																   |																   |																   |																       |																  |
| -------------------------------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------- |
| <p align="center"><image src="https://perso.crans.org/bricout/Intronum/Noise_batch/bateau_in_square.png" controls style="width:95%" ></image></p>| <p align="center"><image src="https://perso.crans.org/bricout/Intronum/Noise_batch/bateau_out_square_noise_0.000.png" controls style="width:95%" ></image></p> | <p align="center"><image src="https://perso.crans.org/bricout/Intronum/Noise_batch/bateau_out_square_noise_0.010.png" controls style="width:95%" ></image></p>| <p align="center"><image src="https://perso.crans.org/bricout/Intronum/Noise_batch/bateau_out_square_noise_0.100.png" controls style="width:95%" ></image></p>| <p align="center"><image src="https://perso.crans.org/bricout/Intronum/Noise_batch/bateau_out_square_noise_0.300.png" controls style="width:95%" ></image></p>|
| <p align="center"><image src="https://perso.crans.org/bricout/Intronum/Noise_batch/lac_in_square.png" controls style="width:95%" ></image></p>| <p align="center"><image src="https://perso.crans.org/bricout/Intronum/Noise_batch/lac_out_square_noise_0.000.png" controls style="width:95%" ></image></p> | <p align="center"><image src="https://perso.crans.org/bricout/Intronum/Noise_batch/lac_out_square_noise_0.010.png" controls style="width:95%" ></image></p>| <p align="center"><image src="https://perso.crans.org/bricout/Intronum/Noise_batch/lac_out_square_noise_0.100.png" controls style="width:95%" ></image></p>| <p align="center"><image src="https://perso.crans.org/bricout/Intronum/Noise_batch/lac_out_square_noise_0.300.png" controls style="width:95%" ></image></p>|


#### Résultats : bruit sur les couches convolutives

|																   |																   |																   |																       |																  |
| -------------------------------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------- |
| <p align="center"><image src="https://perso.crans.org/bricout/Intronum/Noise_conv/bateau_in_square.png" controls style="width:95%" ></image></p>| <p align="center"><image src="https://perso.crans.org/bricout/Intronum/Noise_conv/bateau_out_square_noise_0.000.png" controls style="width:95%" ></image></p> | <p align="center"><image src="https://perso.crans.org/bricout/Intronum/Noise_conv/bateau_out_square_noise_0.040.png" controls style="width:95%" ></image></p>| <p align="center"><image src="https://perso.crans.org/bricout/Intronum/Noise_conv/bateau_out_square_noise_0.100.png" controls style="width:95%" ></image></p>| <p align="center"><image src="https://perso.crans.org/bricout/Intronum/Noise_conv/bateau_out_square_noise_0.300.png" controls style="width:95%" ></image></p>|
| <p align="center"><image src="https://perso.crans.org/bricout/Intronum/Noise_conv/neige_in_square.png" controls style="width:95%" ></image></p>| <p align="center"><image src="https://perso.crans.org/bricout/Intronum/Noise_conv/neige_out_square_noise_0.000.png" controls style="width:95%" ></image></p> | <p align="center"><image src="https://perso.crans.org/bricout/Intronum/Noise_conv/neige_out_square_noise_0.040.png" controls style="width:95%" ></image></p>| <p align="center"><image src="https://perso.crans.org/bricout/Intronum/Noise_conv/neige_out_square_noise_0.100.png" controls style="width:95%" ></image></p>| <p align="center"><image src="https://perso.crans.org/bricout/Intronum/Noise_conv/neige_out_square_noise_0.300.png" controls style="width:95%" ></image></p>|


## Fin



### Visages
Pas accès à l'optimisation des visages
<image src="https://perso.crans.org/petrovich/imnum/face_model.png" controls style="width:70%" ></image>



### Visages

|																	   |																		|
| ---------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------ |
| <p align="center"><image src="https://perso.crans.org/bricout/Intronum/Visages/visage_input.png" controls style="width:40%" ></image></p>| <p align="center"><image src="https://perso.crans.org/bricout/Intronum/Visages/visage_bad_2.png" controls style="width:40%" ></image></p>  |
| <p align="center"><image src="https://perso.crans.org/bricout/Intronum/Visages/visage_bad.png" controls style="width:40%" ></image></p>  | <p align="center"><image src="https://perso.crans.org/bricout/Intronum/Visages/visage_input_2.png" controls style="width:40%" ></image></p>|



### Facilitation des tests : editeur de masks
<image src="https://perso.crans.org/bricout/Intronum/mask_editor.png" controls style="width:60%" ></image>



## Expérimentations sur le réseau



### Entraînement du réseau
<image src="https://perso.crans.org/petrovich/imnum/no_more_training.png" controls style="width:60%" ></image>



### Facilitation des tests : ajout automatique de bruit
IMAGE ou description de la méthode



## Fin