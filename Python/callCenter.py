class Call(object):
    def __init__(self, unique_id, caller_name, phone_number, time_of_call, reason_for_call):
        self.unique_id = unique_id
        self.caller_name = caller_name
        self.phone_number = phone_number
        self.time_of_call = time_of_call
        self.reason_for_call = reason_for_call

    def display(self):
        print "ID: " + str(self.unique_id) + " " +"Name: " + self.caller_name + " " +"Phone Number: " + str(self.phone_number) + " " +"Time: " + self.time_of_call + " " +"Reason for call: " + self.reason_for_call
        return self

class CallCenter(object):
    def __init__(self):
        self.calls = []
        self.queue_size = 0

    def add_calls(self, call):
        self.calls.append(call)
        self.queue_size += 1
        return self

    def remove_calls(self):
        self.calls.pop(0)
        self.queue_size -= 1
        return self

    def removeCallbyNum(self, num):
        for caller in range(0,len(self.calls)):
            if self.calls[caller].caller_number == num:
                self.calls.pop(caller)
                break
        self.queue_size -= 1
        return self

    def info(self):
        print "Current queue size: ", self.queue_size
        for caller in range(len(self.calls)):
            print "Queue Position:",(caller+1), "Name:", self.calls[caller].caller_name, "#:",self.calls[caller].phone_number
        return self

one = Call(1, "Anessa", "111-123-1234", "3:40pm", "Looking for pizza")
two = Call(2, "Boo", "222-222-2222", "5:50pm", "Saying hi")
three = Call(3, "Anne", "000-000-0000", "5:50pm", "Upset")
four = Call(4, "Minh", "121-121-1212", "5:50pm", "Hungry")
five = Call(5, "Bill", "333-333-3333", "5:50pm", "Booking travel plans")
six = Call(6, "Frank", "444-444-2222", "5:50pm", "Assistance")

callCenter1 = CallCenter().add_calls(one).add_calls(two).add_calls(three).add_calls(four).add_calls(five).add_calls(six).info().remove_calls()