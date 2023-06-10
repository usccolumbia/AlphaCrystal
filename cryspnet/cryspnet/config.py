from pathlib import Path

N_ESMBLER = 5

TOPN_BRAVAIS = 2

TOPN_SPACEGROUP = 3

BATCHSIZE = 256

BRAVAIS_SPLIT_NAME = "Bravais"

LEARNER = f"{Path(__file__).parents[0]}/learner/"

BRAVAIS_MODELS_FOLDER = {
    "metal" : "BravaisEsmMetal",
    "oxide" : "BravaisEsmOxide",
    "whole" : "BravaisEsmWhole",
}

BRAVAIS_ENSEMBLER_PREFIX = "ensembler"

LATTICE_PARAM_NAMES = ['a', 'b', 'c', 'alpha', 'beta','gamma']

LATTICE_PARAM_MODELS_FOLDER = "LatticeParam"

LATTICE_PARAM_MODELS = {
    'cubic (F)': 'cubic (F).pkl',
    'cubic (I)': 'cubic (I).pkl',
    'cubic (P)': 'cubic (P).pkl',
    'hexagonal (P)': 'hexagonal (P).pkl',
    'monoclinic (C)': 'monoclinic (C).pkl',
    'monoclinic (P)': 'monoclinic (P).pkl',
    'orthorhombic (C)': 'orthorhombic (C).pkl',
    'orthorhombic (F)': 'orthorhombic (F).pkl',
    'orthorhombic (I)': 'orthorhombic (I).pkl',
    'orthorhombic (P)': 'orthorhombic (P).pkl',
    'rhombohedral (P)': 'rhombohedral (P).pkl',
    'tetragonal (I)': 'tetragonal (I).pkl',
    'tetragonal (P)': 'tetragonal (P).pkl',
    'triclinic (P)': 'triclinic (P).pkl'
}

LATTICE_NORM = "lattice_norm.pkl"

LATTICE_PARAM_ERROR = "error.pkl"

SPACE_GROUP_MODELS_FOLDER = "SpaceGroup"

SPACE_GROUP_MODELS = {
    'cubic (F)': 'cubic (F).pkl',
    'cubic (I)': 'cubic (I).pkl',
    'cubic (P)': 'cubic (P).pkl',
    'hexagonal (P)': 'hexagonal (P).pkl',
    'monoclinic (C)': 'monoclinic (C).pkl',
    'monoclinic (P)': 'monoclinic (P).pkl',
    'orthorhombic (C)': 'orthorhombic (C).pkl',
    'orthorhombic (F)': 'orthorhombic (F).pkl',
    'orthorhombic (I)': 'orthorhombic (I).pkl',
    'orthorhombic (P)': 'orthorhombic (P).pkl',
    'rhombohedral (P)': 'rhombohedral (P).pkl',
    'tetragonal (I)': 'tetragonal (I).pkl',
    'tetragonal (P)': 'tetragonal (P).pkl',
    'triclinic (P)': 'triclinic (P).pkl'
}


BRAVAIS_LATTICE = [
     'cubic (I)',
     'cubic (F)',
     'cubic (P)',
     'hexagonal (P)',
     'rhombohedral (P)',
     'tetragonal (I)',
     'tetragonal (P)',
     'orthorhombic (I)',
     'orthorhombic (F)',
     'orthorhombic (C)',
     'orthorhombic (P)',
     'monoclinic (C)',
     'monoclinic (P)',
     'triclinic (P)'
]

PRED_COLS = {
    "cubic (P)" : ['a'],
    "cubic (F)" : ['a'],
    "cubic (I)" : ['a'],
    
    "monoclinic (P)": ["a", "b", "c", "beta"],
    "monoclinic (C)": ["a", "b", "c", "beta"],

    "hexagonal (P)": ["a", "c"],
    
    "rhombohedral (P)": ["a", "alpha"],
    
    "tetragonal (P)" : ["a", "c"],
    "tetragonal (I)" : ["a", "c"],

    "orthorhombic (P)" : ["a", "b", "c"],
    "orthorhombic (C)" : ["a", "b", "c"],
    "orthorhombic (F)" : ["a", "b", "c"],
    "orthorhombic (I)" : ["a", "b", "c"],
    
    "triclinic (P)" : ["a", "b", "c", "alpha", "beta", "gamma"]
    }

ICSDINFO = [
    'formula',
    'cif_names',
    'Bravais',
    'sym_group',
    'a',
    'b',
    'c',
    'alpha',
    'beta',
    'gamma',
    'v',
    'Date',
    'Bravais_xp',
    'is_oxide',
    'is_metal',
    'is_pervoskite',
    'composition'
    ]

FEATURES = [
    'MagpieData minimum Number',
    'MagpieData maximum Number',
    'MagpieData range Number',
    'MagpieData mean Number',
    'MagpieData avg_dev Number',
    'MagpieData mode Number',
    'MagpieData minimum MendeleevNumber',
    'MagpieData maximum MendeleevNumber',
    'MagpieData range MendeleevNumber',
    'MagpieData mean MendeleevNumber',
    'MagpieData avg_dev MendeleevNumber',
    'MagpieData mode MendeleevNumber',
    'MagpieData minimum AtomicWeight',
    'MagpieData maximum AtomicWeight',
    'MagpieData range AtomicWeight',
    'MagpieData mean AtomicWeight',
    'MagpieData avg_dev AtomicWeight',
    'MagpieData mode AtomicWeight',
    'MagpieData minimum MeltingT',
    'MagpieData maximum MeltingT',
    'MagpieData range MeltingT',
    'MagpieData mean MeltingT',
    'MagpieData avg_dev MeltingT',
    'MagpieData mode MeltingT',
    'MagpieData minimum Column',
    'MagpieData maximum Column',
    'MagpieData range Column',
    'MagpieData mean Column',
    'MagpieData avg_dev Column',
    'MagpieData mode Column',
    'MagpieData minimum Row',
    'MagpieData maximum Row',
    'MagpieData range Row',
    'MagpieData mean Row',
    'MagpieData avg_dev Row',
    'MagpieData mode Row',
    'MagpieData minimum CovalentRadius',
    'MagpieData maximum CovalentRadius',
    'MagpieData range CovalentRadius',
    'MagpieData mean CovalentRadius',
    'MagpieData avg_dev CovalentRadius',
    'MagpieData mode CovalentRadius',
    'MagpieData minimum Electronegativity',
    'MagpieData maximum Electronegativity',
    'MagpieData range Electronegativity',
    'MagpieData mean Electronegativity',
    'MagpieData avg_dev Electronegativity',
    'MagpieData mode Electronegativity',
    'MagpieData minimum NsValence',
    'MagpieData maximum NsValence',
    'MagpieData range NsValence',
    'MagpieData mean NsValence',
    'MagpieData avg_dev NsValence',
    'MagpieData mode NsValence',
    'MagpieData minimum NpValence',
    'MagpieData maximum NpValence',
    'MagpieData range NpValence',
    'MagpieData mean NpValence',
    'MagpieData avg_dev NpValence',
    'MagpieData mode NpValence',
    'MagpieData minimum NdValence',
    'MagpieData maximum NdValence',
    'MagpieData range NdValence',
    'MagpieData mean NdValence',
    'MagpieData avg_dev NdValence',
    'MagpieData mode NdValence',
    'MagpieData minimum NfValence',
    'MagpieData maximum NfValence',
    'MagpieData range NfValence',
    'MagpieData mean NfValence',
    'MagpieData avg_dev NfValence',
    'MagpieData mode NfValence',
    'MagpieData minimum NValence',
    'MagpieData maximum NValence',
    'MagpieData range NValence',
    'MagpieData mean NValence',
    'MagpieData avg_dev NValence',
    'MagpieData mode NValence',
    'MagpieData minimum NsUnfilled',
    'MagpieData maximum NsUnfilled',
    'MagpieData range NsUnfilled',
    'MagpieData mean NsUnfilled',
    'MagpieData avg_dev NsUnfilled',
    'MagpieData mode NsUnfilled',
    'MagpieData minimum NpUnfilled',
    'MagpieData maximum NpUnfilled',
    'MagpieData range NpUnfilled',
    'MagpieData mean NpUnfilled',
    'MagpieData avg_dev NpUnfilled',
    'MagpieData mode NpUnfilled',
    'MagpieData minimum NdUnfilled',
    'MagpieData maximum NdUnfilled',
    'MagpieData range NdUnfilled',
    'MagpieData mean NdUnfilled',
    'MagpieData avg_dev NdUnfilled',
    'MagpieData mode NdUnfilled',
    'MagpieData minimum NfUnfilled',
    'MagpieData maximum NfUnfilled',
    'MagpieData range NfUnfilled',
    'MagpieData mean NfUnfilled',
    'MagpieData avg_dev NfUnfilled',
    'MagpieData mode NfUnfilled',
    'MagpieData minimum NUnfilled',
    'MagpieData maximum NUnfilled',
    'MagpieData range NUnfilled',
    'MagpieData mean NUnfilled',
    'MagpieData avg_dev NUnfilled',
    'MagpieData mode NUnfilled',
    'MagpieData minimum GSvolume_pa',
    'MagpieData maximum GSvolume_pa',
    'MagpieData range GSvolume_pa',
    'MagpieData mean GSvolume_pa',
    'MagpieData avg_dev GSvolume_pa',
    'MagpieData mode GSvolume_pa',
    'MagpieData minimum GSbandgap',
    'MagpieData maximum GSbandgap',
    'MagpieData range GSbandgap',
    'MagpieData mean GSbandgap',
    'MagpieData avg_dev GSbandgap',
    'MagpieData mode GSbandgap',
    'MagpieData minimum GSmagmom',
    'MagpieData maximum GSmagmom',
    'MagpieData range GSmagmom',
    'MagpieData mean GSmagmom',
    'MagpieData avg_dev GSmagmom',
    'MagpieData mode GSmagmom',
    'MagpieData minimum SpaceGroupNumber',
    'MagpieData maximum SpaceGroupNumber',
    'MagpieData range SpaceGroupNumber',
    'MagpieData mean SpaceGroupNumber',
    'MagpieData avg_dev SpaceGroupNumber',
    'MagpieData mode SpaceGroupNumber',
    'NComp',
    '0-norm',
    '2-norm',
    '3-norm',
    '5-norm',
    '7-norm',
    '10-norm',
    'frac s valence electrons',
    'frac p valence electrons',
    'frac d valence electrons',
    'frac f valence electrons',
    'compound possible',
    'max ionic char',
    'avg ionic char',
    'band center',
    'H',
    'He',
    'Li',
    'Be',
    'B',
    'C',
    'N',
    'O',
    'F',
    'Ne',
    'Na',
    'Mg',
    'Al',
    'Si',
    'P',
    'S',
    'Cl',
    'Ar',
    'K',
    'Ca',
    'Sc',
    'Ti',
    'V',
    'Cr',
    'Mn',
    'Fe',
    'Co',
    'Ni',
    'Cu',
    'Zn',
    'Ga',
    'Ge',
    'As',
    'Se',
    'Br',
    'Kr',
    'Rb',
    'Sr',
    'Y',
    'Zr',
    'Nb',
    'Mo',
    'Tc',
    'Ru',
    'Rh',
    'Pd',
    'Ag',
    'Cd',
    'In',
    'Sn',
    'Sb',
    'Te',
    'I',
    'Xe',
    'Cs',
    'Ba',
    'La',
    'Ce',
    'Pr',
    'Nd',
    'Pm',
    'Sm',
    'Eu',
    'Gd',
    'Tb',
    'Dy',
    'Ho',
    'Er',
    'Tm',
    'Yb',
    'Lu',
    'Hf',
    'Ta',
    'W',
    'Re',
    'Os',
    'Ir',
    'Pt',
    'Au',
    'Hg',
    'Tl',
    'Pb',
    'Bi',
    'Po',
    'At',
    'Rn',
    'Fr',
    'Ra',
    'Ac',
    'Th',
    'Pa',
    'U',
    'Np',
    'Pu',
    'Am',
    'Cm',
    'Bk',
    'Cf',
    'Es',
    'Fm',
    'Md',
    'No',
    'Lr'
    ]