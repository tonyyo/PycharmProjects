class Solution(object):
    #todo 超时
    def splitArray0(self, nums):
        N = len(nums)
        f = [1000001] * N  # f[i] 表示nums截止第i个位置时，切分数组所得子数组数的最小值，那么f[i] = min(f[j] + 1)
        f[0] = 1
        for i in range(1, len(f)):
            for j in range(i):
                if self.gcd(nums[i], nums[j]) > 1:
                    if j == 0:  # 匹配到了第一个数
                        f[i] = 1
                        break
                    else:
                        f[i] = min(f[i - 1] + 1, f[j - 1] + 1)  # 比较所有可能情况的最小值，核心状态转移方程
                        if f[i] == 80:
                            print()
            if f[i] == 1000001:  # 没有匹配到任何数
                f[i] = f[i - 1] + 1
        print(f)
        return f[N - 1]

    def gcd(self, num1, num2):
        while num1 != 0:
            num1, num2 = num2 % num1, num1   # 只需要记住这样做能保证num2能够大于num1，所以要将num2 % num1的值赋给num1
        return num2

if __name__ == '__main__':
    solution = Solution()
    nums1 = [579583,514379,326159,374399,562283,656423,3719,515663,613141,637939,594137,186799,590963,91193,510379,176989,178141,663857,123091,812639,521359,550831,340939,379877,599,427957,566617,270443,458863,320027,724481,741679,782191,97423,622247,764611,347287,371359,860077,838069,862501,842939,849419,842077,870577,891629,882083,881437,883537,881233,888059,886583,879371,890563,894763,893281,893449,888557,887503,889769,881591,885793,894689,892123,880361,880409,895649,881411,894449,879539,890887,881597,895777,894427,885713,894211,893339,879689,889921,894871,882139,885679,889769,885961,889877,892219,890441,883489,895211,881407,894871,887633,879673,881963,881099,884497,880799,886609,916129,944417]
    nums = [2,3,3,2,3,3]
    print(solution.splitArray0(nums1))
