from run_pplm import *

def generate_tweet(is_positive, cond_text, length, stepsize):
    if is_positive:
        class_label = 2
        # cond_text += ". I agree because "
    else:
        class_label = 3
        # cond_text += ". I disagree because "
    # length = len(cond_text)

    tweet = run_pplm_example(
        cond_text=cond_text,
        discrim='sentiment',
        class_label=class_label,
        bag_of_words='paper_code/wordlists/twitter.txt',
        length=length,
        stepsize=stepsize,
        sample=True,
        num_iterations=10,
        gamma=1.0,
        gm_scale=0.5,
        kl_scale=0.5,
        verbosity="quiet",
        grad_length=30
    )

    tweet = tweet[len(cond_text) + 14:]
    return tweet

# need to keep track of history of generated tweets
# is_positive = True
# cond_text = "I hated the new guardians of the galaxy movie"
# length = 30
# stepsize = 0.2

# print(generate_tweet(is_positive, cond_text, length, stepsize))
