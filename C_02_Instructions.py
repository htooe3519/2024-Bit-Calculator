# Generates headings (---- heading ----)
def statement_generator(statement, decoration):
    print(f"\n{decoration * 5} {statement} {decoration * 5}")


# Displays instruction
def instruction():
    statement_generator(statement= "Instructions", decoration= "-")

    print('''
Instructions go here. 
- instruction 1
- instruction 2
- etc   
    ''')


# Main routine goes here

# Display instructions if requested
want_instructions = input("Press <enter> to read the instructions "
                          "or any key to continue ")

if want_instructions == "":
    instruction()