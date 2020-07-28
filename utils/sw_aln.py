import numpy as np
import pandas as pd

def get_match_score(s1, s2):
    score = score_matrix[s1][s2]
    return score


def get_matrix_max(matrix, seq1, seq2):  # 得到最大分数下标
    Max = matrix.max()
    for i in range(len(seq2) + 1):
        for j in range(len(seq1) + 1):
            if matrix[i][j] == Max:
                return (i, j)


def main(seq1, seq2):

    best_matrix = np.empty(shape=(len(seq2) + 1, len(seq1) + 1), dtype=int)

    s1 = ""
    s2 = ""
    gap = -2
    for i in range(len(seq2) + 1):
        for j in range(len(seq1) + 1):
            if i == 0 or j == 0:
                best_matrix[i][j] = 0
            else:
                # print(i-1, j-1)
                match = get_match_score(seq2[i - 1], seq1[j - 1])
                gap1_score = best_matrix[i - 1][j] + gap
                gap2_score = best_matrix[i][j - 1] + gap
                match_score = best_matrix[i - 1][j - 1] + match
                score = max(gap1_score, gap2_score, match_score)
                if score > 0:
                    best_matrix[i][j] = score
                else:
                    best_matrix[i][j] = 0

    # traceback
    i, j = get_matrix_max(best_matrix, seq1, seq2)
    while (best_matrix[i][j] != 0):
        match = get_match_score(seq2[i - 1], seq1[j - 1])
        if i > 0 and j > 0 and best_matrix[i][j] == best_matrix[i - 1][j - 1] + match:
            s1 += seq1[j - 1]
            s2 += seq2[i - 1]
            i -= 1
            j -= 1
        elif i > 0 and best_matrix[i, j] == best_matrix[i - 1, j] + gap:
            s1 += '-'
            s2 += seq2[i - 1]
            i -= 1
        else:
            s1 += seq1[j - 1]
            s2 += '-'
            j -= 1
    return s1[::-1] + '\n' + s2[::-1]


if __name__ == '__main__':
    sequence1 = 'CACAATAACAACACAAAAACAACAACAAACGCATCACAATCAACAAGCACATTTTCGTCAAAAGAAACATCGCATCACACACTCTCACACAAAGGTCGACGGCTTGGCTAGAGCTAGTGGAGGTCAACAATGAATGCCTATTTTGGTTTAGTCGTCCAGGCGGTGAGCACAAAATTTGTGTCGTTTGACAAGATGGTTCATTTAGGCAACTGGTCAGATCAGCCCCACTTGTAGCAGTAGCGGCGGCGCTCGAAGTGTGACTCTTATTAGCAGACAGGAACGAGGACATTATTATCATCTGCTGCTTGGTGCACGATAACTTGGTGCGTTTGTCAAGCAAGGTAAGTGGACGACCCGGTCATACCTTCTTAAGTTCGCCCTTCCTCCCTTTATTTCAGATTCAATCTGACTTACCTGTTCTACCCAAGCATCCAAATGAAAAAGCCTGAACTCACCGCGACGTCTGTCGAGAAGTTTCTGATCGAAAAGTTCGACAGCGTCTCCGACCTGATGCAGCTCTCGGAGGGCGAAGAATCTCGTGCTTTCAGCTTCGATGTAGGAGGGCGTGGATATGTCCTGCGGGTAAATAGCTGCGCCGATGGTTTCTACAAAGATCGTTATGTTTATCGGCACTTTGCATCGGCCGCGCTTCCGATTCCGGAAGTGCTTGACATTGGGGAGTTCAGCGAGAGCCTGACCTATTGCATCTCCCGCCGTGCACAGGGTATCACGTTGCAAGACCTGCCTGAAACCGAACTGCCCGCTGTTCTCCAGCCGGTCGCGGAGGCCATGGATGCGATCGCTGCGGCCGATCTTAGCCAGACGAGCGGGTTTGGCCCATTCGGACCGC'
    sequence2 = 'GACCTGGCTGAAATCGAACTGCACGCTGTTCTCCAGCCGGTCGCGGAGGCCATGGATGCGATCGCTGCGGCCGATCTTAGCCAGACGAGCGGGTTTGGCCCATTCGGACCGCAAGGAATCGGTCAATACACTATATGGCGTGATTTCATATGCGCGATTGCTGATCCCCATGTGTATCACTGGCAAACTGTGATGGACGACACCGTCAGTGCGTCCGTCGCGCAGGCTCTCGATGAGCTGATGCTTTGGGCCGAGGACTGCCCCGAAGTCCGGCACCTCGTGCATGCGGATTTCGGCTCCAACAATGTCCTGACGGACAATGGCCGCATAACAGCGGTCATTGACTGGAGCGAGGCGATGTTCGGGGATTCCCAATACGAGGTCGCCAACATCCTCTTCTGGAGGCCGTGGTTGGCTTGTATAGAGCAGCAGACGCGCTACTTCGAGCGGAGGCATCCGGAGCTTGCAGGATCGCCGCGCCTCCGGGCGTATATGCTCCGCATTGGTCTTGACCAACTCTATCAGAGCTTGGTTGACGGCAATTTCGATGATGCAGCTTGGGCGCAGGGTCGATGCGACGCAATCGTCCGATCCGGAGCCGGGACTGTCGGGCGTACACAAATCGCCCGCAG'


    # make a score matrix
    score_matrix = pd.DataFrame([[2, -5, -7, -7], [-5, 2, -7, -7], [-7, -7, 2, -5], [-7, -7, -5, 2]],
                                index=["A", "G", "C", "T"], columns=["A", "G", "C", "T"])

    print(score_matrix)
    print(main(sequence4, sequence5))


