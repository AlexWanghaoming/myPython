# __author__ = "wanghaoming"
# __date__ = "2018-9-10"
#
# from Bio import Entrez
# Entrez.email = '568019240@qq.com'
# def read_id(file_name):
#     id_array = []
#     fh = open(file_name,'r')
#     for line in fh.readlines():
#         id = line.strip()
#         id_array.append(id)
#     fh.close()
#
#     id_array = ','.join(id_array)
#     return id_array
# def download_seq(id_array):
#     result_handle = Entrez.efetch(db="nucleotide",rettype="fasta", id=id_array)
#     result = result_handle.read()
#     return result
# def write_to_file(file_out_name,content):
#     fh = open(file_out_name, 'w')
#     fh.write(content)
#     fh.close()
#
# def main():
#     file_name = '/home/wanghm/wys/wys_geneList'
#     file_out_name = '/home/wanghm/wys/bzip_111Gene.fasta'
#     id_array = read_id(file_name)
#     result = download_seq(id_array)
#     write_to_file(file_out_name,result)
#
# if __name__ == '__main__':
#     main()


import urllib.request
from urllib.error import HTTPError
from bs4 import BeautifulSoup
import re
import time
from selenium import webdriver

file = open("/home/wanghm/wys/gene.fasta",'w')
url = "https://www.arabidopsis.org/browse/genefamily/bZIP-Jak.jsp"
geneurl = 'https://www.arabidopsis.org'

data = []
html = urllib.request.urlopen(url)

bsObj = BeautifulSoup(html,features='html.parser')
geneurllist = []

nuc_numer = bsObj.find_all(name='a', attrs={"href":re.compile(r"^http://arabidopsis\.org.*AT\w{7}")})

for i in nuc_numer:
    geneurllist.append(i['href'])

print(geneurllist)

def get_sequence(each):
    html1 = urllib.request.urlopen(each)
    bsObj1 = BeautifulSoup(html1,features='html.parser')

    temp = bsObj1.findAll('a')
    fastaurl = ''
    for i in temp:
        if i.get_text() == 'full length genomic':
            fastaurl = i['href']
            break

    driver = webdriver.PhantomJS(executable_path= '/usr/bin/phantomjs')
    driver.get(geneurl+fastaurl)

    try:
        sequence = driver.find_element_by_xpath("/html/body/div/div[2]/table/tbody/tr[8]/td[2]/p").text
    except:
        sequence = driver.find_element_by_xpath("/html/body/div/div[2]/table/tbody/tr[7]/td[2]/p").text

    sequence2 = re.sub(r'[( )(\d)]','',sequence)
    driver.close()
    sequence_name = ">"+each[-9:]
    return (sequence_name, sequence2)


for i in geneurllist:
    gene_infomation = get_sequence(i)
    file.write(gene_infomation[0]+'\n'+gene_infomation[1]+'\n')
file.close()


