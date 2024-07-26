# Boyer-Moore Voting Algorithm

## High-Level Overview
**Purpose of Algorithm**
The Boyer-Moore Voting Algorithm is a popular algorithm used to find the majority element in an array. 
A majority element is an element that appears more than ⌊n/2⌋ times, where n is the size of the array. 


**Speed and Space Complexity**
The algorithm operates in O(n) time and O(1) space

## Intuitive Understanding Via Examplar
Let's go through an example to illustrate the algorithm:

Suppose we have the array: [3, 3, 4, 2, 4, 4, 2, 4, 4].

**Initialization:**
candidate = None
count = 0

**First Pass:**

`3`: `count` is 0, so `candidate` = 3 and `count` = 1.
`3`: `candidate` is 3, so `count` = 2.
`4`: `candidate` is 3, so `count` = 1.
`2`: `candidate` is 3, so `count` = 0.
`4`: `count` is 0, so `candidate` = 4 and `count` = 1.
`4`: `candidate` is 4, so `count` = 2.
`2`: `candidate` is 4, so `count` = 1.
`4`: `candidate` is 4, so `count` = 2.
`4`: `candidate` is 4, so `count` = 3.
At the end of the first pass, the `candidate` is 4 with a `count` of 3.

**Second Pass (Verification):**

Count the occurrences of 4 in the array: 4 appears 5 times.
Since 5 > ⌊9/2⌋, 4 is the majority element.

## Procedure of Boyer-Moore Voting Algorithm
1. Step 1: Initialization
    - Start with two variables: `candidate` and `count`
    - Initialize `candidate` to `None`
    - Initialize `count` to `0`

2. Step 2: FIRST PASS
    - Iterate through the array for each element `num`
        - IF `count` is `0`, then:
            i. SET `candidate` to `num` 
            ii. SET `count` to `1`
        - IF `count` is NOT `0`, then:
            i. IF `num` is the same as `candidate` -> INCREMENT `count` by `1`
            ii. IF `num` is NOT THE SAME as `candidate` -> DECREMENT `count` by `1`

3. Step 3: SECOND PASS (Optional but recommended for verification):
    - After the first pass, candidate should be the majority element, if one exists.

    - Verify the candidate by counting its occurrences in the array. 
     - If it appears more than ⌊n/2⌋ times, it is the majority element; otherwise, there is no majority element.










































































































































