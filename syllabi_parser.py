from pdfminer.high_level import extract_text
import re
import numpy as np

def extract_professor(text):
    my_pattern = re.compile("(?:Instructor of Record|Instructor Info|Instructors|Instructor)\D{0,2}[:]*\s(?:Dr.|Professor|[A-z]+)(?:\s|)(?:[A-z]+|)(?:\s|)(?:[A-z]+|)")
    instructor_found = my_pattern.search(text)
    if instructor_found:
        pattern_matches = my_pattern.findall(text)
        clean_pattern_matches = []
        for match in pattern_matches:
            # Remove unwanted title
            clean_match = match.replace("Instructor of Record", "").replace("Instructor Info", "").replace("Instructors", "").replace("Instructor", "").replace(":", "")
            clean_match = clean_match.strip()
            if len(clean_match) > 3:
                clean_pattern_matches.append(clean_match)
        # Return first match
        return clean_pattern_matches[0]  
    else:
       return "Not Found"

def extract_professor_email(text, instructor_surname):
    # User instructor surname to find email
    my_pattern = re.compile("((?:[a-zA-Z0-9_.+-]|)+"+instructor_surname+"+(?:[a-zA-Z0-9_.+-]|)+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+)")
    email_found = my_pattern.search(text)
    if email_found:
        pattern_matches = my_pattern.findall(text)
        # Return first match
        return pattern_matches[0]
    else:
        return "Not Found"

def extract_ta(text):
    #my_pattern = re.compile("((?:Teaching Assistant|TA)(?:[a-z]+|)(?:[:]|)\D{0,2}[A-Z][a-z]+\s(:?[(][A-Z][a-z]+[)]\s|)[A-Z][a-z]+)")
    my_pattern = re.compile("((?:Teaching Assistant|TA)(?:[a-z]+|)(?:[:]|)\s[A-Z][A-z]+\s(?:[A-Z][A-z]+|))")
    ta_found = my_pattern.search(text)
    if ta_found:
        pattern_matches = my_pattern.findall(text)
        clean_pattern_matches = []
        for match in pattern_matches:
            # Remove unwanted title and whitespace
            clean_match = match.replace("Teaching Assistants","").replace("Teaching Assistant", "").replace("TAs", "").replace("TA", "").replace("Info", "").replace(":", "")
            clean_match = clean_match.strip()
            if len(clean_match) > 0:
                clean_pattern_matches.append(clean_match)
        # Search through text one more time to compile full name
        first_match = clean_pattern_matches[0]
        first_name = first_match.split()[0]
        my_pattern = re.compile("("+first_name+"\s(?:[(][A-Z][a-z]+[)]\s|)[A-Z][A-z]+)")
        ta_found = my_pattern.search(text)
        if ta_found:
            pattern_matches = my_pattern.findall(text)
            # Return first match
            return pattern_matches[0]
        else:
            return "Not Found"
    else:
        return "Not Found"

def extract_ta_email(text, ta_surname):
    # User ta surname to find email
    my_pattern = re.compile("((?:[a-zA-Z0-9_.+-]|)+"+ta_surname+"+(?:[a-zA-Z0-9_.+-]|)+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+)")
    email_found = my_pattern.search(text)
    if email_found:
        pattern_matches = my_pattern.findall(text)
        # Return first match
        return pattern_matches[0]
    else:
        return "Not Found"

def extract_time(text):
    my_pattern = re.compile("(\d{1,2}:\d{2}(?:\D{0,3}[ap]m|)\D{0,3}\d{1,2}:\d{2}(?:\D{0,3}[ap]m|))")
    time_found = my_pattern.search(text)
    if time_found:
        pattern_matches = my_pattern.findall(text)
        # Return first match
        return pattern_matches[0]
    else:
        return "Not Found"


def extract_days(text):
    my_pattern = re.compile("(?:Class Meets:|Lecture|Tuesday/|Lab Meeting Times: \D{0,20})(?:\s|)(?:\d{1,2}:\d{2}(?:\D{0,3}[ap]m|)\D{0,3}\d{1,2}:\d{2}(?:\D{0,3}[ap]m|)\s|)[A-Z][A-z]+(?:\s[&]\s[A-Z][A-z]+|)")
    days_found = my_pattern.search(text)
    if days_found:
        pattern_matches = my_pattern.findall(text)
        # Return first match
        return pattern_matches[0]
    else:
        return "Not Found"

def extract_classrooom(text):
    my_pattern = re.compile("((?:[(]|)(?:COB)(?:[)]|)(?:\d{1}|)(?:\D{0,1})\d{3})")
    classroom_found = my_pattern.search(text)
    if classroom_found:
        pattern_matches = my_pattern.findall(text)
        # Return first match
        return pattern_matches[0]
    else:
        return "Not Found"