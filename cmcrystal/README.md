# CMcrystal

Crystal structure reconstruction from contact maps.

Jianjun Hu & Wenhui Yang  
University of South Carolina & Guizhou University

```
Cite us:
@article{hu2021contact,
  title={Contact map based crystal structure prediction using global optimization},
  author={Hu, Jianjun and Yang, Wenhui and Dong, Rongzhi and Li, Yuxin and Li, Xiang and Li, Shaobo and Siriwardane, Edirisuriya MD},
  journal={CrystEngComm},
  volume={23},
  number={8},
  pages={1765--1776},
  year={2021},
  publisher={Royal Society of Chemistry}
}
```





## usage：

cd exp2 directory：target material and target material input

Predict the crystal structure:\
python CMC.py --input exp2/3-109-mp-758053.input \
or \
python CMC.py --input exp2/3-109-mp-758053.input --template random_crystal/3-109-mp-758053_template0.cif


calculation accuracy:\
python CMC_accuracy.py --cif exp2/3-109-mp-758053.cif --predicted resultcif/3-109-mp-758053_template0_predicted.cif
