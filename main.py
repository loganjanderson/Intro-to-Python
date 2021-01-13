post = ('Pyhton Basics', 'Intro guide to Python', 'Some cool content')

# post += (['tag 1', 'tag 2', 'tag 3'],)

tags = ['tag 1', 'tag 2', 'tag 3']

post += (tags,)

print(post[-1][1])