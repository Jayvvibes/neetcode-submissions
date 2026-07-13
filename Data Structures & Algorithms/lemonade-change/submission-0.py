class Solution:
    def lemonadeChange(self, bills: List[int]) -> bool:
        fives = 0
        tens = 0
        twenties = 0
        for i in bills:
            if i == 5:
                fives += 1
            elif i == 10:
                if fives:
                    fives -= 1
                else:
                    return False
                tens += 1
            else:
                if tens and fives:
                    tens -= 1
                    fives -= 1
                elif fives >= 3:
                    fives -= 3
                else:
                    return False
                twenties += 1
        return True