class KMP:
    def computeLPSArray(self, pattern):
        lps = [0] * len(pattern)
        length = 0
        i = 1

        while i < len(pattern):
            if pattern[i] == pattern[length]:
                length += 1
                lps[i] = length
                i += 1
            else:
                if length != 0:
                    length = lps[length - 1]
                else:
                    lps[i] = 0
                    i += 1

        return lps

    def KMPSearch(self, text, pattern):
        m = len(pattern)
        n = len(text)

        lps = self.computeLPSArray(pattern)
        i = 0
        j = 0

        while i < n:
            if pattern[j] == text[i]:
                i += 1
                j += 1

            if j == m:
                print("Pattern at Index: ",i - j)
                j = lps[j - 1]
            elif i < n  and pattern[j] != text[i]:
                if j != 0:
                    j = lps[j - 1]
                else:
                    i += 1

kmp = KMP()
text = str(input())
pattern = str(input())
kmp.KMPSearch(text, pattern)
