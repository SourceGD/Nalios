def mysum(numbers):
    total = 0
    for n in numbers:
        total += n
    return total

# 2 pour le prix d'un
def mysum_recursive(numbers):
    if not numbers:
        return 0
    else:
        return numbers[0] + mysum_recursive(numbers[1:])



# Test
nums = [1.5, 2.0, 3.5, 4.0]
print(mysum(nums))  # Résultat attendu : 11.0 ( ok !)
print(mysum_recursive(nums))  # Résultat attendu : 11.0 ( ok !)

