from itertools import dropwhile
import re
import csv


def remove_lines_before_graph(infile):

    for line in infile:
        # Skip until the line containing [INFO] += org.some-dependency...
        if '+-' not in line and '\\-' not in line:
            continue
        yield line


def extract_groupid_artifactid_version(line):

    m = re.search(r' ([a-zA-Z0-9-_.]+):([a-zA-Z0-9-_.]+).*?([a-zA-Z0-9-_.]+):[^:]+$',
                  line)
    return m.groups()


def main(mvn_dtree_file_path):

    with open('dtree-mvn.csv', 'wt', encoding='utf-8') as outfile:
        csv_writer = csv.writer(outfile)

        with open(mvn_dtree_file_path, 'rt', encoding='ascii') as infile:
            for l in remove_lines_before_graph(infile):
                row = extract_groupid_artifactid_version(l)
                csv_writer.writerow(row)


if __name__ == '__main__':
    import sys
    if len(sys.argv) != 2:
        print(f'Usage: {__file__} <mvn-generated-dependency-tree>')
        exit()

    main(sys.argv[1])
