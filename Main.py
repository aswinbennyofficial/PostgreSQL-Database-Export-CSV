import Participation
import Users
ch=int(input("Select the table to convert to csv:\n1.Participation table\n2.Users table\n3.both\n"))

if(ch==1):
   Participation.main()
elif(ch==2):
   Users.main()
else:
   Participation.main()   
   Users.main()
