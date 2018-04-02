'''
Creates reference file of all possible combinations for Big Papi screens 
Author: Mudra Hegde
Email: mhegde@broadinstitute.org
'''
import pandas as pd
import csv, argparse

def get_parser():
    parser = argparse.ArgumentParser()
    parser.add_argument('--ref1',
        type=str,
        help='Reference file 1')
    parser.add_argument('--ref2',
        type=str,
        help='Reference file 2')
    parser.add_argument('--outputfile',
        type=str,
        help='.csv output file')
    return parser

def get_combos(ref_df1_file,ref_df2_file,outputfile):
    ref_df1 = pd.read_csv(ref_df1_file,header=None)
    ref_df2 = pd.read_csv(ref_df2_file,header=None)
    bc_combos = []
    info_combos = []
    for i,r in ref_df1.iterrows():
        for j,s in ref_df2.iterrows():
            bc_combos.append(r[0]+':'+s[0])
            info_combos.append(r[1]+':'+s[1])
    df = pd.DataFrame({'Barcode':bc_combos,'Construct ID':info_combos})
    df.to_csv(outputfile,index=False,header=None)
    return 1

if __name__ == '__main__':
    args = get_parser().parse_args()
    val = get_combos(args.ref1,args.ref2,args.outputfile)