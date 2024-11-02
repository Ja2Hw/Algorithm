import sys

#WelcomeToSMUPC
#01234567890123 -> 14칸

word = 'WelcomeToSMUPC'
n = int(sys.stdin.readline())

print(word[(n-1)%14])