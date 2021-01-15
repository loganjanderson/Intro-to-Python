def greeting(*args):
    print('Hi ' + ' '.join(args))
    print(args)


greeting('Logan', 'Anderson')