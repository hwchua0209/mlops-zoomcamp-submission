import argparse
import os


def main(params):
    loc = params.loc
    url = params.url

    # Get the name of the file from url
    file_name = url.rsplit("/", 1)[-1].strip()
    print(f"Downloading {file_name} ...")
    # Download file from url
    os.system(f"cd {loc} && curl {url.strip()} -o {file_name}")
    print(f"Download {file_name} completed")


if __name__ == "__main__":
    # Parsing arguments
    parser = argparse.ArgumentParser(
        description="Loading data from .paraquet file link to a local filesystem."
    )

    parser.add_argument("--loc", help="Destination for files.")
    parser.add_argument("--url", help="URL for .parquet file.")

    args = parser.parse_args()
    main(args)
