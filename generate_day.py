try:
    day = input("Day?: ")
    int(day)
except ValueError:
    quit()

with open("template.py") as template:
    with open(f"day{day}.py", 'w') as out:
        for line in template:
            out.write(line.replace('XX', day))
