def generate_primes(limit):
    """使用埃拉托斯特尼筛法生成质数"""
    sieve = [True] * (limit + 1)
    sieve[0:2] = [False, False]
    
    for current in range(2, int(limit ** 0.5) + 1):
        if sieve[current]:
            for multiple in range(current*current, limit + 1, current):
                sieve[multiple] = False
                
    return [num for num, is_prime in enumerate(sieve) if is_prime]

if __name__ == "__main__":
    primes = generate_primes(1000)
    print("1000以内的质数：")
    for i, prime in enumerate(primes):
        print(f"{prime:4}", end=" ")
        if (i + 1) % 5 == 0:
            print()
