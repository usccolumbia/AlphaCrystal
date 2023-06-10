import os
import sys
import argparse
from pymatgen.io.cif import CifParser
import re
import numpy as np

parser = argparse.ArgumentParser(
        description=(
            "generate input file"
            "Generate the input file from the cif file"
        )
    )

parser.add_argument(
    "--cif",
    type=str,
    default="2-14-mp-236.cif",
    metavar="PATH",
    help="Path to cif file to generate input file",
)

args = parser.parse_args(sys.argv[1:])




def adj(structure):
    d2 = structure.distance_matrix
    for i, s1 in enumerate(structure.sites):
        for j, s2 in enumerate(structure.sites):
            if i == j:
                d2[i, j] = 0
            else:
                e1 = s1.as_dict()['species'][0]['element']
                e2 = s2.as_dict()['species'][0]['element']
                z='      '
                z1=z[:6-len(e2)]+e2
                z2=z[:6-len(e1)]+e1
                if e1 + z1 in yuzhi:
                    max_len = float(yuzhi[yuzhi.rindex(e1 + z1) + len(e1 + z1) + 15:yuzhi.rindex(
                        e1 + z1) + len(e1 + z1) + 22])
                    min_len = float(yuzhi[yuzhi.rindex(e1 + z1) + len(e1 + z1) + 4:yuzhi.rindex(
                        e1 + z1) + len(e1 + z1) + 11])
                elif e2 + z2 in yuzhi:
                    max_len = float(yuzhi[
                                    yuzhi.rindex(e2 + z2) + len(e2 + z2) + 15:yuzhi.rindex(
                                        e2 + z2) + len(e2 + z2) + 22])
                    min_len = float(yuzhi[
                                    yuzhi.rindex(e2 + z2) + len(e2 + z2) + 4:yuzhi.rindex(
                                        e2 + z2) + len(e2 + z2) + 11])
                else:
                    max_len = 0.00000
                    min_len = 0.00000
                if min_len <= d2[i, j] <= max_len:
                    d2[i, j] = 1
                else:
                    d2[i, j] = 0
    d2 = d2.astype(int)
    return d2

with open('style.ini', "r") as fileobj:
    yuzhi = fileobj.read()

with open(args.cif, "r") as fileobj:
    text = fileobj.read()
    str1 = (text[text.rindex('_chemical_formula_sum') + len('_chemical_formula_sum') + 3:text.rindex(
        '_cell_volume')].replace('\n', '')).replace("'", '')
    str2 = str1.split(' ')
    fom = ''.join(str2)
    sg = re.findall('\d+', text[text.rindex('_symmetry_Int_Tables_number'):text.rindex(
        '_chemical_formula_structural')])
    la = re.findall(r'\d+\.\d+', text[text.rindex('_cell_length_a'):text.rindex('es_number')])
    parser = CifParser(args.cif)
    structure = parser.get_structures()[0]
    d2=adj(structure)


np.set_printoptions(threshold=np.inf)
fp = open(args.cif.replace('cif','input'), "w")
fp.truncate()
with open(args.cif.replace('cif','input'), "w") as fw:
    fw.write('formula:' + fom + '\n')
    fw.write('spacegroup:' + sg[0] + '\n')
    fw.write('lattice-abc:' + la[0] + ',' + la[1] + ',' + la[2] + '\n')
    fw.write('lattice_angles:' + la[3] + ',' + la[4] + ',' + la[5] + '\n')
    fw.write('contactmap:' + '(' + str(len(d2)) + ',' + str(len(d2)) + ')' + '\n')
    d2 = str(d2).replace(' [', '')
    d2 = d2.replace('[', '')
    d2 = d2.replace(']', '')
    fw.write(d2)

