''' This is how you work out whether if a particular year is a leap year.
- on every year that is divisible by 4 with no remainder
- except every year that is evenly divisible by 100 with no remainder
- unless the year is also divisible by 400 with no remainder   \
Udemy coding exercises do not have a console, so you cannot use the input() function. You will need to call your function with hard-coded values like so:
def is_leap_year(year):
  # your code here
  # Call your function with hard coded values
  is_leap_year(2024)
'''

def is_leap_year(year):  # modulo, because we care about the remainder
  return (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0)

is_leap_year(2400)
