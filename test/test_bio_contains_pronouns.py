from unittest import TestCase
from bio_pronoun_counter.bio_contains_pronouns import bio_contains_pronouns
from bio_pronoun_counter.bio_contains_pronouns import ContainsBio


class TestBioContainsPronouns(TestCase):
    def test_bio_contains_pronouns(self):
        self.assertEqual(bio_contains_pronouns("he/him"), ContainsBio.YES)
        self.assertTrue(bio_contains_pronouns("she/her"), ContainsBio.YES)
        self.assertTrue(bio_contains_pronouns("they/them"), ContainsBio.YES)

    def test_case_sensitive(self):
        self.assertEqual(bio_contains_pronouns("He/him"), ContainsBio.YES)
        self.assertTrue(bio_contains_pronouns("she/Her"), ContainsBio.YES)
        self.assertTrue(bio_contains_pronouns("They/Them"), ContainsBio.YES)

    def test_surrounding_words(self):
        self.assertEqual(bio_contains_pronouns("My pronouns are he/him"), ContainsBio.YES)
        self.assertTrue(bio_contains_pronouns("My pronouns are she/her"), ContainsBio.YES)
        self.assertTrue(bio_contains_pronouns("My pronouns are they/them"), ContainsBio.YES)

    def test_punctuation(self):
        self.assertEqual(bio_contains_pronouns("My pronouns are he/him."), ContainsBio.YES)
        self.assertEqual(bio_contains_pronouns("Standard bio. He/him."), ContainsBio.YES)
        self.assertEqual(bio_contains_pronouns("Standard bio.\nHe/him."), ContainsBio.YES)
        self.assertEqual(bio_contains_pronouns("Standard bio.\nHe/him.\n"), ContainsBio.YES)
        # self.assertEqual(bio_contains_pronouns("Quirky/pronouns: he/based on the internet"), ContainsBio.YES)

    def test_negatives(self):
        self.assertEqual(bio_contains_pronouns("He who does not know history is doomed to repeat it"),
                         ContainsBio.MAYBE)
        self.assertEqual(bio_contains_pronouns("People who feel the need to put pronouns in their bio are obviously "
                                               "soy boys"),
                         ContainsBio.MAYBE)

    def test_real_examples(self):
        bio = 'Father to three boys. Husband to Hetti. MP for #Hitchin and #Harpenden. Retweets mean take a look at ' \
              'this, they don’t mean I necessarily agree! '
        self.assertEqual(ContainsBio.MAYBE, bio_contains_pronouns(bio))  # should be no
