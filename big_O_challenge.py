# Explain, optimize, and benchmark your python code here.

## -----WEEK 1:------
# 99_bottles is O(n). because the amount that it runs is linear to the input
# algo_anagrams_i is O(n) the loop would increase as input does.
#    MEDIAN 0.0008344650268554688
#    MEAN   0.0007762908935546875
#    STDEV  0.0005478974136593445
# # algo-anagrams-ii is O(n^2) the inner loops depends on input from outer loop, this cannot be helped due to needing to count the letters in a string
#  independentley of the other words and then compare to test case.
#deaf_grandma is O(n) due to the time being directly influenced by input.
#factorial is O(n), time is linear to input.
        # MEDIAN 0.00286102294921875
        # MEAN   0.0029754638671875
        # STDEV  0.0012005579949851272
#fibonacci is O(n) time is linear to input.
        # MEDIAN 0.0040531158447265625
        # MEAN   0.0042877197265625
        # STDEV  0.0009086467552038744
#linear_search is O(n) because you have to loop through the entire array to find every input even as the input grows.
# # #
#roman_numerals is O(1) because you only have to touch each letter of the dictionary one time regardless of input size.(if you added multiple numbers as input this would become O(n))
#   MEDIAN 0.0035762786865234375
#   MEAN   0.003795623779296875
#   STDEV  0.000843295015694683
# # 
#algo-sum-pairs is O(n^2) because each number in the array needs to be checked against every other number. cannot be helped.
        # MEDIAN 0.0050067901611328125
        # MEAN   0.005159854888916016
        # STDEV  0.0021770186912038313

# algo-stock-picker is O(n) even though there is a nested for loop. the time would only increase proportionally to the amount of data added.
# FUNCTION: picker Used 500 times
#         MEDIAN 0.00286102294921875
#         MEAN   0.0030241012573242188
#         STDEV  0.001627008676958123
