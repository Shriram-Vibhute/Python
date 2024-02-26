class student:
    # Constructor
    def __init__(self):
        self._value = 10
    
    # Getter
    @property
    def get_value(self):
        # self._value = 1000 -> Even if you want to update the value in setter the it wont get happen
        return 10 * self._value

    
    # Setter
    @get_value.setter
    def get_value(self, new_val):
        self._value = new_val * 100

shri = student()
shri.get_value = 10 # -> Only setter will get executed -> and the value of object were updated
print(shri.get_value) # -> getter wii get execute -> with some hidden calculations
print(shri._value)