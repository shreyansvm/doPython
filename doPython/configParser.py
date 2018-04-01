#!/usr/bin/env python
# -*- coding:utf-8 -*-
import os
from lxml import etree

print("Hello XML")

xmlPath = '/home/rough/xmlTemp.xml'
xslPath = '/home/rough/xslTemp.xsl'

print("------------------------- XSL --------------------------------")
# read xsl file
xslRoot = etree.parse(xslPath)
print("XSL Root - ",xslRoot)

transform = etree.XSLT(xslRoot)
print("XSL transform - ",transform)

print("------------------------- XML --------------------------------")
# read xml
xmlRoot = etree.parse(xmlPath)
print("XML Root - ",xmlRoot)

xmlTemplate = "/tmp/"+str(uuid.uuid4())
print(etree.tostring(xmlRoot,
        pretty_print=True,
        xml_declaration=True, encoding='US-ASCII').decode(), file=open(xmlTemplate, "w"))

print("------------------------- transform --------------------------------")
# transform xml with xslt
# transRoot = transform(xmlRoot)
# print("XML transRoot - ",transRoot)

# OR ----

outfile = '/tmp/config_file_'

# xsltproc is a command line tool for applying XSLT stylesheets to XML documents
# http://xmlsoft.org/XSLT/xsltproc2.html
# Synatx : xsltproc <XSL file> <XML Topo file> > <Output config file>
cmd = "xsltproc {} {} > {}".format(xslPath, xmlTemplate, outfile)
os.system(cmd)

try:
	# delete the temporary XML Topo template
    os.remove(xmlTemplate)
except OSError:
    print('---- OSError ----')s

print("------------------------- done --------------------------------")