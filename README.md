# Event Planner
A (Very) Simple CLI Event Planner written in Python

## Installation

Installation is very simple you just have to download `event-planner.py` and have Python 3.x installed.

## Usage

```bash
python3 event-planner.py
```
**NOTE:** `event-planner.py` creates a file called `.dates` where it stores dates set by the user, make sure there is no other file named `.dates` in the directory where `event-planner.py` is located.

When run the program will return a prompt that looks like this,

```
Event Planner v[VERSION NUMBER]

What do you want to do? (Enter 'help' for a list of commands)
```

From here you can enter seven (7) different commands:
  - `help` - Returns List of Commands
  - `exit` - Exits Program
  - `view` - Shows all Existing Events
  - `add` - Adds an Event
  - `edit` - Edits an Existing Event
  - `remove` - Removes an Existing Event
  - `delete all` - Removes all Existing Events

**NOTE:** After Performing any Action or Getting an Error, `event-planner.py` recursively calls the `main()` function so the program effectively restarts and asks for a command once more. For example, if using the `view` command,

```
Event Planner v[VERSION NUMBER]

What do you want to do? (Enter 'help' for a list of commands)
view
Events:
    [LIST OF EVENTS HERE]



Event Planner v[VERSION NUMBER]

What do you want to do? (Enter 'help' for a list of commands)
```

As you can see the program starts over from the beginning, the guide for the commands implies knowlege of this behaivor.

### Using the `help` command

Using `help` is very simple, all you have to do is type `help` and press <kbd>enter</kbd> and then you will be presented with the complete list of commands like so,

```
Event Planner v[VERSION NUMBER]

What do you want to do? (Enter 'help' for a list of commands)
help
    view - View all events planned
    add - Add a new event
    edit - Edit an event
    remove - Remove an event
    help - View this list of commands
    delete all - Delete all events
    exit - Exit the program
```
### Using the `exit` command

Using `exit` is equally as simple as the `help` command, just type `exit` and press <kbd>enter</kbd> and then the program will be exited in the following manner,

```
Event Planner v[VERSION NUMBER]

What do you want to do? (Enter 'help' for a list of commands)
exit
Exiting program...
```

### Using the `view` command

Using `view` requires you to type `view` and pressing <kbd>enter</kbd> and then you will be presented with a list of your existing events in an ordered list in the following manner,

```
Event Planner v[VERSION NUMBER]

What do you want to do? (Enter 'help' for a list of commands)
view
Events:
    1. [EVENT #1]
    2. [EVENT #2]
    3. [EVENT #3]
    .......
    N. [EVENT #N]
```
### Using the `add` command

Using `add` requires you to multiple steps, firstly type `add` and press <kbd>enter</kbd>, then you will be met with the following question from the program,

```
Event Planner v[VERSION NUMBER]

What do you want to do? (Enter 'help' for a list of commands)
add 
What is the name of the event? (Max 128 characters)
[NAME]
```

Then you enter the name of the event you want to add, the name is limited to 128 characters (bytes), if this limit is exceeded it will be truncated and only the first 128 characters will be used. After that you will be propmpted to add a date to your event which will appear in the following manner,

```
Event Planner v[VERSION NUMBER]

What do you want to do? (Enter 'help' for a list of commands)
add 
What is the name of the event? (Max 128 characters)
[NAME]
What is the date of the event? (MM-DD-YYYY HH:MM:SS AM/PM)
[DATE]
```
The date of the event you provide _MUST_ be in the `MM-DD-YYYY HH:MM:SS AM/PM` format, otherwise the program will throw an error. After entering this the program will indicated that the event has been added successfully,
```
Event Planner v[VERSION NUMBER]

What do you want to do? (Enter 'help' for a list of commands)
add 
What is the name of the event? (Max 128 characters)
[NAME]
What is the date of the event? (MM-DD-YYYY HH:MM:SS AM/PM)
[DATE]
Event added!
```

### Using the `edit` command
Using the `edit` command also requires multiple steps, firstly you must type `edit` and then press <kbd>enter</kbd>, then the program will reply with the following,
```

```
