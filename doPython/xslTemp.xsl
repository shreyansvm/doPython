<?xml version="1.0" encoding="utf-8"?>
<xsl:stylesheet xmlns:xsl="http://www.w3.org/1999/XSL/Transform" version="1.0">
<xsl:output method="text" encoding="iso-8859-1"/>
<xsl:param name="DUT" select="Dut-C"/>
<xsl:param name="TOPOLOGY"/>
<xsl:template match="/">

<xsl:for-each select="default/dut[@name='Dut-C']/var">
echo "######"<xsl:choose>
<xsl:when test="@val=''">
.set <xsl:value-of select="./text()"/>=False
echo <xsl:value-of select="./text()"/> is enabled:$(<xsl:value-of select="./text()"/>)</xsl:when>
<xsl:otherwise>
.set <xsl:value-of select="./text()"/>=<xsl:value-of select="@val"/>
echo <xsl:value-of select="./text()"/> is set:$(<xsl:value-of select="./text()"/>)</xsl:otherwise>
</xsl:choose>
echo "######"

</xsl:for-each>

.if $(customer) == True {
    echo "customer config is enabled"
.endif }
.if $(customer) != True {
    echo "customer config is not enabled"
.endif }

.if $(DPI) == True {
    echo "dpiConfig config is enabled"
.endif }
.if $(DPI) != True {
    echo "dpiConfig config is not enabled"
.endif }

echo PHYSTOPOLOGY is $(PHYSTOPOLOGY)

</xsl:template>
</xsl:stylesheet>

