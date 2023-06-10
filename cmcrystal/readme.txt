exp2 directory：target material and target material input


usage：

Predict the crystal structure:
python CMC.py --input exp2/3-109-mp-758053.input 
or 
python CMC.py --input exp2/3-109-mp-758053.input --template random_crystal/3-109-mp-758053_template0.cif


calculation accuracy:
python CMC_accuracy.py --cif exp2/3-109-mp-758053.cif --predicted resultcif/3-109-mp-758053_template0_predicted.cif
