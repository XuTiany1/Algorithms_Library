# Boyer-Moore Voting Algorithm

## High-Level Overview
**Purpose of Algorithm**
The Boyer-Moore Voting Algorithm is a popular algorithm used to find the majority element in an array. 
A majority element is an element that appears more than ⌊n/2⌋ times, where n is the size of the array. 


**Speed and Space Complexity**
The algorithm operates in O(n) time and O(1) space

## Intuitive Understanding Via Example
Let's go through an example to illustrate the algorithm:

Suppose we have the array: [3, 3, 4, 2, 4, 4, 2, 4, 4].

**Initialization:**
candidate = None
count = 0

**First Pass:**
- `3`: `count` is 0, so `candidate` = 3 and `count` = 1.
- `3`: `candidate` is 3, so `count` = 2.
- `4`: `candidate` is 3, so `count` = 1.
- `2`: `candidate` is 3, so `count` = 0.
- `4`: `count` is 0, so `candidate` = 4 and `count` = 1.
- `4`: `candidate` is 4, so `count` = 2.
- `2`: `candidate` is 4, so `count` = 1.
- `4`: `candidate` is 4, so `count` = 2.
- `4`: `candidate` is 4, so `count` = 3.
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



## Why does this method work? -> Diving Deeper to the Logic


The Boyer-Moore Voting Algorithm works due to the inherent properties of the majority element and how it handles counts during the traversal of the array.


Some key properties that allowed this algorithm to function are the following:

**Majority Element Property:**
>:bulb: The majority element is defined as the element that appears more than ⌊n/2⌋ times in the array of size n.

**Balancing Counts:**
>:bulb: By using a counter that increases for the candidate and decreases for non-candidates, the algorithm leverages the fact that the majority element, if it exists, will balance out all other elements due to its higher frequency.



## Why does this method work? -> Mathematical Justification

- Suppose the majority element is `M` and it appears more than ⌊n/2⌋ times.
- Whenever we encounter `M`, we increment the `count`.
- Whenever we encounter an element different from `M`, we decrement the `count`.
- Since `M` appears more frequently than any other element, the count will be positive by the end of the array. This is because the majority element `M` will offset the influence of all other elements combined.

**Mathematical Justification:**

- Let the number of occurrences of `M` be `x`, and the number of occurrences of all other elements be `y`.
- By definition, $x > \frac{n}{2}\$ and $y < \frac{n}{2} \$.
- During the traversal, when we encounter `M`, the `count` increases by 1.
- When we encounter a different element, the `count` decreases by 1.
- The net effect is that `M` will push the count positively, as it has more occurrences to counteract the decrement caused by other elements.




























































































































