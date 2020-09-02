# O(n^2) time and O(n) space
# n is length of array
def minRewards(scores):
    rewards = [1 for score in scores]
    for i in range(1,len(scores)):
        if scores[i] > scores[i-1]:
            rewards[i] = rewards[i-1] + 1
            continue
        j = i
        while j > 0 and scores[j] < scores[j-1]:
            rewards[j-1] = max(rewards[j-1],rewards[j]+1)
            j -= 1
    return sum(rewards)

# -----------------------------------------------------------------------

# O(n) time and O(n) space
# n is length of array
def minRewards(scores):
    if len(scores) == 1:
        return 1
    rewards = [0 for score in scores]
    local_mins = []
    for i in range(len(scores)):
        if isLocalMin(i,scores):
            rewards[i] = 1
            local_mins.append(i)
    for local_min in local_mins:
        traverseLeft(local_min,scores,rewards)
        traverseRight(local_min,scores,rewards)
    return sum(rewards)

def isLocalMin(i,scores):
    if i == 0:
        return scores[i] < scores[i+1]
    elif i == len(scores) - 1:
        return scores[i] < scores[i-1]
    return scores[i] < scores[i-1] and scores[i] < scores[i+1]

def traverseLeft(idx,scores,rewards):
    i = idx - 1
    while i >= 0 and scores[i] > scores[i+1]:
        rewards[i] = max(rewards[i],rewards[i+1]+1)
        i -= 1

def traverseRight(idx,scores,rewards):
    i = idx + 1
    while i < len(rewards) and scores[i] > scores[i-1]:
        rewards[i] = rewards[i-1] + 1
        i += 1
# -----------------------------------------------------------------------

# O(n) time and O(n) space
# n is length of array
def minRewards(scores):
    rewards = [1 for score in scores]
    for i in range(1,len(scores)):
        if scores[i] > scores[i-1]:
            rewards[i] = rewards[i-1] + 1
    for i in reversed(range(len(scores)-1)):
        if scores[i] > scores[i+1]:
            rewards[i] = max(rewards[i],rewards[i+1]+1)
    return sum(rewards)

print(minRewards([8,4,2,1,3,6,7,9,5]))