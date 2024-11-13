infile = open("gas_prices.csv", "r")
outfile = open("cleveland_gas_prices.csv", "w")


print(infile)
print(outfile)
print()

for line in infile:
    try:
        print(line)
        # date = line.split(",")[0]
        # year = date[-4:]
        # if year == "2024":
        #     numpeoplekilled = int(line.split(",")[11])
        #     if numpeoplekilled > 0:
        #         print(line, file=outfile)
    except:
        print("Error!")
        print("Problem with the following line")
        print(line)

infile.close()
outfile.close()
