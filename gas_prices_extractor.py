infile = open("csv/gas_prices.csv", "r")
outfile = open("csv/cleveland_gas_prices.csv", "w")


print(infile)
print(outfile)
print()

for line in infile:
    try:
        # print(line)
        date = line.split(",")[0]
        area = line.split(",")[2]
        product = line.split(",")[4]
        value = line.split(",")[10]
        if area == "CLEVELAND" and product == "Regular Gasoline":
            print(date, area, product, value)
        #     numpeoplekilled = int(line.split(",")[11])
        #     if numpeoplekilled > 0:
        #         print(line, file=outfile)
    except:
        print("Error!")
        print("Problem with the following line")
        print(line)

infile.close()
outfile.close()
