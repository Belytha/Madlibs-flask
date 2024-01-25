"""Madlibs Stories."""


class Story:
    """Madlibs story.

    To  make a story, pass a list of prompts, and the text
    of the template.

        >>> s = Story(["noun", "verb"],
        ...     "I love to {verb} a good {noun}.")

    To generate text from a story, pass in a dictionary-like thing
    of {prompt: answer, promp:answer):

        >>> ans = {"verb": "eat", "noun": "mango"}
        >>> s.generate(ans)
        'I love to eat a good mango.'
    """

    def __init__(self, words, text, title):
        """Create story with words and template text."""

        self.prompts = words
        self.template = text
        self.title = title

    def generate(self, answers):
        """Substitute answers into text."""

        text = self.template

        for (key, val) in answers.items():
            text = text.replace("{" + key + "}", val)

        return text


# Here's a story to get you started

story1 = Story(
    ["place", "noun", "verb", "adjective", "plural_noun"],
    """Once upon a time in a long-ago {place}, there lived a
       large {adjective} {noun}. It loved to {verb} {plural_noun}.""",
    "Once upon a time"
)
story2 = Story(
    ["adjective1", "adjective2", "type_of_bird", "room", "verb_past_tense", "verb", "relative_name", "noun", "liquid", "verb_ending_in_ing", "part_of_body_plural", "plural_noun", "verb_ending_in_ing2", "noun"],
    """It was a {adjective1}, cold November day. I woke up to the {adjective2}
      smell of {type_of_bird} roasting in the {room} downstairs. I {verb_past_tense}
        down the stairs to see if I could help {verb} the dinner. My mom said, "See if
          {relative_name} needs a fresh {noun}." So I carried a tray of glasses full of
            {liquid} into the {verb_ending_in_ing} room. When I got there, I couldn't
              believe my {part_of_body_plural}! There were {plural_noun} {verb_ending_in_ing2} on the {noun}!""",
    "Thanksgiving day"
)
story3 = Story(
    ["addjective1", "nationality", "person", "noun1", "adjective2", "noun2", "adjective3", "adjective4", "plural_noun", "noun3", "number", "shapes", "food1", "food2", "number2"],
    """Pizza was invented by a {addjective1} {nationality} 
    chef named {person}. To make a pizza, you need to take a 
    lump of {noun1}, and make a thin, round {adjective2} {noun2}. Then you 
    cover it with {adjective3} sauce, {adjective4} cheese, and fresh chopped
      {plural_noun}. Next you have to bake it in a very hot {noun3}. When it is done,
        cut it into {number} {shapes}. Some kids like {food1} pizza the best,
          but my favorite is the {food2} pizza. If I could, I would eat pizza {number2} times a day!""",
    "Pizza Pizza"
)

stories_list = [story1, story2, story3]

