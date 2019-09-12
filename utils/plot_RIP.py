#!/usr/local/bin/python3
"""
Plot RIP counts for each position of multiple sequence alignments (.aln)
Author: Wang Haoming@Xulab
"""
import numpy as np
import pandas as pd
from Bio import AlignIO
from collections import Counter
import re,argparse
import matplotlib.pyplot as plt
from matplotlib.backends.backend_pdf import PdfPages
import matplotlib.patches as patches
def get_unaligned_pos(ref):
    a = re.finditer(' ', ref)
    for i in a:
        yield i.start()

# def plot_stub(index, count):
#     x = np.zeros(2 * count).reshape(2,count)
#     x[:] = index  # assign all x = idex
#     y_start = np.arange(0.2, count, 1)
#     y_end = np.arange(0.8, count, 1)
#     y = np.vstack((y_start, y_end))
#     plt.plot(x, y)

def main():
    # add commandline arguments
    parser = argparse.ArgumentParser(description="Used for plot RIP (repeat-induced point mutation) via multiple sequence alignments.")
    parser.add_argument("-i", '--input', dest="filename", required=True, help='Input .aln file')
    # parser.add_argument("-x", '--type', dest="rip_type", choices=["g2a", "c2t", "all"], default="all", help='Choose to plot g2a, c2t or all RIP')
    parser.add_argument("-c", '--color', dest="col", default="#006925", help="You can choose colors: red, blue or RGB colors")
    parser.add_argument("-o", '--output', dest="output", default="rip_res", help="Output prefix")
    args = parser.parse_args()

    ## read multiple alignment results
    align = AlignIO.read(args.filename, format="clustal")
    # align = AlignIO.read("2HPH-1.aln", format="clustal")

    ## get columns' annotation info
    for i in align.column_annotations.values():
        anno = i

    # transform align obj to array
    align_array = np.array([list(rec) for rec in align], dtype=np.str, order="F")
    pos = get_unaligned_pos(anno)

    g2a_record = [0] * np.shape(align_array)[1]
    c2t_record = [0] * np.shape(align_array)[1]

    for i in pos:
        target_col = align_array[:, i]
        if target_col[0] == "G":
            count_dict = Counter(target_col[1:])
            cc = count_dict["A"]
            g2a_record[i] = g2a_record[i] + cc
        elif target_col[0] == "C":
            count_dict = Counter(target_col[1:])
            cc = count_dict["T"]
            c2t_record[i] = c2t_record[i] + cc

    # make array columns: pos, G->A count, C->T count, total count
    ar = np.array([[i for i in range(1, len(g2a_record)+1)],
                   g2a_record, c2t_record, np.array(g2a_record) + np.array(c2t_record)]).T
    df = pd.DataFrame(ar)
    df.index = range(1, len(df) + 1)
    df.columns = ["pos", "G->A", "C->T", "total"]   # rename columns
    df.to_csv("{0}.csv".format(args.output), index=False)

    row_num = align_array.shape[0] - 1
    rr = row_num / 100
    # output three types of result
    ll = [("total", ar[:, 3]/rr), ("g2a", ar[:, 1]/rr), ("c2t", ar[:, 2]/rr)]
    for item in ll:
        ty = item[0]
        rip_count = item[1]
        pdf = PdfPages('{0}_{1}.pdf'.format(args.output, ty))  # initialize a pdf
        x_start, x_end, y_start, y_end = [], [], [], []
        for idx, i in enumerate(rip_count):
            x_start.append(idx)
            x_end.append(idx)
            y_start.append(0)
            y_end.append(i)
        ## main plot
        """
        整个figure左下角为（0，0）右上角为（1，1），plt.axes(x, y, width, height) 添加一个子图并规定其在页面的相对位置；
        plt.subplot(nrow, ncol, 当前子图定位) 定位较模糊
        """
        # ax1 = plt.subplot(211)
        ax1 = plt.axes([0.1, 0.2, 0.8, 0.7])
        ax1.plot([x_start, x_end], [y_start, y_end], color=args.col)
        plt.suptitle("G->A & C->T") if ty=="total" else plt.suptitle("G->A") if ty=="g2a" else plt.suptitle("C->T")
        plt.ylim(bottom=0)
        plt.xlim(left=0)

        ## record ax1's xlim for ax2
        a,b = plt.xlim()
        plt.ylabel("% of mutations")

        ## repeat structure
        # ax2 = plt.subplot(212)
        # struc_len = 3562
        ax2 = plt.axes([0.1, 0.05, 0.8, 0.1], xlim=(a, b), ylim=(0, 1))

        # patches.Rectangle((x,y), width, height)
        ax2.add_patch(patches.Rectangle((428, 0.7), 1025, 0.25, color="#FF9F1C",ec="black"))
        ax2.add_patch(patches.Rectangle((2455, 0.7), 1025, 0.25, color="#FF9F1C",ec="black"))
        # ax2.add_patch(patches.Rectangle((428+1025, 0.7), 1002, 0.25, color="white",ec="black"))
        ax2.arrow(428 + 300, 0.825, 400, 0, head_width=0.1, head_length=100, fc="white")
        ax2.arrow(3180, 0.825, -400, 0, head_width=0.1, head_length=100, fc="white")
        ## plot linker structure
        ax2.plot([0, 426], [0.825, 0.825], color="black")
        ax2.plot([3482, b], [0.825, 0.825], color="black")
        ax2.plot([428+1035, 428+2012], [0.825, 0.825], color="blue", linewidth=3)
        plt.axis('off')
        # plt.show()
        #
        # import time
        # time.sleep(999)
        pdf.savefig()
        plt.close()
        pdf.close()

if __name__ == '__main__':
    main()
