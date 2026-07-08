class Solution(object):
    def validIPAddress(self, queryIP):
        """
        :type queryIP: str
        :rtype: str
        """

        def v4(queryIP) :
            arr = list(map(str, queryIP.split(".")))
            if len(arr) != 4 :
                return "Neither"
            for i in arr :
                if not i :
                    return "Neither"
                if not i.isdigit() :
                    return "Neither"
                if int(i) > 255 or int(i) < 0 :
                    return "Neither"
                if i[0] == "0" and len(i) != 1 :
                    return "Neither"
            return "IPv4"
        def v6(queryIP) :
            arr = list(map(str, queryIP.split(":")))
            if len(arr) != 8 :
                return "Neither"
            for i in arr :
                if len(i) > 4 or len(i) < 1 :
                    return "Neither"
                for j in i :
                    if (not j.isdigit()) and (j.lower() < 'a' or j.lower() > 'f') :
                        return "Neither"
            return "IPv6"                

        if ":" in queryIP and "." in queryIP :
            return "Neither"
        if ":" in queryIP :
            return v6(queryIP)
        if "." in queryIP :
            return v4(queryIP)
        else :
            return "Neither"