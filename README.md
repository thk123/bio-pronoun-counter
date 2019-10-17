# bio-pronoun-counter
Given a list of Twitter handles, counts the number that have their pronouns in their bio.

# Usage

## Dependencies

The dependencies can be installed with. The main dependency is bear/python-twitter

```
pip install -r requirements.txt
```

## Setup

To use this, you first need to configure certain environment variables to use the twitter API.

You will need to create an app and obtain the keys, as described in this [walkthrough](https://python-twitter.readthedocs.io/en/latest/getting_started.html)

Once you have, set the the following environment variables with appropriate values:

```
CONSUMER_API_KEY
CONSUMER_API_SECRET
ACCESS_TOKEN
ACCESS_SECRET
```

Then run

```
python3 bio_pronoun_counter/main.py data/MPDataOctober2019.csv
```

You can provide any CSV file, the format is the first row should contain a column called `Screen Name` and that
column should contain a list of `@handles`