#!/usr/bin/python3
"""The json.dumps() function creates a JSON string | Alta3 Research"""

# JSON is part of the Python Standard Library
import json

def main():
    """runtime code"""
    ## create a blob of data to work with
    hitchhikers = [{"name": "Zaphod Beeblebrox", "species": "Betelgeusian"},
      {"name": "Arthur Dent", "species": "Human"}]

    ## display our Python data (a list containing two dictionaries)
    print(hitchhikers)

    ## Create the JSON string
    jsonstring = json.dumps(hitchhikers)

    ## Display a single string of JSON
    print(jsonstring)

{
    "row1": ["svralpha", "svrbeta", "svrgamma", "svrdelta"],
    "row2": ["svr-avengers", "svr-justlge"],
    "row3": ["svr1", "svr2b", "svr3c", "svr4d"]
}


if __name__ == "__main__":
    main()

