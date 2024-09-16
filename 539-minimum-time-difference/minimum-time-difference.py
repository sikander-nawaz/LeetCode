class Solution:
    def findMinDifference(self, timePoints: List[str]) -> int:
        dp=[0 for i in range(24*60)]
        for time in timePoints:
            t=int(time[0])*10*60 + int(time[1])*60 + int(time[3])*10 + int(time[4])
            if dp[t]!=0: return 0
            dp[t]=1
        prev,first,ans=-1,-1,inf
        for i in range(24*60):
            if dp[i]==0: continue
            if prev==-1: prev=first=i
            else:
                ans=min(ans,i-prev)
                prev=i
        ans=min(ans,24*60-(prev-first))
        return ans