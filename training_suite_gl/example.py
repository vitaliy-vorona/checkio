import os
import shutil
join = os.path.join


class SestDir:

    ROOT_DIR = 'D:\\users\\vitaliy.vorona\\TESTING'
    TEST_DIR = 'PYTHON\\TESTING'

    def make_test_dirs(self):
        if not os.path.exists(join(self.ROOT_DIR, self.TEST_DIR)):
            os.makedirs(join(self.ROOT_DIR, self.TEST_DIR))

    def clean_test_dir(self):
        if os.path.exists(join(self.ROOT_DIR, self.TEST_DIR)):
            shutil.rmtree(join(self.ROOT_DIR, self.TEST_DIR))

test_dir = SestDir()
test_dir.make_test_dirs()

# test_dir.clean_test_dir()
