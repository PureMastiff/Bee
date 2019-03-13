import time
from fnmatch import fnmatch
from os import stat, walk
from os.path import abspath, exists, join


class Directory():
    def check(self, dir):
        if not exists(dir):
            raise Exception('DirectoryCheck: missing "directory" in config')
        directory = dir
        abs_directory = abspath(directory)
        print(abs_directory)
        name = directory
        pattern = '*'
        recursive = True
        directory_bytes = 0
        directory_files = 0
        for root, dirs, files in walk(directory):
            for filename in files:
                filename = join(root, filename)
                #print filename
                if not fnmatch(filename, pattern):
                    continue
                try:
                    file_stat = stat(filename)
                except OSError, ose:
                    self.warning("DirectoryCheck: could not stat file %s - %s" % (filename, ose))
                else:
                    directory_files += 1
                    directory_bytes += file_stat.st_size


        print directory_files
        print  '{}Kb'.format(directory_bytes/1024)


if __name__ == '__main__':
    d = Directory()
    d.check('/Users/guogx/git/Bee/bee')

