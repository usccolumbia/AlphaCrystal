# CRYSPNet

The Crystal Structure Prediction Network ([CRYSPNet](hhttps://journals.aps.org/prmaterials/abstract/10.1103/PhysRevMaterials.4.123802)) project introduces an alternative way to perform fast prediction on Crystal Structure Information (Bravais Lattice, Space Group, and Lattice Parameter) with the power of neural networks. 

## Installation

**Note:** **Python 3.6** or later is required. Since Fastai library does not support Windows, the following installation only works on a linux-based environment. We recommend using [CONDA environment](https://docs.conda.io/projects/conda/en/latest/user-guide/tasks/manage-environments.html) to create a new environment for this installation.
To install the project with pip and git, run the following commands:
```bash
    git clone https://github.com/auroralht/cryspnet.git
    cd cryspnet
    pip install -e .
```

Pre-trained models are stored in google drive. Download the file `learner.zip` from the [drive](https://drive.google.com/file/d/1rpbV2-mnNj3M16-4BKvhuo5pkeoIY96q/view?usp=sharing). After downloading the file, pls copy it to `cryspnet/cryspnet` and extract it. Five folders: `BravaisEsmMetal`, `BravaisEsmOxide`, `BravaisEsmWhole`, `LatticeParam`, and `SpaceGroup` should be in the `cryspnet/cryspnet/learner` directory after the extraction is completed.

## 🔥Update🔥 
The library has moved from fastai v1 to fastai v2; thus Bravais Lattice, Lattice Parameters and Space Group models are retrained. Please **download** the latest models from [here](https://drive.google.com/file/d/1rpbV2-mnNj3M16-4BKvhuo5pkeoIY96q/view?usp=sharing). The link to the [old](https://drive.google.com/file/d/1s9OkrBRTSWTvufSia-ee625zR73bgBDA/view?usp=sharing) version.

To update the library itself:
```bash
    cd cryspnet
    git pull
    pip install -r requirements.txt
```

## ⚠️About fastai⚠️
*If you are not interested in training your model, then you can skip this part*

*This section would be removed after they fixed this issue in the next release version*

The current fastai v2 tabular modulus has data leakage issues when trying to export the learner. The fix is only made in the development repository. To install:
```bash
    pip uninstall fastai
    git clone https://github.com/fastai/fastai
    pip install -e "fastai[dev]"
```

## Dependancy

[fastai](https://github.com/fastai/fastai), [pytorch](https://github.com/pytorch/pytorch), and [Matminer](https://hackingmaterials.lbl.gov/matminer/installation.html) are three major package used heavily in this project. Please go to their GitHub/documentation site for more information if these packages cannot be installed.

(optional) We recommend using [JupyterLab](https://github.com/jupyterlab/jupyterlab/tree/acf208ed6f6843d03f34666ffc0cb2c37bdf2f3e) to execute our Notebook example. Running with Jupyter Notebook is extremely fine also. To install:

### conda install
```bash
    conda install -c conda-forge jupyterlab
```

### pip install
```bash
    pip install jupyterlab
```

(⚠️ISSUE⚠️) When running through the notebook, a tqdm issue might raise, saying IProcess is not found. It could be solved by installing the [Jupyter Widgets](https://ipywidgets.readthedocs.io/en/stable/user_install.html) 

### conda install
```bash
    conda install -c conda-forge ipywidgets
```

### pip install
```bash
    pip install ipywidgets
```



