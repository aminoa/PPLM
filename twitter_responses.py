from run_pplm import *

def generate_tweets(is_positive, cond_text, length, gamma, num_iterations, num_samples, stepsize, kl_scale, gm_scale):
    if is_positive:
        class_label = 2
    else:
        class_label = 3

    # modify this method properly
    run_pplm_example(
        cond_text=cond_text,
        num_samples=num_samples,
        discrim='sentiment',
        class_label=class_label,
        length=length,
        stepsize=stepsize,
        num_iterations=num_iterations,
        gamma=gamma,
        kl_scale=kl_scale,
        gm_scale=gm_scale,
    )

if __name__ == '__main__':
    # need to keep track of history of generated tweets
    parser = argparse.ArgumentParser()
    parser.add_argument("--is_positive", type=bool, default=True)
    parser.add_argument("--cond_text", type=str, default="I love")
    parser.add_argument("--length", type=int, default=50)
    parser.add_argument("--gamma", type=float, default=1.5)
    parser.add_argument("--num_iterations", type=int, default=3)
    parser.add_argument("--num_samples", type=int, default=1)
    parser.add_argument("--stepsize", type=float, default=0.03)
    parser.add_argument("--kl_scale", type=float, default=0.01)
    parser.add_argument("--gm_scale", type=float, default=0.95)
    args = parser.parse_args()

    generate_tweets(args.is_positive, args.cond_text, args.length, args.gamma, args.num_iterations, args.num_samples, args.stepsize, args.kl_scale, args.gm_scale)
