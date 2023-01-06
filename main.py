import commonTimings

people = int(input("Enter the number of the people who will be in the meeting: "))
print("---------------------------------")
participants = {}
for i in range(people):
    freeSlots = []
    while True:
        slot = int(input(f"Enter the slot for participant-{i+1}: "))
        freeSlots.append(slot)
        again = input("Enter 1 to add one more slot or 0 to exit: ")
        print("---------------------------------")
        if again == "0":
            break
    participants[i]=freeSlots

common = commonTimings.getTimings(participants)
print("common timings:", common)
print("---------------------------------")