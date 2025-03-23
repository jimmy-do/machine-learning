# recursion
def countdown(n):
    if n == 0:
        return
    print(f"Entering from {n}...")
    countdown(n-1)
    print(f"Returning from {n}!")

countdown(3)