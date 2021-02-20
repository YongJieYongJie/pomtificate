import csv

def write_new_dependencies_to_file(dep_to_add, outfile, scope):

    import xml.etree.ElementTree as ET
    deps = ET.Element('dependencies')

    for group_id, artifact_id, version in dep_to_add:
        dep_root = ET.SubElement(deps, 'dependency')
        gid = ET.SubElement(dep_root, 'groupId')
        gid.text = group_id
        aid = ET.SubElement(dep_root, 'artifactId')
        aid.text = artifact_id
        ver = ET.SubElement(dep_root, 'version')
        ver.text = version
        if scope and scope != 'compile':
            ver = ET.SubElement(dep_root, 'scope')
            ver.text = scope

    root = ET.ElementTree(deps)
    with open(outfile, 'wt', encoding='utf-8') as out_xml_file:
        root.write(out_xml_file, encoding='unicode')

def main(sbt_dep_file, mvn_dep_file, outfile, scope):

    sbt_dep_map = parse_dependency_map(sbt_dep_file, delimiter=':')
    mvn_dep_map = parse_dependency_map(mvn_dep_file, delimiter=':')

    dep_to_add = []

    for sbt_dep, sbt_dep_version in sbt_dep_map.items():
        if sbt_dep not in mvn_dep_map:
            print(f'[!] Dependency {sbt_dep} missing in {mvn_dep_file}')
            dep_to_add.append(list(sbt_dep) + [sbt_dep_version])
        elif mvn_dep_map[sbt_dep] != sbt_dep_version:
            print(f'[!] Mismatched dependency for {sbt_dep}: '
                  f'{sbt_dep_version} in {sbt_dep_file} vs '
                  f'{mvn_dep_map[sbt_dep]} in {mvn_dep_file}')
            dep_to_add.append(list(sbt_dep) + [sbt_dep_version])

    for mvn_dep, mvn_dep_version in mvn_dep_map.items():
        if mvn_dep not in sbt_dep_map:
            print(f'[!] Dependency {mvn_dep} missing in {sbt_dep_file}')

    write_new_dependencies_to_file(dep_to_add, outfile, scope)

def parse_dependency_map(csv_file_path, delimiter=','):

    dependency_map = {}

    with open(csv_file_path, 'rt', encoding='utf-8') as csv_file_path:
        csv_reader = csv.reader(csv_file_path, delimiter=delimiter)
        for row in csv_reader:
            dependency_map[tuple(row[:2])] = row[2]

    return dependency_map


if __name__ == '__main__':
    import sys
    if len(sys.argv) != 5:
        print(f'Usage: {__file__} <sbt-dependency-csv> <mvn-dependency-csv> '
              '<output-file> <scope>')
        exit()

    sbt_dep_file, mvn_dep_file, outfile, scope = sys.argv[1:]
    main(sbt_dep_file, mvn_dep_file, outfile, scope)
