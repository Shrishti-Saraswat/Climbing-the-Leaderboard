#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the climbingLeaderboard function below.
def climbingLeaderboard(scores, alice):
    scores11=list(set(scores))
    scores12=sorted(scores11)
    i=0
    ranking=[]
    n=len(scores12)
    for j in alice:
        while(n>i and j>=scores12[i]):
            i+=1
        ranking.append(n+1-i)    
    return ranking

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    scores_count = int(input())

    scores = list(map(int, input().rstrip().split()))

    alice_count = int(input())

    alice = list(map(int, input().rstrip().split()))

    result = climbingLeaderboard(scores, alice)

    fptr.write('\n'.join(map(str, result)))
    fptr.write('\n')

    fptr.close()
