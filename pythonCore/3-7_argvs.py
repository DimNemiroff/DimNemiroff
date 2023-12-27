



def first(size, *argvs ):
    return size + len(argvs)


def second(size, **comment ):
    return size + len(comment)

print(first(5, "first", "second", "third"),
first(1, "Alex", "Boris"),
second(3, comment_one="first", comment_two="second", comment_third="third"),
second(10, comment_one="Alex", comment_two="Boris")
)
