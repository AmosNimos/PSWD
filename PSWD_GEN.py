import random

#This function generate the password.
def generatePassword(pwlength):
	#initialise alphavet string.
	alphabet = "abcdefghijklmnopqrstuvwxyz,./;'[]+_)(*&^%$#@!~`1234567890-=ABCDEFGHIJKLMNOPQRSTUVWXYZ"
	#Initialise array list to contain multiple passwords.
	passwords = [];
	#A variable to temporarely store individual password to string.
	password = "";

	#Loop trough the amount of password required by the user.
	for j in range(pwlength):
		#Select a symbol randomply in the alphavet string.
		next_letter_index = random.randrange(len(alphabet));
		#Add the selected character to the password string
		password = password + alphabet[next_letter_index];
	return password

#main programem funtion
def main():
	#ask the user to input the amount of passwords to generate.
	numPasswords = int(input("How many passwords do you want to generate? "));

	#set a limits to the amount of passwords that can be generated.
	if numPasswords<1:
		print("Minimum amount of password is 1");
		numPasswords=1;
	if numPasswords>100:
		print("Maximum amount of password is 100");
		numPasswords=100;

	#keep the user inform of the progress
	print("Generating " +str(numPasswords)+" passwords");

	#set a defautl password length.
	passwordLengths = 5;

	#inform user of the defaut length setting.
	print("enter 0 for the default 16 character password length");

	#ask the user to input the lenght of each password
	length = int(input("Enter the length of Password "));

	#set limit to the lenght of each password
	if length==0:
    		print("Default length of password is 16");
    		length = 16;
	if length<5:
		print("Minimum length of password is 5");
		length = 5;

	if length>200:
		print("Maximum length of password is 200");
		length = 200;

	#update the password length.
	passwordLengths=length;
	#generate all password and insert them in the Password array list.
	Password=[];
	for i in range(numPasswords):
		Password.append(str(generatePassword(passwordLengths)));

 	#if the array contain multiple password loop trough the list.
	if numPasswords>1:
		for i in range(numPasswords):
			#display all password in the Password list to the user.
			print("Password n."+str(i+1)+" = " + Password[i]);
	else:
		#display the password from the Password list to the user.
		print ("Password"+" = " + Password[0]);
#start programme
main();
