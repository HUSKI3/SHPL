from sys import *
#import file making libraries
#import main files for the data managment
#installing main language prefixes and language compiler starter
print("Can Opener 1.0.3")
print("by Retr0")
print("choose options")
print("________________")
print("1 - open a can")
print("2 - can files")
print("________________")
main_option = input("choose your option")
main_option = int(main_option)
if main_option == 1:
    name = input("file name (.can): ")
    file = open("newcan.can","r")
    print (file.readline())
    input("press any key to exit...")
elif main_option == 2:
    print("upload your file to www.filedropper.com")
    print("then enter your link here")
    link = input("link: ")
    file = open("newcan.can","w")

    file.write("<licenced.can.opener.1.0.3> <1.0.3>")
    file.write(link)
    file.close()
    input("press any key to exit...")
