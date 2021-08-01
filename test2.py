


class Solution:
    def combinationSum(self, candidates, target) :

        def reshape(candidates):
            can1 = []
            index = []

            for i in candidates:
                if i not in can1:
                    can1.append(i)
                    index.append(0)
                else:
                    index[can1.index(i)]+=1

            return (can1 , index)


        def dfs(candidates , can_index, path ,size , begin , res , target):

            if target < 0:
                return
            if target == 0:
                res.append(path)
                return

            for i in range(begin, size):
                if can_index[i]!=0:
                   can_index[i] = can_index[i] - 1
                   dfs(candidates , can_index, path+[candidates[i]] , size , i , res , target-candidates[i])
                   can_index[i] = can_index[i] +1

                else:
                   dfs(candidates,  can_index,path + [candidates[i]], size, i+1, res, target - candidates[i])
        candidates , can_index = reshape(candidates)

        print(candidates , can_index)

        size = len(candidates)
        path = []
        res = []
        begin = 0

        dfs(candidates, can_index, path ,size , begin , res , target)
        return res




s= Solution()
print(s.combinationSum( [3,1,3,5,1,1] , 8))