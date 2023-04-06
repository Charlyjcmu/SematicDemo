"""
This is the entry point of your pipeline.

This is where you import the pipeline function from its module and resolve it.
"""
# Sematic
from movie_rec.pipeline import pipeline
import argparse


if __name__ == "__main__":
    parser = argparse.ArgumentParser("Movie Recs")
    parser.add_argument("--features", type=int, required=True)

    args = parser.parse_args()

    pipeline(args.features).resolve()