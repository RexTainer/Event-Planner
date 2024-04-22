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
