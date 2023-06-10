import argparse
import sys
from pymatgen.core import Composition
from pymatgen.io.cif import CifParser
import re
import numpy as np
import nevergrad as ng
from pyxtal import pyxtal
from pyxtal.lattice import Lattice

parser = argparse.ArgumentParser(
        description=(
            "Crystal Structure prediction by contact map"
        )
    )

# data inputs
parser.add_argument(
    "--input",
    type=str,
    default="2-14-mp-2715.input",
    metavar="PATH",
    help="cmcrystal.input file",
)

parser.add_argument(
    "--template",
    default="",
    type=str,
    metavar="TEMPLATE",
    help="template cif file",
)
#Nevergrad
parser.add_argument(
    "--budget",
    default=10000,
    type=int,
    metavar="INT",
    help="budget of Nevergrad",
)

parser.add_argument(
    "--random",
    default=50,
    type=int,
    metavar="INT",
    help="number of random structures",
)
args = parser.parse_args(sys.argv[1:])

with open('style.ini', "r") as fileobj:
    yuzhi = fileobj.read()

#input:  cif text string
#input:  flatted xyz coordinates of all sites [x1,y1,z1,x2,y2,z2,...]
def replace_sitexyz(text,coordinates):
    coordinates = coordinates.tolist()
    #print('coordinates',coordinates)
    for i in range(len(coordinates)):
        coordinates[i]=str(coordinates[i])
    text1=text[text.rindex('_atom_site_occupancy')+len('_atom_site_occupancy')+3:]
    # print(text1)

    text1=text1.split('  ')
    text1=np.array(text1).reshape(int(len(text1)/7),7)
    h=0
    for i in range(len(text1)):
        if float(text1[i][3]) not in spe:
            text1[i][3] = coordinates[h]
            h+=1
        if float(text1[i][4]) not in spe:
            text1[i][4] = coordinates[h]
            h+=1
        if float(text1[i][5]) not in spe:
            text1[i][5] = coordinates[h]
            h+=1
    if h!=le[w]:
        print('error')
    text1=text1.flatten()
    text1='  '.join(text1)
    text=text.replace(text[text.rindex('_atom_site_occupancy')+len('_atom_site_occupancy')+3:],text1)
    # print(text)
    return text

def convert_to_pymatgenCif(template_file,pym_file):
    with open(template_file, 'r+') as f:
        text = f.read()
        text=text.replace(text[:text.rindex('_symmetry_space_group_')],'')
        text = text.replace('#END', '')
        with open(pym_file, 'r') as fo:
            pym = fo.read()
        pym=pym.replace(pym[pym.rindex('_symmetry_space_group'):pym.rindex('_cell_length_a')],text[text.rindex('_symmetry_space_group'):text.rindex('_symmetry_Int_Tables')])
        pym = pym.replace(pym[pym.rindex('_symmetry_Int_Tables'):pym.rindex('_chemical_formula_structural')],
                          text[text.rindex('_symmetry_Int_Tables'):text.rindex('_symmetry_cell_setting')])
        pym = pym.replace(pym[pym.find('loop_'):pym.rindex('loop_')],
                          text[text.find('loop_'):text.rindex('loop_')])

        text1 = text[text.rindex('_atom_site_occupancy') + len('_atom_site_occupancy') + 1:]
        text1 = text1.split()
        text1 = np.array(text1).reshape(int(len(text1) / 7), 7)
        for i in range(len(text1)):
            text1[i][-1] = text1[i][-1] + '\n'
            text1[i][1]=text1[i][1]+str(i)
        text1 = text1.flatten()
        text1 = '  '.join(text1)
        text1 = '  ' + text1
        pym = pym.replace(pym[pym.rindex('_atom_site_occupancy') + len('_atom_site_occupancy') + 1:], text1)
        f.seek(0)
        f.write(pym)
        f.truncate()


def cm_fitness(p):
    fitness=1111
    for z in p:
        if z in spe:
            fitness=9993
            break
    if fitness==1111:
        with open(files[w], "r") as fileobj:
            text = fileobj.read()
            text = replace_sitexyz(text, p)
            try:
                parser = CifParser.from_string(text)
                structure = parser.get_structures()[0]
                d2 = structure.distance_matrix
            except ValueError:
                fitness=9990
            else:
                if d2.shape != ad[w].shape:
                    fitness = 9999
                else:
                    d2 = adj(structure)
                    comparison = np.multiply(d2, ad[w])
                    n = np.count_nonzero(comparison)
                    n1 = np.count_nonzero(d2)
                    n2 = np.count_nonzero(ad[w])

                    try:
                        fitness = (-2) * n / (n1 + n2)
                    except ZeroDivisionError:
                        fitness = 9995
    return fitness


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


with open(args.input,'r') as fil:
    inp=fil.read()
    formula=inp[inp.rindex('formula:')+len('formula:'):inp.rindex('spacegroup')].replace('\n','')
    spacegroup=int(re.findall('\d+',inp[inp.rindex('spacegroup'):inp.rindex('contactmap')])[0])
    lattice = re.findall(r'\d+\.\d+', inp[inp.rindex('lattice-abc'):inp.rindex('contactmap')])
    dim=re.findall('\d+',inp[inp.rindex('('):inp.rindex(')')])
    contactmap=re.findall('\d+',inp[inp.rindex(')'):])
    for i in range(len(contactmap)):
        contactmap[i]=int(contactmap[i])
    contactmap=np.array(contactmap).reshape(int(dim[0]),int(dim[0]))



comp=Composition(formula)
elements=list(comp.as_dict().keys())
mols= list(comp.as_dict().values())
mols=[int(x) for x in mols]


lat=[]
for k in lattice:
    lat.append(float(k))
latt = Lattice.from_para(lat[0], lat[1], lat[2], lat[3], lat[4], lat[5])

np.set_printoptions(threshold=np.inf)
fn=args.input.replace('.input','').replace('exp2/','')

if args.template!='':
    print('templ_file', args.template)
    try:
        parser = CifParser(args.template)
        structure = parser.get_structures()[0]
        d2 = adj(structure)
    except ValueError:
        fitness = 9990
    else:
        if d2.shape != contactmap.shape:
            fitness = 9999
        else:
            comparison = np.multiply(d2, contactmap)
            n = np.count_nonzero(comparison)
            n1 = np.count_nonzero(d2)
            n2 = np.count_nonzero(contactmap)

            try:
                fitness = 2 * n / (n1 + n2)
            except ZeroDivisionError:
                fitness = 9995
    print('contact map accuracy before', fitness)
    files=[args.template]
else:
    cmfit = []
    mps = []
    sh = []
    for k in range(args.random):
        C = pyxtal()
        C.from_random(3, spacegroup, elements, mols, lattice=latt)
        template_file = f"random_crystal/{fn}_template{k}.cif"
        random_crystal = f"random_crystal/{fn}_random{k}.cif"
        C.to_file(template_file)
        C.to_file(random_crystal)
        C = C.to_pymatgen()
        C.to(filename='random_crystal/pym_file.cif')
        convert_to_pymatgenCif(template_file, 'random_crystal/pym_file.cif')
        with open(template_file, 'r') as fl:
            tex = fl.read()
            tex = tex[tex.rindex('_atom_site_occupancy') + len('_atom_site_occupancy') + 3:]
            tex = tex.split('  ')
            tex = np.array(tex).reshape(int(len(tex) / 7), 7)
            sh.append(len(tex))
            el = []
            mp = []
            for s in range(len(tex)):
                el.append(tex[s][0])
                mp.append(float(tex[s][2]))
            wpel = []
            for e in elements:
                wpel.append(el.count(e))
            mpt = []
            for h in wpel:
                mpt.append(mp[:h])
                mp = mp[h:]
            mps.append(mpt)
            parser = CifParser(template_file)
            structure = parser.get_structures()[0]
            d1 = contactmap
            d2 = adj(structure)
            # print(d2)
            if d1.shape != d2.shape:
                fitness = -9991
            else:
                n = np.sum(d2 * d1 == 1)
                n1 = np.sum(d1 == 1)
                n2 = np.sum(d2 == 1)

                try:
                    fitness = 2 * n / (n1 + n2)
                except ZeroDivisionError:
                    fitness = -9999
            cmfit.append(fitness)

    ind = []
    for z in range(len(mps)):
        tag = True
        for k in mps[z]:
            if k != sorted(k, reverse=True):
                tag = False
                break
        if tag == True:
            ind.append(z)


    sps = []
    cmfitne = []
    for a in ind:
        sps.append(sh[a])
        cmfitne.append(cmfit[a])

    index = []
    cmfitne2 = []
    for k in range(len(sps)):
        if sps[k] == min(sps):
            index.append(ind[k])
            cmfitne2.append(cmfitne[k])

    temindex = []
    for k in range(len(cmfitne2)):
        if cmfitne2[k] == max(cmfitne2):
            temindex.append(index[k])
    index = temindex
    print("finished generating and screening Random Crystal Structure")
    template_file = f"random_crystal/{fn}_template{index[0]}.cif"
    print('templ_file',template_file)
    print('contact map accuracy before', cmfit[index[0]])
    files = [template_file]

with open('spec/spec.txt','r') as fo:
    spe=fo.read()
    spe=re.findall(r'\d+.\d+', spe)
    spe = [float(x) for x in spe]

ad=[]
le = []
co1 = []
co2 = []
s = 0
for i, file in enumerate(files):
    s = i
    ad.append(contactmap)
    with open(file, "r") as fileobj:
        text = fileobj.read()
        co = re.findall(r'\d+.\d+', text[text.rindex('occupancy'):])
        co1.append(co)
        cof = []
        cn=0
        for i in co:
            cof.append(float(i))
            if float(i) not in spe:
                cn+=1
        pf=cof[:]
        cof = np.array(cof).reshape(int(len(cof) / 3), 3)
        co2.append(cof)
        le.append(cn)

best_co = []
#best_fitness = []
c_fitness=[]
w = 0
#rmses = []
#maes = []
for i, file in enumerate(files):
    w = i
    parametrization = ng.p.Instrumentation(
        p=ng.p.Array(shape=(le[i],)).set_bounds(lower=0.0, upper=1.0),
    )

    optimizer = ng.optimizers.DE(parametrization=parametrization, budget=args.budget)
    recommendation = optimizer.minimize(cm_fitness)
    best_x = recommendation.value[1]['p']
    if cm_fitness(best_x)==9993:
        c_a = cm_fitness(np.array(pf))
        c_fitness.append(c_a)
        best_co.append(pf)
        with open(files[w], "r") as fileobj:
            text = fileobj.read()
        res = fileobj.name.replace('random_crystal', 'resultcif').replace('.cif','_predicted.cif')
        fp = open(res, "w")
        fp.truncate()
        with open(res, "w") as fw:
            fw.write(text)
    else:
        c_a = cm_fitness(best_x)
        c_fitness.append(c_a)

        with open(files[w], "r") as fileobj:
            text = fileobj.read()
            text = replace_sitexyz(text, best_x)
        best_xval=re.findall(r'\d+.\d+', text[text.rindex('occupancy'):])
        best_xval=[float(e) for e in best_xval]
        best_co.append(best_xval)
        res = fileobj.name.replace('random_crystal', 'resultcif').replace('.cif','_predicted.cif')
        fp = open(res, "w")
        fp.truncate()
        with open(res, "w") as fw:
            fw.write(text)

print(files)
print('best_co',best_co)
print('contact map accuracy after',-c_fitness[0])




