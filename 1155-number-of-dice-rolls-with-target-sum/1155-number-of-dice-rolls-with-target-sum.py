class Solution:
    def numRollsToTarget(self, n: int, k: int, target: int) -> int:
        count = [ 0 for _ in range(target+1) ]
        for k0 in range(1,k+1) :
            if k0<=target :
                count[k0] = 1
        updated = [ 0 for _ in range(target+1) ]
        for n0 in range(n-1) :
            for t0 in range(target+1) :
                updated[t0]=0
                for k0 in range(1,k+1) :
                    if t0-k0>=1 :
                        updated[t0] += count[t0-k0]
            count[:] = updated[:]           
        return count[target]%(10**9+7)
                    
        