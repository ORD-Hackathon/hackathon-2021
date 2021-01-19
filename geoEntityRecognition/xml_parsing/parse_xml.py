from lxml import etree as et

tree = et.parse('test.xml')
root = tree.getroot()
# print(et.tostring(root, pretty_print=True).decode())
for element in root:
    for subelement in element:
        print(subelement.tag, subelement.text)