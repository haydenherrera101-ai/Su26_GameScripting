import sys
import time

# gives the typing effect instead of printing all at once
def stylized_print(text, delay=0.02):
    for char in text:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(delay)
    print()  # Move to the next line after printing the text
    
# if I need to add any additional helper functions in the future they'll go here 