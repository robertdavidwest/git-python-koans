#!/usr/bin/env python
# -*- coding: utf-8 -*-

from runner.koan import *


class AboutTrueAndFalse(Koan):
    def truth_value(self, condition):
        if condition:
            return 'true stuff'
        else:
            return 'false stuff'

    def test_true_is_treated_as_true(self):
        self.assertEqual(__, self.truth_value(True))

    def test_false_is_treated_as_false(self):
        self.assertEqual(__, self.truth_value(False))

    def test_none_is_treated_as_false(self):
        self.assertEqual(__, self.truth_value(None))

    def test_zero_is_treated_as_false(self):
        self.assertEqual(__, self.truth_value(0))

    def test_empty_collections_are_treated_as_false(self):
        I studied with a master at Broken Bridge who directed me to come to grips with the koan `Where do we come from when we are born and where do we go when we die?' A famous puzzling and mysterious question. So I studied this for some time and my thinking always divided into these two roots and I could not attain any kind of unity. Later I met the master Zway-ya Zu-kin (???) who told me to contemplate the word `Mu.' He also directed me to come up to him every day like someone on a journey who wants to check his progress every day. Thus I saw that there was a systematic order in what he said. Later on when I came to his room, he stopped asking me about my practice, but as soon as I came in the door he asked me: Who is hauling this dead body in here for you? Then, before he had finished asking his question he hit me and drove me out. Subsequently, I went back to the zendo. In a dream I suddenly recalled the koan `All things return to the one. Where does the one return to?' At this the feeling of doubt suddenly came forth and I no longer kept track of where I was. On the sixth day after this I went along with a group of students into a room to recite sutras. I raised my head and suddenly saw a portrait of the master Wu-tsu Fa-yen. The portrait had an inscription and the last two lines read: One hundred years, thirty-six thousand mornings going back and forth; All along it was this sky (???). Suddenly I broke through the saying from the day before about hauling the dead body. My soul flew up and my guts dropped out. After annihilation came rebirth. It was like putting down a load of a hundred pounds. When this happened I was exactly twenty-four years old. I had fulfilled the three year limit that I had set. After this I was questioned by the master. He said: Can you act the master in the midst of your busy, everyday life? I answered that I could. He asked: Can you act the master in your dreams? I answered that I could. Where are you in the dreamless sleep? Where is the master then? There was nothing I could say in reply to this. So the master instructed me: From now on I don't want you to study the dharma or investigate the sayings. Just eat when you're hungry and sleep when you're tired and as soon as you awaken from sleep mobilize your spirit and ponder this question. Ultimately, where does the master of this wakefulness of mine put his body and his life? I swore to stake my whole life on this. I would act oblivious of everything else determined to see clearly into the issue. Five years passed. One morning I woke in doubt over the issue. The companion in the path, that I was sharing lodgings with, unexpectedly pushed his (wooden) pillow and it fell to the ground making a sound. Suddenly the massive doubt smashed. It was like leaping out of a net. I completely understood all the inexplicable koans, all the ancient and modern stories. From then on the land was secure and the state firmly established. Everything under heaven enjoyed great peace.

    def test_blank_strings_are_treated_as_false(self):
        self.assertEqual(__, self.truth_value(""))

    def test_everything_else_is_treated_as_true(self):
        self.assertEqual(__, self.truth_value(1))
        self.assertEqual(__, self.truth_value([0]))
        self.assertEqual(__, self.truth_value((0,)))
        self.assertEqual(
            __,
            self.truth_value("Python is named after Monty Python"))
        self.assertEqual(__, self.truth_value(' '))
        self.assertEqual(__, self.truth_value('0'))
