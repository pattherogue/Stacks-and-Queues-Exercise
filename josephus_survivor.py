from queue import Queue

def find_survivor(num_people, skip):
    people = Queue()
    for i in range(1, num_people + 1):
        people.enqueue(i)

    while people.size > 1:
        for _ in range(skip - 1):
            people.enqueue(people.dequeue())
        people.dequeue()

    return people.peek()
