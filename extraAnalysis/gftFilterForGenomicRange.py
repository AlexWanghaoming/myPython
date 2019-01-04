# Author: Wanghaoming

import pandas as pd
import re
import collections

annot = pd.read_table("/home/wanghm/whm/1FG/fg.gtf",sep="\t",header=None,names=["chr","source","type","start","end","sd","strand","ss","attr"], low_memory=False,)
f2 = open("/home/wanghm/whm/1FG/new.gtf",'w+')
f3 = open("/home/wanghm/whm/1FG/sdsd.gtf",'w+')
annot2 = annot[annot['type'] != "transcript"]
with open("/home/wanghm/whm/1FG/fg.gtf", 'r') as f:
    geneTran = collections.defaultdict(list)
    longestTranscriptList = []
    for i in f:
        cols2 = re.split("\"|\t",i.strip())
        if cols2[2] == "transcript":
            gene = cols2[9].split(":")[1]
            geneTran[gene].append(i)
    def getLength(x):
        length = int(re.split("\"|\t",x)[4]) - int(re.split("\"|\t",x)[3])
        return length
    for gene in geneTran:
        tranList = geneTran[gene]
        lenList=list(map(getLength, tranList))
        longTranIndex = lenList.index(max(lenList))
        longestTranscript = geneTran[gene][longTranIndex]
        f2.write(longestTranscript)
        transcriptID = longestTranscript.split("\"")[3]
        print(transcriptID)

        annot3 = annot2.loc[annot2["attr"].str.match('.*{}";'.format(transcriptID))==True]
        pd.concat([annot2,annot3,annot3]).drop_duplicates(keep=False)

        annot3.to_csv(f3,sep="\t",header=None, index=None)
        annot3.to_csv(f2,sep="\t",header=None, index=None)
f2.close()
f3.close()
"""
writed to file but in 9th col, format is not right, so I use 'sed' to modify it 
    sed 's/""/"/g;s/\t"/\t/;s/;"/;/' new.gtf > lupingNofusionFixORF_onlylongestTran.gtf

"""
