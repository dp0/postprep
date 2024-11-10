#!/usr/bin/env python3

import sys
import mimetypes
import argparse

def classify(filename):
    # Return the mimetype based on the filename
    return mimetypes.guess_type(filename)[0]

def main():
    # Prepare command-line arguments for parsing later
    parser = argparse.ArgumentParser(
        description="Script to prepare photos and videos for sharing online."
    )
    # The last arguments are the files to process
    parser.add_argument("files", nargs="+", help="Photo/video files to process")

    return 0

if __name__ == "__main__":
    sys.exit(main())