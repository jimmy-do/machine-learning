# Example: Nested Function Calls

def function_a():
    print("Starting A...")
    function_b()
    print("Ending A...")

def function_b():
    print("Starting B...")
    function_c()
    print("Ending B...")

def function_c():
    print("Starting C...")
    print("Ending C...")


function_a() # L.I.F.O 