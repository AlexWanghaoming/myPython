import argparse

parser = argparse.ArgumentParser(formatter_class=argparse.RawDescriptionHelpFormatter, description=
                                 """
                                 You are Wanghaoming you are handsome
                                 """, epilog='hahaahahhahaa')

parser.add_argument('-v',action='version', version='%(prog)s v1.01', help="show program version",)    # %(prog)s is program name
parser.add_argument('-test', help="Just for test parse_args()", action='store_const', const="sds")  # default action is store
if __name__ == "__main__":
    print(parser.parse_args('-test'.split(" ")))

    # print("hello world!")

