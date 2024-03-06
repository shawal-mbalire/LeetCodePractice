class Solution:
    def minimumLength(self, s: str) -> int:
        while True:
            chars = ['a','b','c']
            if len (s) == 0: return 0
            prefix = s[0]
            suffix = s[-1]
            if prefix != suffix: return len(s)
            if len (s) == 0: return 0
            pref_index = 0
            suff_index = len(s)-1
            while suff_index > pref_index:
                if s[pref_index+1]==prefix: 
                    prefix + s[pref_index+1]
                    pref_index+=1
                if s[suff_index-1]==suffix: 
                    suffix + s[suff_index-1]
                    suff_index-=1
                if s[pref_index+1]!=prefix: break
                if s[suff_index-1]!=suffix: break
                
            s = s.removeprefix(prefix)
            s = s.removesuffix(suffix)

        # minimumLength(s)

soln = Solution()
ans = soln.minimumLength("aabccabba")
print(ans)