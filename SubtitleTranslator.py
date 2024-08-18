

firstFile = r"Files\[ENG]Gaki no Tsukai - No-Laughing Onsen Yugawara (2004) [bluray remux].ass"
secondFile = r" Files\[PT-BR]Gaki no Tsukai - No-Laughing Onsen Yugawara (2004).ass"


with open("outputFile", "w", encoding="UTF8") as output:
    with open(firstFile, "r", encoding="UTF8") as file, open(secondFile, "r", encoding="UTF8") as secondFile:
        print_mod = False
        while True:
            first_line = file.readline()
            second_line = secondFile.readline()

            if first_line == "":
                break
            if first_line.strip() == "[Events]":
                print("working")
                file.readline()
                a = secondFile.readline()
                print(a)
                print_mod = True

            elif print_mod is True:
                #
                # print("print_mod, working")
                print()
                first_split = first_line.split(",")
                second_split = second_line.split(",")
                print(f"First Split: {first_split}")
                print(f"Secnd Split: {second_split}")
                second_split[3] = first_split[3]
                new_line = ""
                for word in second_split:
                    new_line = new_line + word + ","
                # output.write(new_line[:-1])
            else:
                # output.write(first_line)
                pass
        secondFile.close()
        pass
