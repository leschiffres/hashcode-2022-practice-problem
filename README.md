# hashcode-2022-practice-problem

Solutions for the 2022 practice round problem.

To run the algorithm run in terminal: `python3 run.py`

## Brief Description

Given a list of clients with ingredients they like and dislike we want to create a single pizza that satisfies the maximum number of customers i.e.
- The pizza should contain all ingredients a customer likes
- The pizza should not contain any ingredient a customer likes

## Implemented Algorithms 



### Some intuition

- Files:
    - `a_an_example.in.txt` : Total ingredients: 6, total clients: 3
    - `b_basic.in.txt` : Total ingredients: 6, total clients: 5
    - `c_coarse.in.txt` : Total ingredients: 10, total clients: 10
    - `d_difficult.in.txt` : Total ingredients: 600, total clients: 9368
    - `e_elaborate.in.txt` : Total ingredients: 10000, total clients: 4986
- **Brute Force** is the first option by considering all possible sets of ingredients. It's possible for the first 3 files, but then it's not anymore feasible.
- **Greedy Search** As we can add any number of ingredients we want, non disliked ingredients should be part of the optimal solution
    - Thus we can build a solution by considering all the ingredients and then excluding the most disliked ones. Maybe local search could help.
    - One algorithm could be the following: 
        1. Add all the ingredients 
        2. Iteratively exclude the most disliked one if this leads to a better state.
    - Greedy search incrementally
        1. Add all the ingredients not disliked by anyone
        2. Iteratively add the most liked ingredient
    - The problem with the greedy search is that we do not consider specific subsets but all the elements have a specific order. e.g. if we have ingredients (a,b,c,d) with this specific liked/dislike order. The optimal solution might contain elements (a,d) which we would not be able to track down since greedy search would remove them one by one from left to right and the same applies to the incremental greedy search.
        - One way to tackle this problem, would be to use again greedy search, but instead looking all possible subsets for the next k elements.
        - Another way would be to do a branch and bound approach.
- **Branch and Bound approach**
    1. Initially the upper bound is the whole set of users
    2. For every ingredient we have two options. To add it in the pizza or not. 
        - If we add it in the pizza then the upper bound is reduced by the number of users that dislike it. 
        - If we do not add it in the pizza then the upper bound is reduced by the number of users that like it.
        - (This is not entirely true though. When we exclude iteratively users, we might exclude the same users twice. Thus, we have to keep a set of users that are removed whenever a liked ingredient is excluded and whenever a disliked ingredient is excluded)
        - For the ordering we can choose any of the ones that we did in the greedy search. Let's say we start with the one of the incremental greedy search.
        - First for sure we start with a solution that considers all ingredients not disliked by anyone and then we expand it.
        - As a basic pruning method we can use the existing solutions. If the solution provided is not going to lead to a better solution an existing one we prune it.
        - We could also exclude ingredients that are more disliked than liked, but that would lead potentially excluding optimal solutions.
