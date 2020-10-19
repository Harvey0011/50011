#!/bin/python3

import xml.dom.minidom as xmldom
import re

dom=xmldom.parse('./blocklist.xml')
root = dom.documentElement

def pe(Tag):
    re_em=re.compile(r'''(
                        [a-zA-Z0-9._%+-]+
                        @
                        [a-zA-Z0-9.-]+
                        (\.[a-zA-Z])    
                        )''', re.VERBOSE)
    items=root.getElementsByTagName(Tag)
    
    for i in range(len(items)):
        item=items[i]
        email=item.getAttribute("id")
        if re.match(re_em, email):
            print(item.toxml().split('\n')[0])
            
pe('emItem')
pe('pluginItem')
pe('gfxBlacklistEntry')


