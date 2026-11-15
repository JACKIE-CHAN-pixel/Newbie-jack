# Demo output guide

Run `python planner_demo.py` before editing the code:

```text
(201, 'Registered')
(400, 'Name cannot be empty')
(409, 'Already registered')
(409, 'Event is full')
```

Run `python planner_demo.py board` to see the starting event board:

```text
Spring Fair Planning (spring-fair): 1 space(s) left
Robotics Day (robotics-day): 0 space(s) left
```

The numbers in parentheses are response codes. The demo keeps its data in memory, so each run starts from the same list of attendees. During the bug hunt, changing `>=` to `>` makes the final registration succeed when the event is already full. Restore the file before the final commit.
