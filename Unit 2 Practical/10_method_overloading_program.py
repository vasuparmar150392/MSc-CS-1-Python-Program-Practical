print("Name: Vasu Parmar")
print("Enrollment: 92600565007")
print("-" * 50)
print("Practical 20: Demonstrate Method Overloading (Adding 2 and 3 numbers)")
print("-" * 50)


class Addition:
    """Class to demonstrate method overloading using default arguments."""

    # Method Overloading using default argument (c=None)
    def add(self, a, b, c=None):
        if c is not None:
            result = a + b + c
            print(f"   Adding 3 numbers ({a} + {b} + {c}) = {result}")
            return result
        else:
            result = a + b
            print(f"   Adding 2 numbers ({a} + {b}) = {result}")
            return result


class AdvancedAddition:
    """Class to demonstrate method overloading using variable-length arguments (*args)."""

    def add(self, *args):
        if len(args) == 2:
            result = args[0] + args[1]
            print(f"   Sum of 2 numbers {args}: {result}")
            return result
        elif len(args) == 3:
            result = args[0] + args[1] + args[2]
            print(f"   Sum of 3 numbers {args}: {result}")
            return result
        else:
            result = sum(args)
            print(f"   Sum of {len(args)} numbers {args}: {result}")
            return result


# Demonstration using Method 1 (Default Arguments):
print("Method 1: Overloading using Default Arguments:")
calc1 = Addition()
calc1.add(10, 20)          # Calling with 2 arguments
calc1.add(10, 20, 30)      # Calling with 3 arguments

# Demonstration using Method 2 (Variable-length Arguments):
print("\nMethod 2: Overloading using *args:")
calc2 = AdvancedAddition()
calc2.add(25, 75)          # Calling with 2 arguments
calc2.add(15, 30, 45)      # Calling with 3 arguments
calc2.add(5, 10, 15, 20)   # Calling with 4 arguments
