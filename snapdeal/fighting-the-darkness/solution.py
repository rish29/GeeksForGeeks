no_of_testcases = int(input())

while no_of_testcases:
    no_of_candles = int(input())
    size_of_candles = input().split()
    size_of_candles = [int(size_of_candle) for size_of_candle in size_of_candles]
    print(max(size_of_candles))
    no_of_testcases -= 1
