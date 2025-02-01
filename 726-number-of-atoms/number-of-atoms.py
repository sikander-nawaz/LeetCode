class Solution:
    def countOfAtoms(self, formula: str) -> str:
        def merge_counts(target, source, multiplier=1):
            for elem, count in source.items():
                target[elem] += count * multiplier

        stack = [collections.defaultdict(int)]
        i = 0
        n = len(formula)

        while i < n:
            if formula[i] == '(':
                stack.append(collections.defaultdict(int))
                i += 1
            elif formula[i] == ')':
                top = stack.pop()
                i += 1
                start = i
                while i < n and formula[i].isdigit():
                    i += 1
                multiplier = int(formula[start:i] or 1)
                merge_counts(stack[-1], top, multiplier)
            else:
                start = i
                i += 1
                while i < n and formula[i].islower():
                    i += 1
                element = formula[start:i]
                start = i
                while i < n and formula[i].isdigit():
                    i += 1
                count = int(formula[start:i] or 1)
                stack[-1][element] += count

        final_counts = stack.pop()

        sorted_elements = sorted(final_counts.items())
        result = []
        for elem, count in sorted_elements:
            result.append(elem)
            if count > 1:
                result.append(str(count))

        return ''.join(result)
