import calendar
import datetime
import json
import os
import re

if (not os.path.isfile(".dates") or
    not os.path.exists(".dates") or os.path.getsize(".dates") == 0):
  with open(".dates", "w") as date_file:
    date_file.write("{\n\t\"events\":[]\n}")

commands_explain = [
  "view - View all events planned",
  "add - Add a new event",
  "edit - Edit an event",
  "remove - Remove an event", 
  "help - View this list of commands",
  "delete all - Delete all events",
  "exit - Exit the program"
]

def start_action(do=None):  
  if (do is None):
    return False

  elif (do == "exit"):
    return ["exit", None]

  elif (do == "help"):
    return ["help", "\t" + "\n\t".join(commands_explain)]

  elif (do == "view"):
    with open(".dates", "r") as f:
      raw_json = f.read()
      data = json.loads(raw_json)
      return ["view", data["events"]]

  elif (do == "add"):
    return ["add", None]

  elif (do == "edit"):
    with open(".dates", "r") as f:
      raw_json = f.read()
      data = json.loads(raw_json)
      return ["edit", data["events"]]

  elif (do == "remove"):
    with open(".dates", "r") as f:
      raw_json = f.read()
      data = json.loads(raw_json)
      return ["remove", data["events"]]
  elif (do == "delete all"):
    return ["delete all", None]

  else:
    return False

def is_date_str_valid(date_string: str)->bool:
  regex = r"^([0-9]{2})-([0-9]{2})-([0-9]{4})\s(1[0-2]|(0[0-9])):[0-5][0-9]:[0-5][0-9]\s(AM|PM)$"

  long_months = [1, 3, 5, 7, 8, 10, 12]
  short_months = [4, 6, 9, 11]
  february = [2]

  regex_date = re.match(regex, date_string)

  if (regex_date is None):
    return False
  else:
    month = int(regex_date.group(1))
    day = int(regex_date.group(2))
    year = int(regex_date.group(3))

    if (1 <= month <= 12):
      if (month in long_months and 1 <= day <= 31):
        return True
      elif (month in short_months and 1 <= day <= 30):
        return True
      elif ((month in february and not calendar.isleap(year) and 1 <= day <= 28) or (month in february and calendar.isleap(year) and 1 <= day <= 29)):
        return True
      else:
        return False
    else:
      return False

def main():
  print("Event Planner v0.9.4.1\n")
  print("What do you want to do? (Enter 'help' for a list of commands)")

  command = str(input())

  response = start_action(command)

  if (response is False):
    print("Invalid command", end="\n\n\n" )
    main()
  else:

    if (response[0] == "help"):
      print(response[1], end="\n\n\n")
      main()

    elif (response[0] == "exit"):
      import sys
      print("Exiting program...")
      sys.exit()

    elif (response[0] == "view"):
      events = response[1]
      print("Events:")
      if not events: 
        print("\tThere are no events planned...", end="\n\n\n")
        main()
      else:
        for event in events:
          name = event["name"]
          date_as_str = datetime.datetime.fromtimestamp(int(event["time"])).strftime("%A, %B %d, %Y at %I:%M:%S %p")
          print(f"\t{name} - {date_as_str}")

        print("", end="\n\n\n")
        main()

    elif (response[0] == "add"):
      print("What is the name of the event? (Max 128 characters)")
      name = str(input())[0:128]
      print("What is the date of the event? (MM-DD-YYYY HH:MM:SS AM/PM)")
      date = str(input())
      if (is_date_str_valid(date)):
       epoch = int(datetime.datetime.strptime(date, "%m-%d-%Y %I:%M:%S %p").timestamp())
       with open(".dates", "r") as date_file:
         raw_json = date_file.read()
       with open(".dates", "w") as date_file2:
         data = json.loads(raw_json)
         data["events"].append({
           "name": name,
           "time": epoch
         })
         date_file2.write(json.dumps(data, indent=4))
       print("Event added!", end="\n\n\n")
       main()
      else:
       print("Invalid Date! Must be in MM-DD-YYYY HH:MM:SS AM/PM format!", end="\n\n\n")
       main()

    elif (response[0] == "edit"):
      if not response[1]: 
        print("\tThere are no events planned...", end="\n\n\n")
        main()
      i = 1
      for event in response[1]:
        name = event["name"]
        date_as_str = datetime.datetime.fromtimestamp(int(event["time"])).strftime("%A, %B %d, %Y at %I:%M:%S %p")
        print(f"\t{i}. {name} - {date_as_str}")
        i += 1
      print("Which event do you want to edit? (Enter number)")
      event_to_edit_raw = input()
      if (event_to_edit_raw.isdigit()):
        event_to_edit = int(event_to_edit_raw)
        if (event_to_edit < 1 or len(response[1]) < event_to_edit):
          print("Number Must be Included in the list above!", end="\n\n\n")
          main()
      else:
        print("Invalid answer (Must Be Digit)", end="\n\n\n")
        main()
      print("Do you want to edit the name, the date or both? (Enter 'name', 'date' or 'both')")
      acceptable_answers = ["name", "date", "both"]
      edit_type = str(input())
      if (edit_type in acceptable_answers):
        if (edit_type == "both"):
          print("What is the new name of the event? (Max 128 characters)")
          new_name = str(input())[0:128]
          print("What is the new date of the event? (MM-DD-YYYY HH:MM:SS AM/PM)")
          new_date = str(input())
          if (is_date_str_valid(new_date)):
            epoch = int(datetime.datetime.strptime(new_date, "%m-%d-%Y %I:%M:%S %p").timestamp())
            with open(".dates", "r") as date_file:
              raw_json = date_file.read()
            with open(".dates", "w") as date_file2:
              data = json.loads(raw_json)
              data["events"][event_to_edit - 1]["name"] = new_name
              data["events"][event_to_edit - 1]["time"] = epoch
              date_file2.write(json.dumps(data, indent=4))
            print("Event edited!", end="\n\n\n")
            main()
          else:
            print("Invalid Date! Must be in MM-DD-YYYY HH:MM:SS AM/PM format!", end="\n\n\n")
            main()

        elif (edit_type == "name"):
          print("What is the new name of the event? (Max 128 characters)")
          new_name = str(input())[0:128]
          with open(".dates", "r") as date_file:
            raw_json = date_file.read()
          with open(".dates", "w") as date_file2:
            data = json.loads(raw_json)
            data["events"][event_to_edit - 1]["name"] = new_name
            date_file2.write(json.dumps(data, indent=4))
          print("Event name edited!", end="\n\n\n")
          main()

        elif (edit_type == "date"):
          print("What is the new date of the event? (MM-DD-YYYY HH:MM:SS AM/PM)")
          new_date = str(input())
          if (is_date_str_valid(new_date)):
            epoch = int(datetime.datetime.strptime(new_date, "%m-%d-%Y %I:%M:%S %p").timestamp())

            with open(".dates", "r") as date_file:
              raw_json = date_file.read()
            with open(".dates", "w") as date_file2:
              data = json.loads(raw_json)
              data["events"][event_to_edit - 1]["time"] = epoch
              date_file2.write(json.dumps(data, indent=4))
            print("Event date edited!", end="\n\n\n")
            main()
          else:
            print("Invalid Date! Must be in MM-DD-YYYY HH:MM:SS AM/PM format!", end="\n\n\n")
            main()
      else:
        print("Invalid answer", end="\n\n\n")
        main()

    elif (response[0] == "remove"):
      if not response[1]: 
        print("\tThere are no events planned...", end="\n\n\n")
        main()
      i = 1
      for event in response[1]:
        name = event["name"]
        date_as_str = datetime.datetime.fromtimestamp(int(event["time"])).strftime("%A, %B %d, %Y at %I:%M:%S %p")
        print(f"\t{i}. {name} - {date_as_str}")
        i+=1
      print("Which event do you want to remove? (Enter number)")
      event_to_remove_raw = input()
      if (event_to_remove_raw.isdigit()):
        event_to_remove = int(event_to_remove_raw)
        if (event_to_remove < 1 or event_to_remove > len(response[1])):
          print("Number Must be Included in the list above!", end="\n\n\n")
          main()
      else:
        print("Invalid answer (Must Be Digit)", end="\n\n\n")
        main()
      with open(".dates", "r") as date_file:
        raw_json = date_file.read()
      with open(".dates", "w") as date_file2:
        data = json.loads(raw_json)
        del data["events"][event_to_remove-1]
        date_file2.write(json.dumps(data, indent=4))
      print("Event removed!", end="\n\n\n")
      main()

    elif (response[0] == "delete all"):
      print("A warning will be displayed before deleting all events. Are you sure you want to delete all events? (Enter 'yes' or 'no')")
      answer = str(input())
      if (answer == "yes"):
        with open(".dates", "w") as date_file:
          date_file.write("{\n\t\"events\":[]\n}")
        print("All events deleted!", end="\n\n\n")
        main()
      elif (answer == "no"):
        print("'delete all' canceled!", end="\n\n\n")
        main()
      else:
        print("Invalid answer", end="\n\n\n")
        main()
main()