Hello There.
My name is Kennedy Kimathi.
Am Currently at PLP.
I am a web developer, looking to solve problems and bring abput ideas to reality.
Let's reach out to share ideas.
Contact info: jrkennedy027@gmail.com   +254797658655


with open("input.txt", "w") as file:
    file.write("Hello There.\n")
    file.write("My name is Kennedy Kimathi. \n")
    file.write("I am a web developer, looking to solve problems and bring abput ideas to reality.
.\n")
    file.write("Let's reach out to share ideas.
\n")
    file.write("Contact info: jrkennedy027@gmail.com   +254797658655
.\n")


with open("input.txt", "r") as file:
    content = file.read()

word_count = len(content.split())

processed_content = content.upper()

with open("output.txt", "w") as file:
    file.write(processed_content)
    file.write(f"\nWORD COUNT: {word_count}\n")

print("Processing complete! The output has been saved to output.txt.")
