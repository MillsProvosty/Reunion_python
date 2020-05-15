# Reunion

## Setup

* Fork this Repository
* Clone YOUR fork
* Complete the activity below
* Push your solution to your fork

## Tasks

This is a small application to split expenses after a group of friends get together for a reunion. This will track how
 much each person spent on a particular activity, how much each person owed, and ultimately print out a summary of how much each person owes or is owed. 
 TDD was used to drive development. 



Additionaly, use TDD to create a Reunion class that responds to the following interaction pattern:
`

### Iteration 3: Reunion Calculations

Use TDD to update your Reunion class to respond to the following interaction pattern.

For the `breakout` method, the key is a person's name and the 
value is what they owe for the whole reunion. 
This should be the combination of what they owe from all 
activities. Again, a negative value means they are owed money. 
In the following example, `"Maria"` owes 10 from brunch and is
owed 20 from drinks, so her final amount owed in the breakout is -10.



### Iteration 4: Detailed Breakout

Use TDD to create a `detailed_breakout` method. This method should return a hash with a person's name as a key, and an array as a value. That array should contain hashes that represent what that person owes for a particular activity. Specifically, each of those hashes should have three keys:

* `:activity` - the name of the activity
* `:payees` - an array of the people who owe them for the activity if they are owed money, or an array of the people who they owe if they owe money.
* `:amount` - the amount of money to pay to/from *each* of the payees

The reunion class should respond to the following interaction pattern:

```ruby
pry(main)> reunion = Reunion.new("1406 BE")

# One person owes one person
pry(main)> activity_1 = Activity.new("Brunch")
pry(main)> activity_1.add_participant("Maria", 20)
pry(main)> activity_1.add_participant("Luther", 40)

# One person owes two people
pry(main)> activity_2 = Activity.new("Drinks")
pry(main)> activity_2.add_participant("Maria", 60)
pry(main)> activity_2.add_participant("Luther", 60)
pry(main)> activity_2.add_participant("Louis", 0)

# Two people owe one person
pry(main)> activity_3 = Activity.new("Bowling")
pry(main)> activity_3.add_participant("Maria", 0)
pry(main)> activity_3.add_participant("Luther", 0)
pry(main)> activity_3.add_participant("Louis", 30)

# Two people owe two people
pry(main)> activity_4 = Activity.new("Jet Skiing")
pry(main)> activity_4.add_participant("Maria", 0)
pry(main)> activity_4.add_participant("Luther", 0)
pry(main)> activity_4.add_participant("Louis", 40)
pry(main)> activity_4.add_participant("Nemo", 40)

pry(main)> reunion.add_activity(activity_1)
pry(main)> reunion.add_activity(activity_2)
pry(main)> reunion.add_activity(activity_3)
pry(main)> reunion.add_activity(activity_4)

pry(main)> reunion.detailed_breakout
# =>
# {
#   "Maria" => [
#     {
#       activity: "Brunch",
#       payees: ["Luther"],
#       amount: 10
#     },
#     {
#       activity: "Drinks",
#       payees: ["Louis"],
#       amount: -20
#     },
#     {
#       activity: "Bowling",
#       payees: ["Louis"],
#       amount: 10
#     },
#     {
#       activity: "Jet Skiing",
#       payees: ["Louis", "Nemo"],
#       amount: 10
#     }
#   ],
#   "Luther" => [
#     {
#       activity: "Brunch",
#       payees: ["Maria"],
#       amount: -10
#     },
#     {
#       activity: "Drinks",
#       payees: ["Louis"],
#       amount: -20
#     },
#     {
#       activity: "Bowling",
#       payees: ["Louis"],
#       amount: 10
#     },
#     {
#       activity: "Jet Skiing",
#       payees: ["Louis", "Nemo"],
#       amount: 10
#     }
#   ],
#   "Louis" => [
#     {
#       activity: "Drinks",
#       payees: ["Maria", "Luther"],
#       amount: 20
#     },
#     {
#       activity: "Bowling",
#       payees: ["Maria", "Luther"],
#       amount: -10
#     },
#     {
#       activity: "Jet Skiing",
#       payees: ["Maria", "Luther"],
#       amount: -10
#     }
#   ],
#   "Nemo" => [
#     {
#       activity: "Jet Skiing",
#       payees: ["Maria", "Luther"],
#       amount: -10
#     }
#   ]
# }
```