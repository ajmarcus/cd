from typing import List

words = ["one", "two"]

def letters(words: List[str]) -> List[str]:
    results = []
    for w in words:
        for l in w:
            results.append(l)
    return results

if __name__ == "__main__":
    print(letters(words))
