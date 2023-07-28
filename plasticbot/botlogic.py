import random

#random tips generator
def gen_tips():
    t1 = "Remember to always throw your garbage in it's place."
    t2 = "Don't throw your plastic wastes away, recycle it!"
    t3 = "Don't throw your garbage to the river!"
    t4 = "You can sort you garbage from organic and anorganic!"
    tips = [t1, t2, t3, t4]
    return random.choice(tips)