from logic import *

AKnight = Symbol("A is a Knight")
AKnave = Symbol("A is a Knave")

BKnight = Symbol("B is a Knight")
BKnave = Symbol("B is a Knave")

CKnight = Symbol("C is a Knight")
CKnave = Symbol("C is a Knave")

# Puzzle 0
# A says "I am both a knight and a knave."
knowledge0 = And(
    # A is either a Knight or a Knave
    Or(AKnight, AKnave),
    # If A is a Knight, it would imply that he is a Knight and a Knave
    Implication(AKnight,And(AKnight, AKnave))
)

# Puzzle 1
# A says "We are both knaves."
# B says nothing.
knowledge1 = And(
    # A is either a Knight or a Knave
    Or(AKnight, AKnave),
    # B is either a Knight or a Knave
    Or(BKnight, BKnave),
    # If A is a Knave, what he says is false
    Biconditional(AKnave, Not(And(AKnave, BKnave)))
)

# Puzzle 2
# A says "We are the same kind."
# B says "We are of different kinds."
knowledge2 = And(
    # A is either a Knight or a Knave
    Or(AKnight, AKnave),
    # B is either a Knight or a Knave
    Or(BKnight, BKnave),
    # If A is a Knight, what he says is true
    Biconditional(AKnight, Or(And(AKnave, BKnave),And(AKnight,BKnight))),
    # If B is a Knight, what he says is true
    Biconditional(BKnight, Or(And(AKnave, BKnight),And(AKnight,BKnave))),
    # If B is a Knave, what he says is false
    Implication(BKnave, Not(Or(And(AKnave, BKnight),And(AKnight,BKnave))))
)

# Puzzle 3
# A says either "I am a knight." or "I am a knave.", but you don't know which.
# B says "A said 'I am a knave'."
# B says "C is a knave."
# C says "A is a knight."
knowledge3 = And(
    # A is either a Knight or a Knave
    Or(AKnight, AKnave),
    # B is either a Knight or a Knave
    Or(BKnight, BKnave),
    # C is either a Knight or a Knave
    Or(CKnight, CKnave),
    # If B is a Knight, what he says is true, and if A is a knave, what he says is false
    Biconditional(BKnight, Biconditional(AKnave, Not(AKnave))),
    Biconditional(BKnight, CKnave),
    # If C is a Knight, what he says is true
    Biconditional(CKnight, AKnight)
)


def main():
    symbols = [AKnight, AKnave, BKnight, BKnave, CKnight, CKnave]
    puzzles = [
        ("Puzzle 0", knowledge0),
        ("Puzzle 1", knowledge1),
        ("Puzzle 2", knowledge2),
        ("Puzzle 3", knowledge3)
    ]
    for puzzle, knowledge in puzzles:
        print(puzzle)
        if len(knowledge.conjuncts) == 0:
            print("    Not yet implemented.")
        else:
            for symbol in symbols:
                if model_check(knowledge, symbol):
                    print(f"    {symbol}")


if __name__ == "__main__":
    main()
