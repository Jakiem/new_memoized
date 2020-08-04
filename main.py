# BEGIN (write your solution here)
def memoizing(loop):
    def wrapper(func):
        cash = {}
        list_ = []
        def inner(*args):
            for i in args:
                if i not in list_:
                  list_.append(i)
                  if len(list_) > loop:
                      del cash[list_[0]]
                      del list_[0]
                  if i in cash:
                      return cash[i]
                  cash[i] = func(*args)
                  print(cash)
                  return cash[i]
                return cash[i]
        return inner
    return wrapper
# END



def test_memoizing():
    arguments = []

    @memoizing(3)
    def inc(argument):
        arguments.append(argument)
        return argument + 1

    assert inc(inc(inc(0))) == 3
    assert arguments == [0, 1, 2]

    _ = inc(inc(inc(0)))
    assert arguments == [0, 1, 2], "All resluts sholud be got from memory!"

    assert inc(10) == 11
    assert arguments == [0, 1, 2, 10], "New argument should be added!"

    assert inc(0) == 1
    assert arguments == [0, 1, 2, 10, 0], (
        "Result for zero should be recalculated!",
    )
test_memoizing()