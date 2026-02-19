import logging 

def main():
    with open("signal.txt", 'r') as in_file:
        pluses = 0
        characters = 0
        next_char = in_file.read(1)
        while next_char != "":
            characters += 1
            if next_char == "+":
                pluses += 1
            if next_char == "0":
                logging.warning("0 found at position {}".format(characters))
            if next_char == "-":
                logging.info("- found at position {}".format(characters))
            if next_char not in "+-0":
                logging.error("At position {}, bad character {} found".format(characters, next_char))
            next_char = in_file.read(1)
        perc = pluses / characters * 100
        print("Answer is {}".format(round(perc)))


if __name__ == "__main__":
    logging.basicConfig(filename = "signal.log",
                        level=logging.ERROR,
                        filemode='w')
    main()
