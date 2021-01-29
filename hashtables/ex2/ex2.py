#  Hint:  You may not need all of these.  Remove the unused functions.
class Ticket:
    def __init__(self, source, destination):
        self.source = source
        self.destination = destination

def reconstruct_trip(tickets, length):
    cache = {}
    route = []
#cache and route are both empty
    for ticket in tickets:
        cache[ticket.source] = ticket.destination
    #going though the and making the source = destination pointing to it
    destination = cache["NONE"] 
    #set to none  
    while destination != "NONE":
        route.append(destination)
        destination = cache[destination]
    route.append("NONE")
    #this is where you add it in
    return route