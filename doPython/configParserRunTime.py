
# import os
# from lxml import etree
#
# print("Hello XML")
#
# xmlPath = '/Users/BytePython/PycharmProjects/doPython/xmlTemp.xml'
# xslPath = '/Users/BytePython/PycharmProjects/doPython/xslTemp.xsl'
#
# print("------------------------- XSL --------------------------------")
# # read xsl file
# xslRoot = etree.parse(xslPath)
# print("XSL Root - ",xslRoot)
#
# transform = etree.XSLT(xslRoot)
# print("XSL transform - ",transform)
#
# print("------------------------- XML --------------------------------")
#
#
# outfile = 'run_time_config_file'

import os
import lxml.etree as ET

xmlPath = '/Users/BytePython/PycharmProjects/doPython/xmlTemp.xml'
xslPath = '/Users/BytePython/PycharmProjects/doPython/xslTemp.xsl'
outfile = 'run_time_config_file'

dom = ET.parse(xmlPath)
print(dom)
xslt = ET.parse(xslPath)
print(xslt)
transform = ET.XSLT(xslt)
print(transform)
newdom = transform(dom)
print(newdom)
print(ET.tostring(newdom, pretty_print=True))

cmd = "xsltproc {} {} > {}".format(xslPath, xmlPath, outfile)
os.system(cmd)
