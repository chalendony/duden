import duden

def main():

    # find the correct url

    # get definition and examples
    w1 = duden.get('einfach_einmal_simpel')
    # remove beispiel code to get the meanings???
    print(w1.meaning_example)

    # change the depth, include code



if __name__ == '__main__':
    main()
