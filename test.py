class Solution(object):

    def __init__(self):
        self.anser = []
        self.cureent = []
        self.count = 0

    def process(self, candidates, target):

           self.count+=1
           for i in range (len(candidates)):

               self.cureent.append(candidates[i])

               if sum(self.cureent) == target:
                   #print(self.cureent)
                   self.anser.append(list(self.cureent))
                   self.cureent.pop()
                   break

               elif sum(self.cureent)  < target:

                   self.process(candidates[i:] , target)
                  # print(self.cureent)
                   self.cureent.pop()
               else :

                   self.process(candidates[i+1: ], target)
                   self.cureent.pop()


    def combinationSum(self, candidates, target):
        candidates.sort()
        print(candidates)
        self.process(candidates , target)
        print(self.count)
        return self.anser


s= Solution()
print(len(s.combinationSum([48,22,49,24,26,47,33,40,37,39,31,46,36,43,45,34,28,20,29,25,41,32,23] , 69)))