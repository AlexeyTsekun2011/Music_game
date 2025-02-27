# class Story:
#     stories = []
#
#     def __init__(self, name, events, duration):
#         self.name = name
#         self.events = events
#         self.duration = duration
#         Story.stories.append(self)

def get_coords(screen_notes):
    for note in screen_notes:
        print(note.rect.x, note.rect.y)
