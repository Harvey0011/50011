#!/bin/python3

import xml.dom.minidom as xmldom
import re

dom=xmldom.parse('./blocklist.xml')
root=dom.documentElement

def pbID(Tag):
    re_blockID=re.compile(r'^(i|g)\d*$')
    items=root.getElementsByTagName(Tag)
    for i in range(len(items)):
        item=items[i]
        id=item.getAttribute("blockID")
        if re.match(re_blockID, id) :
            print(item.toxml().split('\n')[0])
          

pbID('emItem')
pbID('pluginItem')
pbID('gfxBlacklistEntry')


