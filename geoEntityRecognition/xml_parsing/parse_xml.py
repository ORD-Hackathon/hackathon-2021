from lxml import etree as et

tree = et.parse('cities_example.xml')
root = tree.getroot()
# print(et.tostring(root, pretty_print=True).decode())
print(root.tag)
# for element in root:
#     for subelement in element:
#         print(subelement.tag, subelement.text)