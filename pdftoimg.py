#created by Vijay Sahu
#facebook.com/vijaysahuofficialpage
import os
from pdf2image import convert_from_path

folder_path = input("enter folder path >>> ")
file_name = input("Enter file name with extension >>> ")

final_folder_path = os.path.abspath(folder_path)
final = os.path.join(final_folder_path, file_name)

file_exists = os.path.exists(final)

if file_exists == False:
    print("File Not Found")

else:
    print("File detected")
    pages = convert_from_path(final, output_folder=final_folder_path, fmt="JPEG", dpi=200)
    print("File successfully converted")
