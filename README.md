# Exceptions Activity

## Wave 1: Understanding the code.

 - Run the code, entering a few numbers and computing an average.
 - Read the code, discussing with your group how it works.
   In particular, what is the try/except doing?
 - Predict what will happen if you run the code and try to compute an average before entering any numbers.
   Then, try actually running it. What happens? Does it match what you expected? 

## Wave 2: Raising a better exception.

- Modify the average function. Make it so that it does NOT raise a ZeroDivisionError. Instead, have it raise a ValueError.
  The description of the error should be 'cannot compute average of an empty collection'.
- Run the code again, attempting to compute an average before entering any numbers. Verify that your new exception shows up.

## Wave 3: Catching an exception.

- Modify the calculator function, adding a new try/catch to catch your new exception.
  Make it so that the code does not crash if the user attempts to calculate an average before entering numbers.
  Instead, it should show the message 'You must enter at least one number before calculating an average'.
  It should then continue to prompt the user for more input.