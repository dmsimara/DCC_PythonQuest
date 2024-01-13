
with open ('story.txt', 'r') as file:
    story = file.readlines()

    lines = len(story)
    print("\nThe number of lines in story.txt is %d." % (lines))