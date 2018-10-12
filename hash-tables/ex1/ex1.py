def reconstruct_trip(tickets):
    flights = {}
    itinerary = []
    for ticket in tickets:
        flights[ticket[0]] = ticket[1]
    current_ticket = flights[None]
    while current_ticket != None:
        itinerary.append(current_ticket)
        if current_ticket not in flights:
            return []
        current_ticket = flights[current_ticket]
    return itinerary


if __name__ == '__main__':
  # You can write code here to test your implementation using the Python repl
  pass
