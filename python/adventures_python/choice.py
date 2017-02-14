print "a: Cake \nb: Carrot\nc: Fish\nd:Soup \n"
choice = raw_input("Select an option in (a,b,c,d):")

if choice == "a":
	print "Here is your cake.Yum!"
elif choice == "b":
	print "Carrots are orange. Have fun"
elif choice == "c":
	print "Fish living in water"
elif choice == "d":
	print "Today's soup is tomato,Spoons are located behind you!"
else:
	print choice + "is not a valid option,have some sir"