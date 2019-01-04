import pandas as pd
import re
annot = pd.read_table("/home/wanghm/whm/1FG/fg.gtf",sep="\t",header=None,names=["chr","source","type","start","end","sd","strand","ss","attr"], low_memory=False,)
annot2 = annot[annot['type'] != "transcript"]
print(annot2[annot2['attr'].str.match('.*transcript:FGRRES_17079.1";')==True])
# print(annot2[("transcript:FGRRES_17079.1" in annot2['attr']) == True])

