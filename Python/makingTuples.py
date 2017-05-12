my_dict = {
  "Speros": "(555) 555-5555",
  "Michael": "(999) 999-9999",
  "Jay": "(777) 777-7777"
}
new_list = []
def phoneNumbers(my_dict):
    for key,data in my_dict.iteritems():
        x = zip(my_dict.keys(), my_dict.values())
        print x
        break

phoneNumbers(my_dict)

 #OR

def phoneNumbers(input):
     print input.items()
print phoneNumbers(my_dict)