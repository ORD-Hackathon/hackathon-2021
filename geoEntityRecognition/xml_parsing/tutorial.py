from lxml import etree
 
root = etree.Element("users")

user1 = etree.SubElement(root, "user")
name1 = etree.SubElement(user1, "name")
name1.text = "Amanda"
age1 = etree.SubElement(user1, "age")
age1.text = "21"

user2 = etree.SubElement(root, "user")
name2 = etree.SubElement(user2, "name")
name2.text = "Tom"
age2 = etree.SubElement(user2, "age")
age2.text = "38"

with open('test.xml', 'wb') as f:
    f.write(etree.tostring(root, pretty_print=True))
