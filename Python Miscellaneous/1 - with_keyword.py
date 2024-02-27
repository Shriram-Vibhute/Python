# Creating custon context mnagers

class MyContextManager:
    def __enter__(self):
        print("Entering the context")
        # Any setup actions can be performed here
        return self

    def __exit__(self, exc_type, exc_value, traceback):
        print("Exiting the context")
        # Any teardown actions can be performed here
        # The exception details are passed to the arguments if an exception occurs

# Using the custom context manager
with MyContextManager() as cm:
    print("Inside the context")
# Exiting the context automatically after the block

