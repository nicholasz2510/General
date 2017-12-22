output_file = open("13(file).txt", "w")

for x in range(1, 101):
    output_file.write("")
    for y in range(1, 101):
        if len(str(x * y)) == 1:
            output_file.write(str(x * y) + "    |",)
        elif len(str(x * y)) == 2:
            output_file.write(str(x * y) + "   |",)
        elif len(str(x * y)) == 3:
            output_file.write(str(x * y) + "  |",)
        elif len(str(x * y)) == 4:
            output_file.write(str(x * y) + " |",)
        elif len(str(x * y)) == 5:
            output_file.write(str(x * y) + "|",)
output_file.close()