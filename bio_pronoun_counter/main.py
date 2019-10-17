import csv
import sys
import twitter
import os

from bio_pronoun_counter.bio_contains_pronouns import bio_contains_pronouns
from bio_pronoun_counter.bio_contains_pronouns import ContainsBio


def read_handles(path):
    with open(path) as dataset:

        csv_reader = csv.reader(dataset, delimiter=',')
        handles_index = -1
        for row in csv_reader:
            if handles_index == -1:
                handles_index = row.index('Screen Name')
            else:
                handle = row[handles_index]
                yield handle


def get_handle_from_bio(api, handle):
    if not handle:
        yield None
    try:
        res = api.UsersLookup(screen_name=handle)
        if len(res) == 1:
            print(res[0].description)
            yield res[0].description

    except Exception as e:
        print(e)
        print('unknown user: ' + handle)
        yield None


def main(data_path):
    api = twitter.Api(consumer_key=os.environ['CONSUMER_API_KEY'],
                      consumer_secret=os.environ['CONSUMER_API_SECRET'],
                      access_token_key=os.environ['ACCESS_TOKEN'],
                      access_token_secret=os.environ['ACCESS_SECRET'])

    yes_count = 0
    total_count = 0
    for handle in read_handles(data_path):
        for bio in get_handle_from_bio(api, handle[1:]):
            if bio:
                total_count += 1
                result = bio_contains_pronouns(bio)
                if result == ContainsBio.YES:
                    print("The following bio contains pronouns:")
                    print(handle)
                    print(bio)
                    print('--------------------------------------')
                    yes_count += 1
                if result == ContainsBio.MAYBE:
                    print("Ambiguous bio:")
                    print(handle)
                    print(bio)
                    print('--------------------------------------')
                    # print("Does this bio contain pronouns?")
                    # print(bio)
                    # while True:
                    #     answer = input()
                    #     if answer == 'y':
                    #         yes_count += 1
                    #     elif answer == 'n':
                    #         break
                    #     else:
                    #         print('unrecognised input')

    print('Have pronouns: ' + str(yes_count))
    print('Out of: ' + str(total_count))


main(sys.argv[1])
