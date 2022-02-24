# hashcode-2022-practice-problem

Solutions for the 2022 practice round problem.

To run the algorithm run in terminal: `python3 run.py`

## Brief Description

Given a list of clients with ingredients they like and dislike we want to create a single pizza that satisfies the maximum number of customers i.e.
- The pizza should contain all ingredients a customer likes
- The pizza should not contain any ingredient a customer likes

## Implemented Algorithms 

- A brute force approach. 
- A greedy search where we add /remove the ingredients iteratively until adding / removing a new one will not lead to a better state.
