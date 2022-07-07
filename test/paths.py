import os

def test_ProjectRootDirectory():
    root_dir = os.path.dirname(os.path.abspath('requirements.txt'))
    # TODO: Eric put the path to your project in. This is just
    # so we don't lose our minds dealing with I/O.
    assert (
        root_dir == '/home/c/dev/jenny' 
        or root_dir == 'C:\\Users\\Eric\\Documents\\Pycharm Projects\\Jenny'
    )


if __name__ == '__main__':
    test_ProjectRootDirectory()