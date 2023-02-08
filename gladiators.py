import psycopg2
from config import host, user, password, db_name

# connect to exist database
connection = psycopg2.connect(
    host=host,
    user=user,
    password=password,
    database=db_name
)
connection.autocommit = True

# with connection.cursor() as cursor:
#     cursor.execute(
#         "SELECT version();"
#     )
#     print(f"Server version: {cursor.fetchone()}")
# create new table
# with connection.cursor() as cursor:
#     cursor.execute(
#             """CREATE TABLE Gladiators(
#                 id serial PRIMARY KEY,
#                 nick_name varchar(50) NOT NULL,
#                 health varchar(50) NOT NULL,
#                 force varchar(50) NOT NULL,
#                 luck varchar(50) NOT NULL,
#                 bonus_level varchar(50)
#                 );
#             """
#         )
#     print("[INFO] Table created successful")

#
while True:
    print("Hello Gladiator! you can select one of these options: 1 - Create Gladiator, 2 - level Up")

    options = int(input("choose options:"))

    if options == 1:
        input_name = input("Name your gladiator:")
        health = 100
        force = 10
        luck = 10
        bonus_level = 10
        print(f"{input_name} has Health - {health}, Force - {force}, Luck - {luck}, Level bonus - {bonus_level}")

        with connection.cursor() as cursor:
            cursor.execute(
                f"""INSERT INTO Gladiators (nick_name, health, force, luck, bonus_level) VALUES
                 ('{input_name}', '{health}', '{force}', '{luck}', '{bonus_level}');"""
            )
            # connection.close()

    elif options == 2:
        attributes = str(input("You have three attribute(health, force, luck),which one you want upgrade?: "))
        spend_level = int(input("How many levels you want to spend: "))

        with connection.cursor() as cursor:
            cursor.execute(
                """SELECT health FROM Gladiators;"""
            )
            health = str((cursor.fetchone())).replace(",", "").replace("'", "").replace("(", "").replace(")", "")

        with connection.cursor() as cursor:
            cursor.execute(
                """SELECT force FROM Gladiators;"""
            )
            force = str((cursor.fetchone())).replace(",", "").replace("'", "").replace("(", "").replace(")", "")

        with connection.cursor() as cursor:
            cursor.execute(
                """SELECT luck FROM Gladiators;"""
            )
            luck = str((cursor.fetchone())).replace(",", "").replace("'", "").replace("(", "").replace(")", "")

        with connection.cursor() as cursor:
            cursor.execute(
                """SELECT bonus_level FROM Gladiators;"""
            )
            bonus_level = str((cursor.fetchone())).replace(",", "").replace("'", "").replace("(", "").replace(")", "")

        # connection.close()

        if attributes == "luck":

            average_bonus = int(bonus_level) - spend_level
            luck_level = spend_level + int(luck)
            print(f"Your gladiator has {luck_level} luck")
            with connection.cursor() as cursor:
                cursor.execute(
                    f"""UPDATE Gladiators
                    SET bonus_level = {average_bonus}, luck = {luck_level};"""
                )
            if int(bonus_level) <= 0:
                print("You need bonus level to update your gladiators!")

        elif attributes == "force":
            average_bonus = int(bonus_level) - spend_level
            force_level = spend_level + int(force)
            print(f"Your gladiator has {int(force_level)} force")
            with connection.cursor() as cursor:
                cursor.execute(
                    f"""UPDATE Gladiators
                    SET bonus_level = {average_bonus}, force = {int(force_level)};"""
                )
            if int(bonus_level) <= 0:
                print("You need bonus level to update your gladiators!")

        elif attributes == "health":
            average_bonus = int(bonus_level) - spend_level
            health_level = spend_level + int(health)
            print(f"Your gladiator has {int(health_level)} health")
            with connection.cursor() as cursor:
                cursor.execute(
                    f"""UPDATE Gladiators
                    SET bonus_level = {average_bonus}, force = {health_level};"""
                )
            if int(bonus_level) <= 0:
                print("You need bonus level to update your gladiators!")

    else:
        print("Error")
