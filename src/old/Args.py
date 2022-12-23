

# принимаем все аргументы
def sequence_time(*args):
    total_minutes = sum(args)
    if total_minutes < 60:
        return f"Total time to launch is {total_minutes} minutes"
    else:
        return f"Total time to launch is {total_minutes/60} hours"


print(sequence_time(5, 8, 69, 468, 468, 46, 4))

# принимаем все аргументы с ключами


def crew_members(**kwargs):
    print(f"{len(kwargs)} astronauts assigned for this mission:")
    for title, name in kwargs.items():
        print(f"{title}: {name}")


print(crew_members(captain="Neil Armstrong",
      pilot="Buzz Aldrin", command_pilot="Michael Collins"))
