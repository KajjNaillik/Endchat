from flask import Flask

def get_entry():
    txt = input("Please type your message : ")
    return txt

def print_entry(text):
    print(text)

def main():
    print_entry(get_entry())

main()