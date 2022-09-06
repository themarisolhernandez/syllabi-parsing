from syllabi_parser import *
import pandas as pd
import os

# Get all file names from syllabi folder
files=os.listdir(r"syllabi/")

def main_func():
    data_records = []
    for i in range(0,len(files)):
        text = extract_text("syllabi/" + files[i])
        text = text.replace("\n", " ").replace("  ", " ")
        class_name = files[i].replace(".pdf", "")
        instructor_name = extract_professor(text)
        instructor_surname = instructor_name.split()[-1].lower()
        instructor_email = extract_professor_email(text, instructor_surname=instructor_surname)
        ta_name = extract_ta(text)
        ta_surname = ta_name.split()[-1].lower()
        ta_email = extract_ta_email(text, ta_surname=ta_surname)
        time = extract_time(text)
        day = extract_days(text)
        classroom = extract_classrooom(text)
        # Append dictionary of extracted info
        data_records.append({"Class Name":class_name, "Instructor":instructor_name, "Instructor Email":instructor_email,
                            "TA":ta_name, "TA Email":ta_email, "Time":time, "Day":day, "Classroom":classroom})
    df = pd.DataFrame.from_records(data_records,index=['0', '1', '2', '3'])
    df.to_csv("output/syllabi-features.csv", index=False)

if __name__ == "__main__":
   main_func()