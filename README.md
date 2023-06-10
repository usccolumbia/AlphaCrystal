# AlphaCrystal
AlphaCrytal: Contact map based deep learning algorithm for crystal structure prediction

```
Hu, J., Zhao, Y., Song, Y., Dong, R., Yang, W., Li, Y. and Siriwardane, E., 2021. Alphacrystal: Contact map based crystal structure prediction using deep learning. arXiv preprint arXiv:2102.01620.
```

### Installation:

1) Install [MLatticeABC](https://github.com/usccolumbia/MLatticeABC), a software for predicting lattice parameters a/b/c from a given formula

2) Install [Cryspnet](https://github.com/AuroraLHT/cryspnet), a software to predict the crystal system and space groups from a given formula

3) Download the AlphaCrystal model file last-model-12-0-125-32.h5 from [Figshare](https://figshare.com/articles/software/Deep_learning_model_file_for_AlphaCrystal_For_structure_prediction_of_crystal_materials_with_12_atoms/23488214) and put it into the models folder.

4) Install other needed packages
```
tensorflow                      2.4.1
pymatgen                        2023.5.31 
nevergrad                       0.6.0         
ninja                           1.10.2.3      
numba                           0.53.0        
numpy                           1.24.3
```
### How to run
given a formula Ag2F4, 

(1) use 
```
python MLatticeABC/predict.py -i Ag2F4
```
to predict the a,b,c of lattice unit cell.

(2) use 

put Ag2F4 into formula.csv file.
```
python cryspnet/predict.py -i formula.csv
```
To get top 1-5 space groups and alpha/beta/gamma parameters.

(3) put all the info into a csv input.csv file

formula,crystal,a,b,c,alpha,beta,gamma,Top-1 SpaceGroup,Top-2 SpaceGroup,Top-3 SpaceGroup,Top-4 SpaceGroup,Top-5 SpaceGroup,
Ag2F4,monoclinic,4.062,4.667,6.129,90.0,96.94,90.0,14,11,13,7,4

(4) predict the contact map for the formula
```
python contactmap.py --input-file input.csv
```
it will generate the contact map file in test/test_output/Ag2F4-*.**.input

(5) Reconstruct the crystal structure from contact map file
```
cd cmcrystal
python CMC.py --input ../test/test_output/Ag2F4-orthorhombic-62.input

### Acknowledgement

This software is developed based on three open source software including [MLatticeABC](https://github.com/usccolumbia/MLatticeABC), [CMCrystal](https://github.com/usccolumbia/cmcrystal), [cryspnet](https://github.com/AuroraLHT/cryspnet). We strongly appreciate their open-source contribution. We include their folders and some codes for illustrations and easy use by materials researchers.


