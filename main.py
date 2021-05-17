from Scanner import Scanner
from Parser import Parser

def main():

    while(True):

        Input=input()

        if Input == "q" or Input == "Q":
            break

        sccaner=Scanner(Input)

        if(sccaner.get_tokens() == True):
            pass
            #print(sccaner.tokens)
        else:
            print("some thing wrong with sccaner")
            continue

        parser=Parser(sccaner.tokens)
        output=parser.compute_exp()

        if parser.error :
            print("some thing wrong with parser")
        else:
            print(output)

if __name__ == '__main__':
    main()