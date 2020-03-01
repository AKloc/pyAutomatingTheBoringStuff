# This will pull everything from the random module.
# It's functionally equivalent to: "from random import *", but this form prevents you from having to use "random.method"
import random
import sys

for i in range(5):
    print(random.randint(1,10))

# Exits. Obviously doesn't do anything here because it's the end of the program anyhow.
sys.exit()