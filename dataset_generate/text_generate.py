"""
Venic - Voice Enabled Intelligent Programming Assistant

@author IT19180526 - S.A.N.L.D. Chandrasiri
@version 1.0
"""

import random

variable = [
    "main", "master", "size", "height", "weight",
    "bag", "can", "computer", "phone", "laptop",
    "mobilephone", "smartphone", "phonenumber", "contactnumber", "address",
    "location", "email", "contact", "emailaddress", "mouse",
    "keyboard", "screen", "touchscreen", "fruit", "food",
    "vegetable", "eatables", "price", "cost", "sum",
    "addition", "a", "b", "c", "p",
    "q", "r", "s", "x", "y",
    "z", "answer", "result", "user", "userid",
    "id", "num", "age", "department", "hospital",
    "wheel", "seat", "car", "bus", "van",
    "bike", "glass", "red", "black", "white",
    "blue", "yellow", "valid", "subtract", "value",
    "arr", "i", "val", "key", "count",
]

variable_two = [
    "main", "master", "size", "height", "weight",
    "bag", "can", "computer", "phone", "laptop",
    "smartphone", "contact", "address", "user", "userid",
    "location", "email", "contact", "mouse", "value",
    "keyboard", "screen", "touchscreen", "fruit", "food",
    "vegetable", "eatables", "price", "cost", "sum",
    "addition", "x", "y", "z", "answer",
    "id", "num", "age", "department", "hospital",
    "wheel", "seat", "car", "bus", "van",
    "bike", "glass", "red", "black", "result"
]

className = [
    "main", "master", "size", "height", "weight",
    "bag", "util", "utility", "can", "computer",
    "phone", "laptop", "repository", "api", "controller",
    "mobilephone", "smartphone", "mobile", "service", "model",
    "repo", "address", "location", "email", "contact",
    "mouse", "keyboard", "screen", "touch", "fruit",
    "food", "vegetable", "eatables", "price", "cost",
    "sum", "addition", "answer", "result", "user",
    "userid", "id", "num", "age", "department",
    "hospital", "wheel", "seat", "car", "bus",
    "van", "bike", "glass", "red", "black",
    "white", "blue", "a", "b", "c",
    "p", "q", "r", "s", "x",
    "y", "z",
]

className_two = [
    "main", "master", "size", "height", "weight",
    "bag", "util", "utility", "can", "computer",
    "phone", "laptop", "repository", "api", "controller",
    "smartphone", "mobile", "service", "model", "contact",
    "repo", "address", "location", "email", "black",
    "mouse", "keyboard", "screen", "touch", "fruit",
    "food", "vegetable", "eatables", "price", "cost",
    "sum", "addition", "answer", "result", "user",
    "id", "num", "age", "department", "van",
    "hospital", "wheel", "seat", "car", "bus",
    "bike", "glass", "red", "white", "blue",
]

arrValue = [
    "main", "master", "size", "height", "weight",
    "bag", "util", "utility", "can", "computer",
    "phone", "laptop", "repository", "api", "controller",
    "mobilephone", "smartphone", "mobile", "service", "model",
    "repo", "address", "location", "email", "contact",
    "mouse", "keyboard", "screen", "touch", "fruit",
    "food", "vegetable", "eatables", "price", "cost",
    "sum", "addition", "answer", "result", "user",
    "userid", "id", "num", "age", "department",
    "hospital", "wheel", "seat", "car", "bus",
    "van", "bike", "glass", "red", "black",
    "white", "blue", "a", "b", "c",
    "p", "q", "r", "s", "x",
    "y", "z", "one", "two", "three",
    "four", "five", "six", "seven", "eight",
    "nine", "ten", "bottle", "cup", "plate",
    "school", "university", "campus", "kamal", "amal",
    "sunil", "chandra", "house", "home", "aeroplane",
]

methodName = [
    "repository", "api", "controller", "service", "model",
    "repo", "sum", "addition", "answer", "result",
    "get", "update", "create", "delete", "find",
    "receive", "calculate", "decrement", "increment", "calc",
    "add", "valid", "move", "work", "write",
    "spec", "buy", "run", "notify", "output",
    "communicate", "call", "send", "input", "subtract",
    "multiply", "divide", "modulus", "check", "display",
    "show", "view", "max", "min", "is",
    "contain", "remove", "clear", "clean", "put",
    "set", "build", "plus", "minus", "append",
    "reset", "rebuild", "change", "select", "generate",
]

number = [
    "one", "two", "three", "four", "five",
    "six", "seven", "eight", "nine", "ten",
]

logical = [
    "less than", "less than or equal",
    "greater than", "greater than or equal",
    "equal", "not equal"
]

boolean = [
    "true", "false"
]

numberlarge = [
    "one hundred", "two hundred",
    "three hundred", "four hundred",
    "five hundred", "six hundred",
    "seven hundred", "eight hundred",
    "nine hundred", "one thousand"
]

numberlong = [
    "one thousand", "two thousand",
    "three thousand", "four thousand",
    "five thousand", "six thousand",
    "seven thousand", "eight thousand",
    "nine thousand", "one thousand"
]

numbermiddle = [
    "twenty", "thirty",
    "forty", "fifty",
    "sixty", "seventy",
    "eighty", "ninety",
]

dataType = [
    "integer", "string",
    "double", "flout",
    "boolean", "byte",
    "short", "long",
    "char",
]

element_name = [
    "main", "master", "size", "height", "weight",
    "bag", "utility", "can", "computer", "mouse",
    "phone", "laptop", "repository", "api", "controller",
    "mobile", "service", "model", "contact", "value",
    "vegetable", "eatables", "price", "cost", "sum",
    "addition", "x", "y", "z", "answer",
    "communicate", "call", "send", "input", "subtract",
    "multiply", "divide", "modulus", "check", "display",
    "wheel", "seat", "car", "bus", "van",
    "bike", "glass", "red", "black", "result"
]

element_type = [
    "project", "class", "interface", "method", "function",
    "array", "arraylist", "attribute", "constant", "hashmap",
    "hashset", "linkedlist", "procedure", "property", "variable",
    "property", "struct", "enum",
]


def generate():
    print("- intent: informremove")
    print("  examples: |")

    for x in element_type:
        for i in element_name:
            if i != x:
                print('    - delete [' + x + '](type) named [' + i + '](name)')

    print("#######################################################")
    for x in element_type:
        for i in element_name:
            if i != x:
                print('    - delete [' + x + '](type) [' + i + '](name)')

    print("#######################################################")
    for x in element_type:
        for i in element_name:
            if i != x:
                print('    - remove [' + x + '](type) named [' + i + '](name)')

    print("#######################################################")
    for x in element_type:
        for i in element_name:
            if i != x:
                print('    - remove [' + x + '](type) [' + i + '](name)')

    print("#######################################################")


'''
    voice_generation("what is the "+conv[1] + " of the " + conv[0])    
    print('    - remove [' + x + '](type) [' + i + '](name)')    
    
    - create new [project](type) named [example](name)
    - create new [project](type) [example](name)
    - Create [project](type) named [example](name)
    - Create [project](type) [example](name)
    
    - initialize new [project](type) named [example](name)
    - initialize new [project](type) [example](name)
    - initialize [project](type) [example](name)    
    
    - delete array named [count](name)
    - delete array [main](name)    
    - remove array named [count](name)
    - remove array [main](name)  
        
'''

if __name__ == '__main__':
    generate()
