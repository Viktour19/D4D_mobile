infile = open('cities_regionID.csv', 'r')
all_lines = infile.readlines()
all_lines.pop(0)

region_towers = {}
for line in all_lines:
    content = line.rstrip('\n').split(',')
    if '"' in content[-1]:
	region = content[-1].strip('"') 
	try:
	    region_towers[region] += 1
	except KeyError:
	    region_towers[region] = 1
outfile = open('region_towers.txt', 'w')
write_lines = []
for region, count in region_towers.items():
    newline = region + '\t' + str(count) + '\n'
    write_lines.append(newline)
outfile.writelines(write_lines)
outfile.close()

