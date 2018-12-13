import pymysql
from prettytable import PrettyTable

connection = pymysql.connect(
    host='localhost',
    user='root',
    password='',
    db='lakers',
)

option = 1
while option:
    print("[A] Add Player")
    print("[B] View Official Roster")
    print("[C] Edit Player Detail(s)")
    print("[D] Remove Player from Roster")
    print("[E] Exit")

    option = input('What would you like to do? : ')


    if option in "Aa":

        jersey_no = input('Enter jersey number: ')
        firstname = input('Enter first name: ')
        lastname = input('Enter last name: ')
        try:
            with connection.cursor() as cursor:
                sql = "INSERT INTO `roster` (`player_id`, `jersey_no`, `firstname`, `lastname`) VALUES (NULL, %s, %s, %s);"
                try:
                    cursor.execute(sql, (jersey_no,firstname,lastname))
                    print("Player Successfully Added!")
                except:
                    print("Error!")


                connection.commit()
        finally:
            option = 1
        
    


    elif option in "Bb":   
        try:
            with connection.cursor() as cursor:
                sql = "SELECT * FROM `roster`"
                try:
                    cursor.execute(sql)
                    result = cursor.fetchall()
                    t= PrettyTable(['Player ID', 'Jersey No.', 'First Name', 'Last Name'])
                    for col in result:
                        t.add_row([col[0], col[1], col[2], col[3] ])
                    print (t)
                except:
                 print("Error!")

                connection.commit()
        finally:
            option = 1

    elif option in "Cc":
        
        id = input('Enter Player ID you want to update: ')

        try:
             with connection.cursor() as cursor:
                update_player =  "SELECT *  FROM roster WHERE player_id = %s"
                try:
                    cursor.execute(update_player, id)
                    if cursor.rowcount > 0 :
                        print ('[1] Jersey Number')
                        print ('[2] First Name')
                        print ('[3] Last Name')

                        edit_option = input('Enter player detail to update: ')
                        if edit_option == "1":
                            new_jersey_no = input ('Enter new jersey number: ')
                            update_query = "UPDATE `roster` SET `jersey_no` = " + "'" + new_jersey_no + "'" + "  WHERE `roster`.`player_id` =" + id
                            cursor.execute(update_query)
                            print ('Player Detail Succesfully Updated!')
                        elif edit_option == "2":
                            new_firstname = input('Enter new  firstname: ')
                            update_query = "UPDATE `roster` SET `firstname` = " + "'" + new_firstname + "'" + "  WHERE `roster`.`player_id` =" + id
                            cursor.execute(update_query)
                            print ('Player Detail Succesfully Updated!')
                        elif edit_option == "3":
                            new_lastname = input('Enter new lastname: ')
                            update_query = "UPDATE `roster` SET `lastname` = " + "'" + new_lastname + "'" + "  WHERE `roster`.`player_id` =" + id
                            cursor.execute(update_query)
                            print ('Player Detail Succesfully Updated!')
                        else:
                            print ('Error!')

                        
                    else:
                        print ("Sorry but player ID '" + id + "' unregistered.")
                except:
                    print("Error!")

                connection.commit()
        finally:
            option = 1

            
    elif option in "Dd":
        id = input('Enter ID number of player to be deleted: ')
        try:
            with connection.cursor() as cursor:
                sql = "DELETE FROM `roster` WHERE `roster`.`player_id` =" + id
                try:
                    cursor.execute(sql)
                    print("Player succesfully removed from roster.")
                except:
                    print("Error!")

                connection.commit()
        finally:
            option = 1


    elif option in "Ee":
        exit()
    else:
        print ('Error!')





