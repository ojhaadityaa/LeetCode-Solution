#User function Template for python3

class Solution:
    def permutation (self, S):
        # code here
        ans = []
        p = S[0]
        self.helper(p, S[1:], ans)
        return ans

    def helper(self, p, s, ans):
        if len(s) == 0:
            ans.append(p)
            return
        ch = s[0]
        self.helper(p+' '+ch, s[1:], ans)
        self.helper(p+ch, s[1:], ans)




#{ 
 # Driver Code Starts
#Initial Template for Python 3



if __name__ == '__main__': 
    ob = Solution()
    t = int (input ())
    for _ in range (t):
        S = input()
        ans = ob.permutation(S);
        write = "";
        for i in ans:
            write += "(" + i + ")"
        print(write)


# } Driver Code Ends