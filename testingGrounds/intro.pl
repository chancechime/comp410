% Alice likes pizza, burgers, burritos, and yogurt.
likes(alice, pizza).
likes(alice, burgers).
likes(alice, burritos).
likes(alice, yogurt).

% Bob likes pizza, burgers, salad, and milks.
likes(bob, pizza).
likes(bob, burgers).
likes(bob, salad).
likes(bob, milks).

% Bill likes food served warm
likes(bill, bacon, warm).

% def myAppend(list1, list2):
%     if isinstance(list1, Nil):
%         return list2
%     elif: isinstance(list1, Cons):
%         rest = myAppend(list1.tail, list2)
%         return Cons(list1.head, rest)

myAppend(nil, List, List).
myAppend(cons(Head, Tail), List2, Output) :-
    Output = cons(Head, Rest),
    myAppend(Tail, List2, Rest).