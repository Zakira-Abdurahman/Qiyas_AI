num = int(input("Enter a positive integer:"))
temp = num

# variables to store results
sum_digits = 0
product_digits = 1
reverse_num = 0
largest_digit = 0
smallest_digit = 9
even_count = 0
odd_count = 0

while temp > 0:
     digit = temp % 10
     temp = temp // 10

     sum_digits += digit
     product_digits *= digit
     reverse_num = reverse_num * 10 + digit
     if digit > largest_digit:
          largest_digit = digit
     if digit < smallest_digit:
          smallest_digit = digit
     if digit % 2 == 0:
      even_count +=1
     else:
         odd_count +=1


def factorial(n):
    if n == 0 or n ==1:
        return 1
    return n * factorial(n-1)


if num == reverse_num:
    palindrome = True
else:
    palindrome = False

print(" Number Analysis")
print("sum of digits:", sum_digits)
print("Product of digits:", product_digits)
print("Reverse:", reverse_num)
print("Largest digit:", largest_digit)
print("Smallest digit:", smallest_digit)
print("Even digits:", even_count)
print("odd digit:", odd_count)
print("Factoril:", factorial(num))
print("Palindrome:", palindrome)


     


     

