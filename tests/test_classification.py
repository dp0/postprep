# These tests run through different filenames and ensure they are classified
# correctly

import unittest
from postprep import classify

class TestClassification(unittest.TestCase):
    def test_pictures(self):
        assert classify("test.jpg") == "image/jpeg"
        assert classify("test.jpeg") == "image/jpeg"
        assert classify("file.JPG") == "image/jpeg"
        assert classify("file.JPEG") == "image/jpeg"
        assert classify("x.JpEg") == "image/jpeg"
        assert classify("x.JpG") == "image/jpeg"

    def test_videos(self):
        assert classify("test.mp4") == "video/mp4"
        assert classify("file.MP4") == "video/mp4"
        assert classify("x.Mp4") == "video/mp4"