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

print("------------------------- transform --------------------------------")
# transform xml with xslt
transRoot = transform(xmlRoot)
print("XML transRoot - ",transRoot)