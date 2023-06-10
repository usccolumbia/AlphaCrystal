import os
import json
import pickle
import pandas as pd
import numpy as np
import tensorflow as tf
from tensorflow.keras.layers import *
from tensorflow.keras.regularizers import l1,l2
from pymatgen.core.composition import Composition
os.environ["CUDA_VISIBLE_DEVICES"]='0'
import argparse

def output(targets, model, props, n=12, outdir='test_formulas'):
    for row in targets:
        formula = row[0]
        print(formula)
        c = Composition(formula)
        d = c.as_dict()
        symbols = []
        for k in d:
            symbols += [k]*int(d[k])
        inputs = np.array([elem_prop[e] for e in symbols])
        hw = len(inputs)
        padding = np.zeros((n-inputs.shape[0], inputs.shape[1]))
        inputs = np.concatenate((inputs,padding),axis=0).reshape((1,12,11))
        probs = model.predict(inputs)
        preds = (probs>0.5).astype(float)[0].astype(int)#.reshape((12,12)).astype(int)

        zeros = np.zeros((n,n)).astype(int)
        cnt = 0
        for i in range(1,n):
            for j in range(i):
                zeros[i][j] = preds[cnt]
                zeros[j][i] = preds[cnt]
                cnt += 1

        preds = zeros[:hw, :hw]
        matrix = []
        for hh in preds:
            hh = hh.astype(str)
            matrix.append(' '.join(hh))
        matrix = '\n'.join(matrix)

        a,b,c = row[2:5]
        alpha,beta,gama = row[5:8]
        sps = row[8:13]
        cry_stru = row[1]

        for sp in sps:
            res = ''
            res += 'formula:'+str(formula)+'\n'
            res += 'spacegroup:'+str(sp)+'\n'
            res += 'lattice-abc:'+str(a)+','+str(b)+','+str(c)+'\n'
            res += 'lattice_angles:'+','.join([str(alpha),str(beta),str(gama)])+'\n'
            res += 'contactmap:'+'(%d,%d)'%(hw,hw)+'\n'
            res += matrix+'\n'
            f = open(f'{outdir}/%s-%s-%-d.input'%(formula,cry_stru,sp), 'w')
            f.write(res)
            f.close()




if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Process input files for output generation.')
    parser.add_argument('--model', default='models/last-model-12-0-125-32.h5',
                        help='Path to the model file')
    parser.add_argument('--element-prop', default='element-prop.json',
                        help='Path to the element properties file')
    parser.add_argument('--input-file', default='test/test_formula.csv',
                        help='Path to the input CSV file')
    parser.add_argument('--out_dir', default='test/test_output',
                        help='Path to output contact map files')
    args = parser.parse_args()

    model_path = args.model
    elem_prop_path = args.element_prop
    input_file_path = args.input_file

    model = tf.keras.models.load_model(model_path)
    with open(elem_prop_path, 'r') as f:
        elem_prop = json.load(f)

    df = pd.read_csv(input_file_path, index_col=0)
    targets = df.values

    output(targets, model, elem_prop,12, args.out_dir)
    print(f"Check output contact maps in the folder: {args.out_dir}")

'''
if __name__ == '__main__':
    model = tf.keras.models.load_model("models/last-model-12-0-125-32.h5")
    with open('element-prop.json', 'r') as f:
        elem_prop = json.load(f)
    
    df = pd.read_csv('test/test_formula.csv', index_col=0)#, index_col=0
    targets = df.values

    output(targets,model,elem_prop)
    print("check output contact maps in folder /test/test_formula") 
'''
