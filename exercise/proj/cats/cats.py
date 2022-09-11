"""Typing test implementation"""

from utils import lower, split, remove_punctuation, lines_from_file
from ucb import main, interact, trace
from datetime import datetime


###########
# Phase 1 #
###########


def choose(paragraphs, select, k):
    """Return the Kth paragraph from PARAGRAPHS for which SELECT called on the
    paragraph returns true. If there are fewer than K such paragraphs, return
    the empty string.
    """
    # BEGIN PROBLEM 1
    "*** YOUR CODE HERE ***"
    lst = []
    for each in paragraphs:
        if select(each):
            lst.append(each)
    if k > len(lst) - 1:
        return "" 
    else:
        return lst[k]
    # END PROBLEM 1


def about(topic):
    """Return a select function that returns whether a paragraph contains one
    of the words in TOPIC.

    >>> about_dogs = about(['dog', 'dogs', 'pup', 'puppy'])
    >>> choose(['Cute Dog!', 'That is a cat.', 'Nice pup!'], about_dogs, 0)
    'Cute Dog!'
    >>> choose(['Cute Dog!', 'That is a cat.', 'Nice pup.'], about_dogs, 1)
    'Nice pup.'
    """
    assert all([lower(x) == x for x in topic]), 'topics should be lowercase.'
    # BEGIN PROBLEM 2
    "*** YOUR CODE HERE ***"
    def judge(string):
        str_rev = string.lower()
        lst = remove_punctuation(str_rev).split()
        for each in topic:
            for word in lst:
                if word == each:
                    return True
        return False

    return judge
    # END PROBLEM 2


def accuracy(typed, reference):
    """Return the accuracy (percentage of words typed correctly) of TYPED
    when compared to the prefix of REFERENCE that was typed.

    >>> accuracy('Cute Dog!', 'Cute Dog.')
    50.0
    >>> accuracy('A Cute Dog!', 'Cute Dog.')
    0.0
    >>> accuracy('cute Dog.', 'Cute Dog.')
    50.0
    >>> accuracy('Cute Dog. I say!', 'Cute Dog.')
    50.0
    >>> accuracy('Cute', 'Cute Dog.')
    100.0
    >>> accuracy('', 'Cute Dog.')
    0.0
    """
    typed_words = split(typed)
    reference_words = split(reference)
    # BEGIN PROBLEM 3
    "*** YOUR CODE HERE ***"
    type_len = len(typed_words)
    refer_len = len(reference_words)
    if type_len == 0 or refer_len == 0:
        return 0.0

    wrong_len = 0
    for i in range(refer_len):
        if i >= type_len:
            break
        if typed_words[i] != reference_words[i]:
            wrong_len += 1
    
    if type_len > refer_len:
        wrong_len += type_len - refer_len

    return (1 - wrong_len / type_len) * 100

    # END PROBLEM 3


def wpm(typed, elapsed):
    """Return the words-per-minute (WPM) of the TYPED string."""
    assert elapsed > 0, 'Elapsed time must be positive'
    # BEGIN PROBLEM 4
    "*** YOUR CODE HERE ***"
    type_len = len(typed)/5
    return type_len * (60 / elapsed)
    # END PROBLEM 4


def autocorrect(user_word, valid_words, diff_function, limit):
    """Returns the element of VALID_WORDS that has the smallest difference
    from USER_WORD. Instead returns USER_WORD if that difference is greater
    than LIMIT.
    """
    # BEGIN PROBLEM 5
    "*** YOUR CODE HERE ***"
    if len(valid_words) == 0:
        return user_word
    if user_word in valid_words:
        return user_word
    min_dif = diff_function(user_word, valid_words[0], limit)
    min_index = 0
    for i in range(len(valid_words)):
        tmp_dif = diff_function(user_word, valid_words[i], limit)
        if tmp_dif < min_dif:
            min_index = i
            min_dif = tmp_dif
    
    if min_dif <= limit:
        return valid_words[min_index]
    else:
        return user_word
    # END PROBLEM 5


def shifty_shifts(start, goal, limit):
    """A diff function for autocorrect that determines how many letters
    in START need to be substituted to create GOAL, then adds the difference in
    their lengths.
    """
    # BEGIN PROBLEM 6
    def shift_helper(start, goal, limit, correct_len, i):
        if correct_len > limit:
            return limit + 1
        elif i >= len(start) or i >= len(goal):
            return correct_len
        else:
            if start[i] != goal[i]:
                return shift_helper(start, goal, limit, correct_len+1, i+1)
            else:
                return shift_helper(start, goal, limit, correct_len, i+1)

    correct_len = shift_helper(start, goal, limit, 0, 0)

    if len(goal) > len(start):
        correct_len += len(goal) - len(start)
    elif len(start) > len(goal):
        correct_len += len(start) - len(goal)

    return correct_len
        
    # END PROBLEM 6


def pawssible_patches(start, goal, limit):
    """A diff function that computes the edit distance from START to GOAL."""

    if limit < 0: # 突破界限直接返回超级大 
        return 1000
    
    elif start == goal: # 如果一致直接结束迭代
        # BEGIN
        "*** YOUR CODE HERE ***"
        return 0
        # END
    
    elif start == "" or goal == "": # 某个替换完了说明剩下都要oper
        # BEGIN
        "*** YOUR CODE HERE ***"
        max_len = max(len(start), len(goal))
        return max_len + pawssible_patches("", "", limit - max_len)
        # END
   
    elif start[0] == goal[0]: # 如果相同就不用做oper
        return pawssible_patches(start[1:], goal[1:], limit)
    
    else: # 三种情况都是对第一个进行操作
        add_diff = 1 + pawssible_patches(start, goal[1:], limit - 1)
        remove_diff = 1 + pawssible_patches(start[1:], goal, limit - 1)
        substitute_diff = 1 + pawssible_patches(start[1:], goal[1:], limit - 1)
        # BEGIN
        "*** YOUR CODE HERE ***"
        return min(add_diff, remove_diff, substitute_diff) # 每次迭代返回使用三种oper后的最小情况
        # END


def final_diff(start, goal, limit):
    """A diff function. If you implement this function, it will be used."""
    assert False, 'Remove this line to use your final_diff function'


###########
# Phase 3 #
###########


def report_progress(typed, prompt, user_id, send):
    """Send a report of your id and progress so far to the multiplayer server."""
    # BEGIN PROBLEM 8
    "*** YOUR CODE HERE ***"
    num = 0
    for i in range(len(typed)):
        if typed[i] != prompt[i]:
            break
        num += 1

    send({'id': user_id, 'progress': num/len(prompt)})

    return num/len(prompt)

    # END PROBLEM 8


def fastest_words_report(times_per_player, words):
    """Return a text description of the fastest words typed by each player."""
    game = time_per_word(times_per_player, words)
    fastest = fastest_words(game)
    report = ''
    for i in range(len(fastest)):
        words = ','.join(fastest[i])
        report += 'Player {} typed these fastest: {}\n'.format(i + 1, words)
    return report


def time_per_word(times_per_player, words):
    """Given timing data, return a game data abstraction, which contains a list
    of words and the amount of time each player took to type each word.

    Arguments:
        times_per_player: A list of lists of timestamps including the time
                          the player started typing, followed by the time
                          the player finished typing each word.
        words: a list of words, in the order they are typed.
    """
    # BEGIN PROBLEM 9
    "*** YOUR CODE HERE ***"
    time_list = []
    for i in range(len(times_per_player)):
        time_list.append([])
        for j in range(1, len(times_per_player[i])):
            time_list[i].append(times_per_player[i][j] - times_per_player[i][j-1])

    return game(words, time_list)

    # END PROBLEM 9


def fastest_words(game):
    """Return a list of lists of which words each player typed fastest.

    Arguments:
        game: a game data abstraction as returned by time_per_word.
    Returns:
        a list of lists containing which words each player typed fastest
    """
    player_indices = range(len(all_times(game)))  # contains an *index* for each player
    word_indices = range(len(all_words(game)))    # contains an *index* for each word
    # BEGIN PROBLEM 10
    "*** YOUR CODE HERE ***"
    word_list = all_words(game)
    time_list = all_times(game)
    fastest_list = []
    for _ in range(len(time_list)):
        fastest_list.append([])

    for i in range(len(word_list)):
        min_time = time_list[0][i]
        index = 0
        for j in range(len(time_list)):
            if min_time > time_list[j][i]:
                min_time = time_list[j][i]
                index = j
        fastest_list[index].append(word_list[i])

    return fastest_list
    # END PROBLEM 10


def game(words, times):
    """A data abstraction containing all words typed and their times."""
    assert all([type(w) == str for w in words]), 'words should be a list of strings'
    assert all([type(t) == list for t in times]), 'times should be a list of lists'
    assert all([isinstance(i, (int, float)) for t in times for i in t]), 'times lists should contain numbers'
    assert all([len(t) == len(words) for t in times]), 'There should be one word per time.'
    return [words, times]


def word_at(game, word_index):
    """A selector function that gets the word with index word_index"""
    assert 0 <= word_index < len(game[0]), "word_index out of range of words"
    return game[0][word_index]


def all_words(game):
    """A selector function for all the words in the game"""
    return game[0]


def all_times(game):
    """A selector function for all typing times for all players"""
    return game[1]


def time(game, player_num, word_index):
    """A selector function for the time it took player_num to type the word at word_index"""
    assert word_index < len(game[0]), "word_index out of range of words"
    assert player_num < len(game[1]), "player_num out of range of players"
    return game[1][player_num][word_index]


def game_string(game):
    """A helper function that takes in a game object and returns a string representation of it"""
    return "game(%s, %s)" % (game[0], game[1])

enable_multiplayer = False  # Change to True when you're ready to race.

##########################
# Command Line Interface #
##########################


def run_typing_test(topics):
    """Measure typing speed and accuracy on the command line."""
    paragraphs = lines_from_file('data/sample_paragraphs.txt')
    select = lambda p: True
    if topics:
        select = about(topics)
    i = 0
    while True:
        reference = choose(paragraphs, select, i)
        if not reference:
            print('No more paragraphs about', topics, 'are available.')
            return
        print('Type the following paragraph and then press enter/return.')
        print('If you only type part of it, you will be scored only on that part.\n')
        print(reference)
        print()

        start = datetime.now()
        typed = input()
        if not typed:
            print('Goodbye.')
            return
        print()

        elapsed = (datetime.now() - start).total_seconds()
        print("Nice work!")
        print('Words per minute:', wpm(typed, elapsed))
        print('Accuracy:        ', accuracy(typed, reference))

        print('\nPress enter/return for the next paragraph or type q to quit.')
        if input().strip() == 'q':
            return
        i += 1


@main
def run(*args):
    """Read in the command-line argument and calls corresponding functions."""
    import argparse
    parser = argparse.ArgumentParser(description="Typing Test")
    parser.add_argument('topic', help="Topic word", nargs='*')
    parser.add_argument('-t', help="Run typing test", action='store_true')

    args = parser.parse_args()
    if args.t:
        run_typing_test(args.topic)
