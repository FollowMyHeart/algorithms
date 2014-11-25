# author:Michael Huang
# date:2014.11.25
#
# 此算法为时间复杂度为O(N^2)的计算最大子序列方法，方法容易实现，但效率不高。
def MaxSubsequenceSum(seq):
    max_sum = seq[0]
    max_from = 0
    max_to = 0
    for i in range(len(seq)):
        this_sum = 0
        for j in range(i,len(seq)):
            this_sum += seq[j]
            if this_sum > max_sum:
                max_sum = this_sum
                max_from = i
                max_to = j
    print("The max subsequence sum is ", max_sum)
    print("The max subsequence is ",[seq[i] for i in range(max_from, max_to+1)])
    return max_sum


## The max subsequence sum is  25
## The max subsequence is  [9, 7, -4, -7, 11, 9]
seq = [1, -3, 22, -9,-23, 2, -11, 9, 7,-4,-7,11,9]
MaxSubsequenceSum(seq)

## 处理都是负数的情况
## The max subsequence sum is  -1
## The max subsequence is  [-1]
seq2 = [-3, -4, -9, -7,-1,-20]
MaxSubsequenceSum(seq2)


### 这种方法有误，仍待解决
##def MaxSubSum(seq, left, right):
##    max_left_sum_with_border = 0
##    max_right_sum_with_border = 0
##    left_border_sum = 0
##    right_border_sum = 0
##    max_left_sum = 0
##    max_right_sum = 0
##
##    if(left == right):
##        if seq[left] > 0:
##            return seq[left]
##        else:
##            return 0
##
##    center = (left + right) // 2
##    max_left_sum = MaxSubSum(seq, left, center)
##    max_right_sum = MaxSubSum(seq, center+1, right)
##
##    max_left_sum_with_border = 0
##    left_border_sum = 0
##    for i in range(center, left-1, -1):
##        left_border_sum += seq[i]
##        if(left_border_sum > max_left_sum_with_border):
##            max_left_sum_with_border = left_border_sum
##    
##    max_right_sum_with_border = 0
##    right_border_sum = 0
##    for i in range(right-1, center, -1):
##        right_border_sum += seq[i]
##        if(right_border_sum > max_right_sum_with_border):
##            max_right_sum_with_border = right_border_sum
##
##    return max(max(max_left_sum, max_right_sum),max_left_sum_with_border+max_right_sum_with_border)
##
##def MaxSubsequenceSum2(seq):
##    return MaxSubSum(seq, 0, len(seq)-1)
##
##seq = [1, -3, 22, -9,-23, 2, -11, 9, 7,-4,-7,11,9]
##print(MaxSubsequenceSum2(seq))


## 这种方法的时间复杂度为O(N),但是不容易想到。
def MaxSubsequenceSum3(seq):
   this_sum = max_sum = seq[0]
   min_i = max_i = 0
   for i in range(len(seq)):
       this_sum += seq[i]
       if(this_sum > max_sum):
           max_sum = this_sum
           max_i = i
       elif this_sum < 0:
           this_sum = 0
           min_i = i

   if max_sum <=0 :
       print("The max subsequence sum is ",max_sum)
       print("The max subsequence is ",[max_sum])
   else:
       print("The max subsequence sum is ", max_sum)
       print("The max subsequence is ",[seq[i] for i in range(min_i+1, max_i+1)])
   return max_sum 

#seq = [1, -3, 22, -9,-23, 2, -11, 9, 7,-4,-7,11,9]
MaxSubsequenceSum3(seq)

#seq2 = [-3, -4, -9, -7,-1,-20]
MaxSubsequenceSum3(seq2)
