from django.http import JsonResponse

def count_primes_view(request):
    n = int(request.GET.get('n', 0))  # Get 'n' from query parameters
    if n < 0:
        return JsonResponse({'error': 'Input must be a non-negative integer.'}, status=400)

    def count_primes(n):
        if n <= 2:
            return 0
        is_prime = [True] * n
        is_prime[0] = is_prime[1] = False
        for i in range(2, int(n**0.5) + 1):
            if is_prime[i]:
                for j in range(i * i, n, i):
                    is_prime[j] = False
        return sum(is_prime)

    result = count_primes(n)
    return JsonResponse({'n': n, 'prime_count': result})
                