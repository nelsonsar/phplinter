import subprocess
import os

class PHPLint:
    def __init__(self):
        self.silent = False

    def set_silent_lint(self, is_silent):
        self.silent = is_silent

    def lint(self, path):
        if os.path.isfile(path):
            self.lint_file(path)
        elif os.path.isdir(path):
            self.lint_dir(path)

    def lint_file(self, path):
        if self.is_php_file(path):
            process = subprocess.Popen(['php', '-l', path], shell=False,
                                        stdout=subprocess.PIPE, stderr=subprocess.PIPE)
            (process_stdout, process_stderr) = process.communicate();
            if not self.is_silent_lint():
                print process_stdout.rstrip()
            if process.returncode > 0:
                print process_stderr.rstrip()
                raise SystemExit(1)

    def lint_dir(self, path):
        for root_dir, dir_name, files in os.walk(path):
            for f in files:
                self.lint_file(os.path.join(root_dir, f))

    def is_php_file(self, filename):
        return filename.endswith('.php')

    def is_silent_lint(self):
        return self.silent

