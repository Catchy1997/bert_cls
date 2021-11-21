import pandas as pd
import os, json, re
import pickle as pkl
from tqdm import tqdm


if __name__ == "__main__":
    with open('/Users/linzhang/Documents/src/BERT-NER/datasets/data.json', 'r') as f:
        data = f.readlines()
    for line in tqdm(data[128+24:128+24+24]):
        line = json.loads(line)
        
        with open('datasets/financial/dev.json', 'a') as f:
            f.write(json.dumps(line, ensure_ascii=False)+'\n')