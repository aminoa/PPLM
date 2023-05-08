from run_pplm import *

def generate_tweet(is_positive, cond_text, length, stepsize):
    if is_positive:
        class_label = 2
    else:
        class_label = 3

    # modify this method properly
    tweet = run_pplm_example(
        cond_text=cond_text,
        discrim='sentiment',
        class_label=class_label,
        length=length,
        stepsize=stepsize,
        sample=True,
        num_iterations=10,
        gamma=1.0,
        gm_scale=0.7,
        kl_scale=0.2,
        verbosity="regular"
    )

    # print(tweet)

    tweet = tweet[len(cond_text) + 14:]
    return tweet

# need to keep track of history of generated tweets
# is_positive = True
# cond_text = "I hated the new guardians of the galaxy movie. "
# length = 30
# stepsize = 0.2

# print(generate_tweet(is_positive, cond_text, length, stepsize))