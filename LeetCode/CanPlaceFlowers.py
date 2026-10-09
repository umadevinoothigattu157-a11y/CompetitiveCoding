class Solution:
    def canPlaceFlowers(self, flowerbed: list[int], n: int) -> bool:
        flowersPlotted = flowerbed.count(1)
        length = len(flowerbed)
        prev = 0
        current =flowerbed[0]
        after =flowerbed[1] if length > 1 else 0
        for i in range(length):
            current = flowerbed[i]
            if current == 0:
                if prev == 0 and after == 0:
                    flowerbed[i] = 1
                    current = 1
            prev = current 
            current = after
            if i+2<length:
                after = flowerbed[i+2]
            else:
                after = 0
        isPlaced = flowerbed.count(1) - flowersPlotted
        if isPlaced >= n:
            return True
        else:
            return False
