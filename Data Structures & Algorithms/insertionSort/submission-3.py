class Solution:
    def insertionSort(self, pairs: List[Pair]) -> List[List[Pair]]:
        result = []

        # Process each element
        for i in range(len(pairs)):
            current = pairs[i]
            j = i - 1

            # Shift larger elements to the right
            while j >= 0 and pairs[j].key > current.key:
                pairs[j + 1] = pairs[j]
                j -= 1

            # Insert current element at correct position
            pairs[j + 1] = current

            # Save the current state
            result.append(list(pairs))

        return result