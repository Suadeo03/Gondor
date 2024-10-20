import xml.etree.ElementTree as ET

tree = ET.parse('C:\\Users\\brian\\PycharmProjects\\Gondor\\resources\\nlm.xml')
root = tree.getroot()
root.tag = 'Concept'
root.attrib = {}
new_list = []
for child in root[0][0]:
    new_list.append(child.attrib)

sentanceObj = []
i=0
while i< len(new_list):
    sentanceObj.append(new_list[i]['displayName'])
    i=i+1


