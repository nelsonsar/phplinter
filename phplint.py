import subprocess
import os

class PHPLint:
    def lint(self, path):
        if os.path.isfile(path):
            self.lintFile(path)
        elif os.path.isdir(path):
            self.lintDir(path)

    def lintFile(self, path):
        if self.isPHPFile(path):
            returnCode = subprocess.call(['php', '-l', path], shell=False)
            if returnCode > 0:
                raise SystemExit(1)

    def lintDir(self, path):
        for rootDir, dirName, files in os.walk(path):
            for f in files:
                self.lintFile(os.path.join(rootDir, f))

    def isPHPFile(self, filename):
        return filename.endswith('.php')

