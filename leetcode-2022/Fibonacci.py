def fib( n: int) -> int:
	if n < 2:
            return n
        
        first = 0
        second = 1
        
        for i in range(2,n+1):
            third = first + second
            first = second
            second = third
            
        return second
