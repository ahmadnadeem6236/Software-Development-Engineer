def misMatch(arr,target):
    count = 0
    for word in arr:
        if len(word) == len(target):
            for i, _ in enumerate(word):
                if word[i] != target[i]:
                    count += 1
            if count == 1:
                return word
            else:
                count = 0

    return "No found"


arr = ["bana", "apple", "balaba", "banzna"]
target = "banana"

res = misMatch(arr, target)
print(res)
