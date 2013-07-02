import subprocess
import os

class PHPLint:
    def __init__(self):
        self.silent = False

    def setSilentLint(self, isSilent):
        self.silent = isSilent

    def lint(self, path):
        if os.path.isfile(path):
            self.lintFile(path)
        elif os.path.isdir(path):
            self.lintDir(path)

    def lintFile(self, path):
        if self.isPHPFile(path):
            process = subprocess.Popen(['php', '-l', path], shell=False, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
            (processStdOut, processStdErr) = process.communicate();
            if not self.isSilentLint():
                print processStdOut.rstrip()
            if process.returncode > 0:
                print processStdErr.rstrip()
                raise SystemExit(1)

    def lintDir(self, path):
        for rootDir, dirName, files in os.walk(path):
            for f in files:
                self.lintFile(os.path.join(rootDir, f))

    def isPHPFile(self, filename):
        return filename.endswith('.php')

    def isSilentLint(self):
        return self.silent

