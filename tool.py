from PIL import Image
import pathlib
import argparse

def main():
    arg_parser = argparse.ArgumentParser()
    arg_parser.add_argument("-r", "--root", default="./")
    arg_parser.add_argument("-n", "--name", default="cover.jpeg")
    args = arg_parser.parse_args()

    paths = pathlib.Path(args.root).rglob(args.name)

    for image_path in paths:
        with Image.open(image_path) as image_in:
            image_resized = image_in.resize((200,200), resample=Image.LANCZOS)
            image_resized.save(image_path)

if __name__ == "__main__":
    main()
