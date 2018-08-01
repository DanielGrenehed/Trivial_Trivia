# -*- coding: UTF-8 -*-

import string

def PlaceAcute(s):
    cuts =[]
    for i in range(len(s)):
        if (s.startswith("acute;", i)): cuts.append(i)
    if len(cuts) == 0: return s
    fs = ""
    lc = 0
    for i in cuts:
        fs+=s[lc:i-2]+s[i-1:i]+u"´"
        lc= i+6
    return fs


def CS(s):
    replacements = {"&quot;":'"', "&#039":"'", "&shy;":"-", 
        "&aring;":u"å", "&auml;":u"ä", "&ouml;":u"ö", "&amp;":u"&", 
        u"';":"'", "&rdquo;":u'”', "&ldquo;":u'“', "&rsquo;":u"’", "&hellip;":u"..."}
    cs = PlaceAcute(s)
    for k, v in replacements.items():
        cs = cs.replace(k, v)
    return cs