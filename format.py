# -*- coding: UTF-8 -*-

import string

class String_Formatting_Object:

    replace_s = {"&quot;":'"', "&#039":"'", "&shy;":"-",
        "&aring;":u"å", "&auml;":u"ä", "&ouml;":u"ö", "&amp;":u"&",
        u"';":"'", "&rdquo;":u'”', "&ldquo;":u'“', "&rsquo;":u"’", "&hellip;":u"..."}

    def __init__(self, string):
        self.string = string
        self.f_string = False

    def __Locate(self, prefix):
        loc =[]
        for i in range(len(self.string)): #find prefix
            if self.string.startswith(prefix, i): loc.append(i)
        if len(loc) == 0: return False
        return loc

    def __Acute(self):
        cuts = self.__Locate("acute;")
        if cuts == False:
            self.a_string = self.string
            return
        temp_s = ""
        lower_cut = 0
        for i in cuts:
            temp_s += self.string[lower_cut:i+2] + self.string[i-1:i] + u"´"
            lower_cut = i + 6
        self.a_string = temp_s

    def __Format(self):
        self.__Acute()
        temp_s = self.a_string
        for k, v in self.replace_s.items():
            temp_s = temp_s.replace(k, v)
        self.f_string = temp_s

    def GetFormattedString(self):
        if self.f_string != False: return self.f_string
        self.__Format()
        return self.f_string

    def GetString(self):
        return self.string

    def SetString(self, string):
        self.string = string
        self.f_string = False

    @staticmethod
    def CreateFormattedString(string):
        obj = String_Formatting_Object(string)
        return obj.GetFormattedString()

"""
def PlaceAcute(s):
    cuts =[]
    for i in range(len(s)): #find prefix
        if (s.startswith("acute;", i)): cuts.append(i)
    if len(cuts) == 0: return s
    out_string = ""
    lower_cut = 0
    for i in cuts: #replace text
        out_string += s[lower_cut:i-2] + s[i-1:i] + u"´"
        lower_cut = i + 6
    return out_string


def FormatString(s):
    replace = {"&quot;":'"', "&#039":"'", "&shy;":"-",
        "&aring;":u"å", "&auml;":u"ä", "&ouml;":u"ö", "&amp;":u"&",
        u"';":"'", "&rdquo;":u'”', "&ldquo;":u'“', "&rsquo;":u"’", "&hellip;":u"..."}

    f_string = PlaceAcute(s)

    for k, v in replace.items():
        f_string = f_string.replace(k, v)
    return f_string
"""
