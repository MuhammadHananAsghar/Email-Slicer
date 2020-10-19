# Email Slicer By Muhammad Hanan Asghar
print("")
print(" [>] Email Slicer [<] ")
print("")
inp = input("Enter Email to Slice : ")
if inp == "":
  print("Enter Email Correctly!")
else:
  data = inp.split("@")
  print(" [*] Your Username is : {}".format(data[0]))
  print(" [*] Your Domain Name is : {}".format(data[1]))
print("Thanks For Using")
