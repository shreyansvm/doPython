<?xml version="1.0" encoding="utf-8"?>
<xsl:stylesheet xmlns:xsl="http://www.w3.org/1999/XSL/Transform" version="1.0">
<xsl:output method="text" encoding="iso-8859-1"/>
<xsl:param name="DUT" select="Dut"/>
<xsl:param name="TOPOLOGY"/>
<xsl:template match="/">

<xsl:for-each select="default/dut[@name='Dut']/var">
echo "######"
<xsl:choose>
<xsl:when test="@val=''">
.set <xsl:value-of select="@val"/>=False
echo <xsl:value-of select="@val"/> is disabled:$(<xsl:value-of select="@val"/>)</xsl:when>
<xsl:when test="@val='VzW'">
Hello World
</xsl:when>
<xsl:otherwise>
.set <xsl:value-of select="@val"/>=<xsl:value-of select="./text()"/>
echo <xsl:value-of select="@val"/> is set:$(<xsl:value-of select="@val"/>)</xsl:otherwise>
</xsl:choose>
echo "######"

</xsl:for-each>

echo PHYSTOPOLOGY is $(PHYSTOPOLOGY)
echo SUBTOPOLOGY is $(SUBTOPOLOGY)

<xsl:variable name="author"
              select="'Shreyans'"/>
Author:  <xsl:text/>
   <xsl:value-of select="$author" />


<xsl:if test="default/dut[@name='Dut']/var='customer'">
    Doing some customer config
</xsl:if>

<xsl:if test="default/dut[@name='Dut']/var='ABC' and default/dut[@name='Dut']/var/@val='customer'">
    # ------------------------ customer is ABC ------------------------

    .if $(customer) == ABC {
    echo "ABC customer config is enabled"
    .endif }
</xsl:if>
<xsl:if test="default/dut[@name='Dut']/var='DEF' and default/dut[@name='Dut']/var/@val='customer'">
    # ------------------------ customer is DEF ------------------------

    .if $(customer) == DEF {
    echo "DEF customer config is enabled"
    .endif }
</xsl:if>
<xsl:if test="default/dut[@name='Dut']/var='Enable' and default/dut[@name='Dut']/var/@val='icr'">
    # ------------------------ Adding Geo-Red config ------------------------

    .if $(icr) == True {
    echo "icr is enabled"
        <xsl:if test="(default/dut[@name='Dut']/var='Enable') and (default/dut[@name='Dut']/var/@val='trap')">
        .if $(trap) == True {
            echo "trap is enabled"
        .endif }
        </xsl:if>
    .endif }
</xsl:if>
<xsl:if test="default/dut[@name='Dut']/var='Enable' and default/dut[@name='Dut']/var/@val='dpi'">
    # ------------------------ Adding DPI config ------------------------

    .if $(dpi) == True {
    echo "dpi is enabled"
    .endif }
</xsl:if>

</xsl:template>
</xsl:stylesheet>

