# Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.

# You may assume that each input would have exactly one solution, and you may not use the same element twice.

# You can return the answer in any order.


# first submission with ruby

# def two_sum(nums, target)
#     indices = []
#     nums.each_with_index do |num1, index1|
#         nums.each_with_index do |num2, index2|
#             if index2 > index1 && num1 + num2 == target 
#                 indices << index1
#                 indices << index2
#             end 
#         end 
#     end 

#     indices
# end

# second submission with js

