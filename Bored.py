  1 import requests
  2 
  3 def get_random_activity():
  4     """
  5     Fetch a random activity from the Bored API.
  6     """
  7     url = "https://www.boredapi.com/api/activity/"
  8     try:
  9         response = requests.get(url)
 10         response.raise_for_status()  # Check for any error in the response
 11         data = response.json()
 12         return data
 13     except requests.exceptions.RequestException as e:
 14         print(f"Error occurred: {e}")
 15         return None
 16 
 17 if __name__ == "__main__":
 18     print("Welcome! This script suggests random activities to do when you're bored.")
 19 
 20     while True:
 21         input("Press Enter when you're bored, or type 'exit' to quit: ")
 22         num_participants = input("How many participants are there? (Enter a number or 'exit'): ")
 23 
 24         if num_participants.lower() == 'exit':
 25             print("\nHave a good day! Hope you find something fun to do. :)\n")
 26             break
 27 
 28         if not num_participants.isdigit():
 29             print("Invalid input. Please enter a number or 'exit'.\n")
 30             continue
 31 
 32         activity_data = get_random_activity()
 33         if activity_data:
 34             activity = activity_data['activity']
 35             cost = activity_data['price']
 36             print(f"\nFeeling bored? How about: {activity}")
 37             print(f"This activity is suitable for {num_participants} participant(s).")
 38             print(f"The estimated cost of this activity is ${cost:.2f}.\n")
 39         else:
 40             print("Sorry, couldn't fetch an activity. Please try again later.\n")
 41 
 42         # Ask user if they want to retry for another activity
 43         retry = input("Do you want to retry for another activity? (yes/no): ")
 44         if retry.lower() == 'no':
 45             print("\nHave a good day! Hope you find something fun to do :).\n")
 46             break
 47 
~                                                                                                                                 
~                                            
