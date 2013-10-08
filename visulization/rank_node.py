fname = 'cdr_10.csv'
infile = open(fname, 'r')
#infile = open('pref_MIGR.csv', 'r')
all_lines = infile.readlines()
header = all_lines.pop(0)
sorted_lines = sorted(all_lines, key=lambda x:int(x.split(',')[-1]), reverse=True)

max = int(sorted_lines[0].split(',')[-1])
min = int(sorted_lines[-1].split(',')[-1])
thr = 0.01
write_lines = [header]
for line in sorted_lines:
    content = line.rstrip('\n').split(',')
    content[-1] = str((float(content[-1]) - min) / (max - min))
    if float(content[-1]) > thr:
        newline = ','.join(content) + '\n'
        write_lines.append(newline)

outfile = open('sorted_' + fname, 'w')
#outfile = open('sorted_pref_MIGR.csv', 'w')
outfile.writelines(write_lines)
outfile.close()
