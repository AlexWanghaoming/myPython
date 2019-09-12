def wordBreak(s, wordDict):
    wordDict.sort(key=lambda x: len(x))
    dp = []
    def helper(s):

        for i in range(len(s)):
            print(i,"len:",len(s))
            if s[0:i] in wordDict:
                print(s[0:i])
                # dp.append(True)
                s = s[i:len(s)]
                print("len:",len(s))
                if len(s) != 0:
                    helper(s)
                else:
                    print("Yeah")
                    dp.append(True)
                    # return True
            else:
                dp.append(False)
    # helper(s)
    return (helper(s), dp[len(dp)-1])





if __name__ == '__main__':
    s = "applepenapple"
    wordDict = ["apple","pen"]
    print(wordBreak(s, wordDict))