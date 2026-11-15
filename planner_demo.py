import sys


events = {
    'spring-fair': {
        'title': 'Spring Fair Planning',
        'capacity': 2,
        'attendees': ['Mina'],
    },
    'robotics-day': {
        'title': 'Robotics Day',
        'capacity': 2,
        'attendees': ['Noah', 'Ari'],
    },
}


def register(event_id, name):
    # Check that the event exists before reading its details.
    if event_id not in events:
        return 404, 'Event not found'

    if not name.strip():
        return 400, 'Name cannot be empty'

    event = events[event_id]

    if name in event['attendees']:
        return 409, 'Already registered'

    if len(event['attendees']) >= event['capacity']:
        return 409, 'Event is full'

    event['attendees'].append(name)
    return 201, 'Registered'


def show_board():
    for event_id, event in events.items():
        spaces = event['capacity'] - len(event['attendees'])
        print(f"{event['title']} ({event_id}): {spaces} space(s) left")


if __name__ == '__main__':
    if len(sys.argv) > 1 and sys.argv[1] == 'board':
        show_board()
    else:
        print(register('spring-fair', 'Linh'))
        print(register('spring-fair', ''))
        print(register('spring-fair', 'Linh'))
        print(register('robotics-day', 'Kai'))
