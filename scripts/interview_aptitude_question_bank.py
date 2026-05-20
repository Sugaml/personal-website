"""Logical / aptitude questions for technical interview prep."""

from __future__ import annotations

Question = dict


def q(stem: str, options: dict[str, str], answer: str | list[str], why: str) -> Question:
    return {"stem": stem, "options": options, "answer": answer, "why": why.strip()}


def all_questions() -> dict[str, list[Question]]:
    sections = {
        "Number series": _number_series(),
        "Letter and word patterns": _letter_patterns(),
        "Analogies and classification": _analogies(),
        "Syllogisms and deductive logic": _syllogisms(),
        "Coding-decoding": _coding_decoding(),
        "Blood relations and family logic": _blood_relations(),
        "Direction and distance": _direction(),
        "Seating and ordering": _seating(),
        "Puzzles and constraints": _puzzles(),
        "Data interpretation logic": _data_logic(),
        "Tech-flavored reasoning": _tech_logical(),
    }
    for item in _extra_questions():
        sections.setdefault(item["category"], []).append(
            q(item["stem"], item["options"], item["answer"], item["why"])
        )
    return sections


def _extra_questions() -> list[dict]:
    """Additional questions to expand the bank."""
    raw = [
        ("Number series", "Find the next: 81, 27, 9, 3, ?", {"A": "0", "B": "1", "C": "2", "D": "6"}, "B", "÷3 each step: 3÷3=1."),
        ("Number series", "Find the next: 2, 5, 10, 17, 26, ?", {"A": "35", "B": "37", "C": "39", "D": "41"}, "B", "Differences +3,+5,+7,+9 → +11 → 26+11=37."),
        ("Number series", "Find the next: 1, 8, 27, 64, ?", {"A": "100", "B": "125", "C": "216", "D": "343"}, "B", "Cubes: 1³, 2³, 3³, 4³ → 5³=125."),
        ("Letter and word patterns", "Complete: Z26, Y25, X24, ?", {"A": "W23", "B": "V22", "C": "U21", "D": "W22"}, "A", "Letter steps back; number is alphabet position."),
        ("Analogies and classification", "Subnet is to Network as Container is to ?", {"A": "Pod", "B": "Host", "C": "Cluster", "D": "Image"}, "B", "Subnet segments a network; container runs on a host OS/kernel."),
        ("Syllogisms and deductive logic", "No untested code reaches production. This change reached production. Therefore", {"A": "It was tested", "B": "It was not tested", "C": "Testing is optional", "D": "Production is untested"}, "A", "Contrapositive: production → tested."),
        ("Puzzles and constraints", "Clock shows 3:15. Angle between hour and minute hands?", {"A": "0°", "B": "7.5°", "C": "15°", "D": "30°"}, "B", "Hour hand past 3: 97.5°; minute at 90° → 7.5°."),
        ("Tech-flavored reasoning", "Replica set: 3 nodes, majority quorum. How many failures tolerated?", {"A": "0", "B": "1", "C": "2", "D": "3"}, "B", "Need 2 of 3 for majority; one node may fail."),
        ("Data interpretation logic", "p99 latency 200 ms, median 40 ms. Best inference?", {"A": "Most users see ~40 ms; tail is heavy", "B": "Everyone sees 200 ms", "C": "Median equals p99", "D": "System is unusable"}, "A", "Median describes typical; p99 captures slow tail."),
        ("Direction and distance", "Walk 3 km East, 4 km North. Bearing from start?", {"A": "North-East", "B": "53° North of East", "C": "Both A and B describe it", "D": "South-West"}, "C", "3-4-5 triangle; arctan(4/3) ≈ 53° north of east."),
        ("Seating and ordering", "Deadline Mon < Wed < Fri. Job X due Wed, Y due before X, Z due Fri. Order?", {"A": "Y, X, Z", "B": "X, Y, Z", "C": "Y, Z, X", "D": "Z, Y, X"}, "A", "Y before Wed, X Wed, Z Fri."),
        ("Blood relations and family logic", "Mother's brother is your ?", {"A": "Uncle", "B": "Cousin", "C": "Nephew", "D": "Brother"}, "A", "Maternal uncle."),
        ("Coding-decoding", "What is decimal 15 written in hexadecimal?", {"A": "E", "B": "F", "C": "G", "D": "15"}, "B", "15₁₀ = F₁₆."),
        ("Number series", "Find the next: 10, 13, 19, 28, 40, ?", {"A": "52", "B": "55", "C": "58", "D": "61"}, "B", "Differences +3, +6, +9, +12 → +15 → 40+15=55."),
        ("Analogies and classification", "Cache is to RAM as RAM is to ?", {"A": "CPU register / faster tier", "B": "Disk", "C": "Network", "D": "GPU only"}, "A", "Each layer is faster storage closer to the compute unit."),
        ("Syllogisms and deductive logic", "Some alerts are false positives. All false positives should be tuned. Therefore", {"A": "Some alerts should be tuned", "B": "All alerts are false", "C": "No tuning needed", "D": "All alerts are true"}, "A", "Some alerts fall in the 'false positive' set that requires tuning."),
        ("Puzzles and constraints", "You have 12 balls, one heavier. Minimum balance weighings?", {"A": "2", "B": "3", "C": "4", "D": "5"}, "B", "4-4-4 split; up to 3 weighings classic—actually 12 balls one heavy: 4 vs 4, then 2 vs 2, then 1 vs 1 = 3. For 3^k >= 12, k=3 → B."),
        ("Tech-flavored reasoning", "MTTR drops but incident count doubles. Best reading?", {"A": "Team fixes faster but stability worsened", "B": "System is perfect", "C": "MTTR is useless", "D": "Fewer incidents"}, "A", "Faster recovery does not imply fewer failures."),
        ("Data interpretation logic", "Success rate rises from 80% to 90% while volume drops 50%. Careful conclusion?", {"A": "Absolute successes may have fallen", "B": "Successes definitely doubled", "C": "Volume is irrelevant", "D": "Rate alone proves improvement"}, "A", "Check counts: 0.9 × 50% volume vs 0.8 × 100%."),
        ("Letter and word patterns", "Rearrange the letters of LISTEN (one word, common English).", {"A": "SILENT", "B": "ENLIST", "C": "INLETS", "D": "TINSEL"}, "A", "LISTEN is a classic anagram of SILENT."),
    ]
    out = []
    for cat, stem, opts, ans, why in raw:
        out.append({"category": cat, "stem": stem, "options": opts, "answer": ans, "why": why})
    return out


def _number_series() -> list[Question]:
    scenarios = [
        ("Find the next number: 2, 6, 12, 20, 30, ?", {"A": "40", "B": "42", "C": "44", "D": "48"}, "B",
         "Differences are +4, +6, +8, +10; next difference is +12 → 30 + 12 = 42."),
        ("Find the next number: 3, 9, 27, 81, ?", {"A": "162", "B": "243", "C": "324", "D": "729"}, "B",
         "Each term is multiplied by 3 (geometric progression). 81 × 3 = 243."),
        ("Find the next number: 1, 1, 2, 3, 5, 8, 13, ?", {"A": "18", "B": "20", "C": "21", "D": "24"}, "C",
         "Fibonacci: each term is the sum of the two before it. 8 + 13 = 21."),
        ("Find the next number: 64, 32, 16, 8, ?", {"A": "2", "B": "4", "C": "6", "D": "0"}, "B",
         "Each term is half the previous. 8 ÷ 2 = 4."),
        ("Find the next number: 5, 11, 23, 47, 95, ?", {"A": "189", "B": "191", "C": "193", "D": "190"}, "B",
         "Pattern: ×2 + 1. 95 × 2 + 1 = 191."),
        ("Find the next number: 121, 144, 169, 196, ?", {"A": "216", "B": "225", "C": "256", "D": "289"}, "B",
         "Perfect squares: 11², 12², 13², 14² → next is 15² = 225."),
        ("Find the next number: 2, 3, 5, 7, 11, 13, ?", {"A": "15", "B": "17", "C": "19", "D": "21"}, "B",
         "Prime numbers in order. After 13 comes 17."),
        ("Find the next number: 100, 50, 52, 26, 28, ?", {"A": "12", "B": "14", "C": "16", "D": "30"}, "B",
         "Alternating ÷2 and +2: 100÷2=50, +2=52, ÷2=26, +2=28, ÷2=14."),
        ("Find the next number: 7, 14, 28, 56, ?", {"A": "84", "B": "98", "C": "112", "D": "128"}, "C",
         "Each term doubles. 56 × 2 = 112."),
        ("Find the missing number: 4, 9, 19, 39, ?", {"A": "59", "B": "69", "C": "79", "D": "89"}, "C",
         "Each term ≈ previous × 2 + 1: 4×2+1=9, 9×2+1=19, 19×2+1=39, 39×2+1=79."),
        ("Find the next number: 1, 4, 9, 16, 25, ?", {"A": "30", "B": "36", "C": "49", "D": "64"}, "B",
         "Squares of 1, 2, 3, 4, 5 → next is 6² = 36."),
        ("Find the next number: 0, 1, 1, 2, 4, 7, 13, ?", {"A": "20", "B": "22", "C": "24", "D": "26"}, "C",
         "Tribonacci-style: each term is sum of previous three. 4+7+13=24."),
    ]
    return [q(s, o, a, w) for s, o, a, w in scenarios]


def _letter_patterns() -> list[Question]:
    scenarios = [
        ("Find the next pair: AZ, BY, CX, ?", {"A": "DW", "B": "EV", "C": "FU", "D": "ET"}, "A",
         "First letter advances A→B→C→D; second retreats Z→Y→X→W → DW."),
        ("Find the next term: J, F, M, A, M, J, ?", {"A": "J", "B": "A", "C": "S", "D": "O"}, "A",
         "First letters of months: Jan, Feb, Mar, Apr, May, Jun → Jul (J)."),
        ("Find the next term: Z, X, V, T, ?", {"A": "S", "B": "R", "C": "Q", "D": "P"}, "B",
         "Skip one letter backward in the alphabet: Z, X, V, T, R."),
        ("ACE, BDF, CEG, ?", {"A": "DFH", "B": "DGI", "C": "EFH", "D": "FGI"}, "A",
         "Each group shifts all three letters forward by one: A→D, C→F, E→H."),
        ("Find the next: AB, DE, GH, JK, ?", {"A": "LM", "B": "MN", "C": "NO", "D": "OP"}, "B",
         "Pairs of consecutive letters with one letter skipped between pairs: AB (skip C) DE … → MN."),
        ("If CODE is written as DPEF (each letter +1), how is DATA written?", {"A": "EBUB", "B": "EBTA", "C": "DATB", "D": "CZSZ"}, "A",
         "Shift each letter +1: D→E, A→B, T→U, A→B → EBUB."),
        ("Find the odd one out: A) EQ  B) FL  C) IR  D) KO", {"A": "EQ", "B": "FL", "C": "IR", "D": "KO"}, "C",
         "EQ, FL, KO are +5 letter pairs (E+5=Q, etc.). IR is +6 (I→R)."),
        ("Complete: M, O, Q, S, ?", {"A": "T", "B": "U", "C": "V", "D": "W"}, "B",
         "Skip one letter: M, (N), O, (P), Q, (R), S, (T), U."),
    ]
    return [q(s, o, a, w) for s, o, a, w in scenarios]


def _analogies() -> list[Question]:
    scenarios = [
        ("Book is to Library as Car is to ?", {"A": "Road", "B": "Garage", "C": "Driver", "D": "Engine"}, "B",
         "A book is stored in a library; a car is stored in a garage."),
        ("Painter is to Brush as Writer is to ?", {"A": "Paper", "B": "Pen", "C": "Novel", "D": "Desk"}, "B",
         "Tool relationship: painter uses a brush; writer uses a pen."),
        ("Odometer is to Mileage as Compass is to ?", {"A": "Speed", "B": "Direction", "C": "Needle", "D": "Hiking"}, "B",
         "Odometer measures mileage; compass indicates direction."),
        ("Caterpillar is to Butterfly as Tadpole is to ?", {"A": "Fish", "B": "Frog", "C": "Pond", "D": "Egg"}, "B",
         "Metamorphosis: immature form to adult form."),
        ("Which does not belong? A) Triangle  B) Square  C) Circle  D) Cube", {"A": "Triangle", "B": "Square", "C": "Circle", "D": "Cube"}, "D",
         "Triangle, square, circle are 2D shapes; cube is 3D."),
        ("Microphone is to Sound as Camera is to ?", {"A": "Film", "B": "Lens", "C": "Image", "D": "Light"}, "C",
         "Microphone captures sound; camera captures an image."),
        ("CPU is to Computer as Engine is to ?", {"A": "Wheel", "B": "Car", "C": "Fuel", "D": "Road"}, "B",
         "CPU is the core processing unit of a computer; engine is the core power unit of a car."),
        ("Encryption is to Confidentiality as Checksum is to ?", {"A": "Availability", "B": "Integrity", "C": "Latency", "D": "Throughput"}, "B",
         "Encryption protects confidentiality; checksums detect corruption (integrity)."),
    ]
    return [q(s, o, a, w) for s, o, a, w in scenarios]


def _syllogisms() -> list[Question]:
    scenarios = [
        (
            "All developers write code. Some developers are architects. Which conclusion MUST be true?",
            {"A": "All architects write code", "B": "Some people who write code are architects",
             "C": "No architects write code", "D": "All architects are developers"},
            "B",
            "Architects in the 'some developers' group write code, so some code writers are architects. "
            "We cannot conclude all architects write code or are developers.",
        ),
        (
            "No critical bugs are ignored. Some open tickets are critical bugs. Which follows?",
            {"A": "Some open tickets are not ignored", "B": "All open tickets are ignored",
             "C": "No open tickets exist", "D": "All tickets are critical"},
            "A",
            "Open tickets that are critical bugs cannot be ignored, so at least some open tickets are not ignored.",
        ),
        (
            "If it rains, the deploy window is postponed. It rained. What can we conclude?",
            {"A": "Deploy is postponed", "B": "Deploy happened on time", "C": "It will not rain tomorrow",
             "D": "Postponement causes rain"},
            "A",
            "Modus ponens: rain → postpone; rain is true, so postpone follows.",
        ),
        (
            "If latency exceeds 200 ms, auto-scale triggers. Latency is 150 ms. What follows?",
            {"A": "Auto-scale definitely triggered", "B": "Auto-scale definitely did not trigger",
             "C": "We cannot conclude whether auto-scale triggered", "D": "Latency will exceed 200 ms soon"},
            "C",
            "Affirming the antecedent fails: low latency means the sufficient condition for scaling was not met, "
            "but scaling could still happen for other reasons.",
        ),
        (
            "All prime numbers greater than 2 are odd. The number 9 is odd. Therefore 9 is prime. This argument is",
            {"A": "Valid", "B": "Invalid — affirming the consequent", "C": "Invalid — denying the antecedent",
             "D": "A tautology"},
            "B",
            "Oddness does not imply primality (9 = 3×3). This is the affirming-the-consequent fallacy.",
        ),
        (
            "Either the build failed or tests failed (or both). Tests did not fail. Conclusion?",
            {"A": "Build failed", "B": "Build passed", "C": "Both failed", "D": "Nothing can be concluded"},
            "A",
            "Disjunctive syllogism: (B ∨ T); ¬T ⊢ B.",
        ),
    ]
    return [q(s, o, a, w) for s, o, a, w in scenarios]


def _coding_decoding() -> list[Question]:
    scenarios = [
        ("In a code, CLOUD → DMPVE. Each letter shifts +1. What is K8S?", {"A": "L9T", "B": "L8T", "C": "K9S", "D": "J7R"}, "A",
         "Apply +1 to each character: K→L, 8→9, S→T."),
        ("If 253 means 'data pipeline' and 157 means 'data lake', what does 25 likely mean?", {"A": "lake", "B": "data", "C": "pipeline", "D": "storage"}, "B",
         "Prefix 25 is shared → 'data'."),
        ("MACHINE is coded as NBDIJOF (+1 each). How is NEURAL coded?", {"A": "OFVSBM", "B": "MDTZQK", "C": "OFURBM", "D": "NEURAL"}, "A",
         "Shift each letter forward by one."),
        ("In binary, what is decimal 13?", {"A": "1100", "B": "1101", "C": "1011", "D": "1110"}, "B",
         "13 = 8+4+1 = 1101₂."),
        ("If @ means + and # means ×, evaluate 4 @ 3 # 2 (standard order: # before @).", {"A": "10", "B": "14", "C": "24", "D": "20"}, "A",
         "3 # 2 = 6, then 4 @ 6 = 10."),
        ("ROT13 of 'HELLO' (letters only) is", {"A": "URYYB", "B": "IFMMP", "C": "KHOOR", "D": "GRZZB"}, "A",
         "H→U, E→R, L→Y, L→Y, O→B."),
    ]
    return [q(s, o, a, w) for s, o, a, w in scenarios]


def _blood_relations() -> list[Question]:
    scenarios = [
        ("A is B's father. B is C's mother. How is A related to C?", {"A": "Grandfather", "B": "Grandmother",
         "C": "Uncle", "D": "Father"}, "A",
         "A is parent of B; B is parent of C → A is grandfather of C."),
        ("Pointing to a photo, Sam says 'He is my mother's only son-in-law.' Who is in the photo?", {"A": "Sam",
         "B": "Sam's brother", "C": "Sam's husband or wife's brother", "D": "Sam's father"}, "C",
         "Mother's only son-in-law is the husband of her daughter (or son's wife's brother in some puzzles)—"
         "typically Sam's husband if Sam is female, or the man married to Sam's sister. Standard answer: Sam's husband."),
        ("X is Y's brother. Y is Z's sister. Z is X's ?", {"A": "Brother", "B": "Sister", "C": "Sibling", "D": "Cousin"}, "C",
         "X and Y share parents; Y and Z share parents → X and Z are siblings."),
        ("If P + Q means P is father of Q, and P - Q means P is sister of Q, then A + B - C means", {"A": "A is uncle of C",
         "B": "A is grandfather of C", "C": "A is father of B who is sister of C", "D": "C is aunt of A"}, "C",
         "A is father of B; B is sister of C."),
    ]
    return [q(s, o, a, w) for s, o, a, w in scenarios]


def _direction() -> list[Question]:
    scenarios = [
        ("You walk 10 m North, then 10 m East. How far are you from the start (straight line)?", {"A": "10 m",
         "B": "14.14 m", "C": "20 m", "D": "15 m"}, "B",
         "Right triangle: √(10²+10²) = √200 ≈ 14.14 m."),
        ("Facing East, you turn right twice. Which direction do you face?", {"A": "North", "B": "South", "C": "West", "D": "East"}, "C",
         "East → South (right once) → West (right twice)."),
        ("A bird flies 6 km South, 8 km West. Distance from start?", {"A": "10 km", "B": "12 km", "C": "14 km", "D": "2 km"}, "A",
         "6-8-10 Pythagorean triple."),
        ("Town A is north of B. City C is east of B. City C is relative to A mostly", {"A": "South-east", "B": "North-east",
         "C": "South-west", "D": "North-west"}, "A",
         "From A (north of B), B is south; C is east of B → south-east of A."),
    ]
    return [q(s, o, a, w) for s, o, a, w in scenarios]


def _seating() -> list[Question]:
    scenarios = [
        (
            "Five people sit in a row. A is not at either end. B is immediately right of A. C is at the left end. "
            "Who is at the right end?",
            {"A": "A", "B": "B", "C": "D or E (one of the remaining)", "D": "Cannot be determined without more info"},
            "D",
            "Positions _ _ _ _ _. C at pos 1. A not at 1 or 5. B right of A. Several arrangements remain for D/E at the right end.",
        ),
        (
            "Six friends A–F sit around a circular table facing the center. A is opposite D. B is two seats right of A. "
            "Who is opposite B?",
            {"A": "D", "B": "E", "C": "F", "D": "Depends on clockwise numbering"},
            "D",
            "Circular seating with 'two seats right' is ambiguous without a fixed numbering direction—classic under-specified puzzle.",
        ),
        (
            "In a queue, Sam is 7th from the front and 12th from the back. How many people are in the queue?",
            {"A": "18", "B": "19", "C": "20", "D": "21"}, "B",
             "7 + 12 - 1 = 18… Wait: 7th from front means 6 ahead; 12th from back means 11 behind; total = 6+1+11=18. "
             "Standard formula: 7+12-1=18 → A. Recount: positions 1..n, Sam at 7 and at n-11, so n-11=7, n=18.",
        ),
        (
            "Tasks T1, T2, T3 must run in order. T2 cannot run before T1. T3 runs last. Valid order?",
            {"A": "T2, T1, T3", "B": "T1, T2, T3", "C": "T3, T1, T2", "D": "T1, T3, T2"},
            "B",
            "T3 last eliminates C. T2 after T1 eliminates A. D has T3 before T2 done—invalid. Only T1, T2, T3 works.",
        ),
    ]
    # Fix queue answer explanation - answer should be A (18)
    scenarios[2] = (
        scenarios[2][0],
        scenarios[2][1],
        "A",
        "Sam is counted in both ranks: total = 7 + 12 - 1 = 18 people.",
    )
    return [q(s, o, a, w) for s, o, a, w in scenarios]


def _puzzles() -> list[Question]:
    scenarios = [
        (
            "Three boxes: one has only apples, one only oranges, one mixed. Labels are ALL wrong. "
            "You may pick one fruit from one box. Which box do you open to label all boxes correctly?",
            {"A": "Box labeled Apples", "B": "Box labeled Oranges", "C": "Box labeled Mixed", "D": "Any box works equally"},
            "C",
            "Open 'Mixed' (mislabeled): you draw a fruit proving pure apple or orange; use wrong labels on others to deduce the rest.",
        ),
        (
            "Two statements: (1) Exactly one of us is lying. (2) Exactly two of us are lying. "
            "Spoken by two people—can both be true?",
            {"A": "Yes", "B": "No — they contradict", "C": "Only if both lie", "D": "Only if both tell truth"},
            "B",
            "Statement (1) implies one liar total; (2) implies two liars—cannot both describe the same pair consistently.",
        ),
        (
            "You have 8 identical-looking balls; one is heavier. Minimum weighings on a balance scale?",
            {"A": "1", "B": "2", "C": "3", "D": "4"},
            "B",
            "Split 3-3-2: weigh 3 vs 3; if equal, weigh 2; else weigh 1 vs 1 within heavy group → 2 weighings.",
        ),
        (
            "A is taller than B. C is shorter than B. D is taller than A. Who is tallest?",
            {"A": "A", "B": "B", "C": "D", "D": "Cannot tell"},
            "C",
            "D > A > B > C.",
        ),
        (
            "Three switches in another room control one bulb. You enter once. How do you identify every switch?",
            {"A": "Turn one on 5 minutes, off; turn second on; enter—lit=second, warm-off=first, cold-off=third",
             "B": "Turn all on at once", "C": "Impossible in one visit", "D": "Flip randomly"},
            "A",
            "Use bulb heat: on, warm-off, cold-off identifies all three with one room entry.",
        ),
    ]
    return [q(s, o, a, w) for s, o, a, w in scenarios]


def _data_logic() -> list[Question]:
    scenarios = [
        (
            "Server uptime logs: Mon 99.9%, Tue 99.8%, Wed 99.2%, Thu 99.9%, Fri 99.8%. "
            "Which day is the clear outlier for investigation?",
            {"A": "Monday", "B": "Wednesday", "C": "Friday", "D": "Thursday"},
            "B",
            "Wednesday at 99.2% is materially below the cluster near 99.8–99.9%.",
        ),
        (
            "A test has 40 questions. +2 for correct, -0.5 for wrong, 0 for blank. Score is 52 with 4 blank. "
            "How many were correct?",
            {"A": "28", "B": "30", "C": "32", "D": "34"},
            "B",
            "Let c be correct, w wrong: c+w=36, 2c-0.5w=52. Substitute w=36-c: 2c-0.5(36-c)=52 → 2.5c=70 → c=28… "
            "Recalc: 2c - 0.5(36-c) = 52 → 2c -18 +0.5c = 52 → 2.5c = 70 → c=28. Check: 28 correct, 8 wrong, 4 blank: 56-4=52. Answer A=28.",
        ),
        (
            "If 40% of requests fail retries and 25% of those retries succeed, what share of original requests recover via retry?",
            {"A": "10%", "B": "15%", "C": "25%", "D": "40%"},
            "A",
            "0.40 × 0.25 = 0.10 = 10% of original traffic.",
        ),
        (
            "Median of {3, 7, 7, 8, 22} is 7. A new value 100 is added. New median?",
            {"A": "7", "B": "7.5", "C": "8", "D": "22"},
            "A",
            "Sorted: 3, 7, 7, 8, 22, 100 — even count, median is average of 3rd and 4th = (7+8)/2 = 7.5 → B.",
        ),
    ]
    scenarios[1] = (scenarios[1][0], scenarios[1][1], "A", scenarios[1][3].split("Answer A")[0] + "28 correct, 8 wrong, 4 blank → 56−4=52.")
    scenarios[3] = (scenarios[3][0], scenarios[3][1], "B", "Six values: middle pair 7 and 8 → median 7.5.")
    return [q(s, o, a, w) for s, o, a, w in scenarios]


def _tech_logical() -> list[Question]:
    scenarios = [
        (
            "A service handles 1000 RPS. Each instance handles 200 RPS. Minimum instances for headroom if you want 25% spare capacity?",
            {"A": "5", "B": "6", "C": "7", "D": "8"},
            "C",
            "Need 1000/200 = 5 instances at 100%; with 25% headroom: 5 × 1.25 = 6.25 → round up to 7.",
        ),
        (
            "Logs show errors spike only when deploy version v2 runs AND cache is cold. Best next step?",
            {"A": "Rollback v2 immediately without analysis", "B": "Reproduce with v2 and cold cache in staging",
             "C": "Delete all logs", "D": "Disable monitoring"},
            "B",
            "Isolate the interaction (version × cache state) before changing production.",
        ),
        (
            "If p → q and q → r, which is equivalent to p → r?",
            {"A": "Hypothetical syllogism (transitivity)", "B": "Converse error", "C": "Denying the antecedent", "D": "None"},
            "A",
            "Chain of implications: p→q and q→r gives p→r."),
        (
            "A hash table has O(1) average lookup. Worst case becomes O(n) when",
            {"A": "Many keys collide into the same bucket", "B": "The table is empty", "C": "Keys are sorted", "D": "Load factor is low"},
            "A",
            "Collision chains degrade to linear search in a bucket.",
        ),
        (
            "You must choose: (A) 99.99% uptime SLA or (B) feature shipped 2 weeks earlier. "
            "Stakeholders say revenue loss without feature exceeds outage cost. Rational choice?",
            {"A": "Always pick SLA", "B": "Quantify outage cost vs delayed revenue; decide on expected value",
             "C": "Always ship early", "D": "Flip a coin"},
            "B",
            "Trade-off reasoning uses expected cost/benefit, not absolutes.",
        ),
        (
            "Two independent services each have 99.9% availability. Serial dependency (A then B) availability is approximately",
            {"A": "99.9%", "B": "99.8%", "C": "99.99%", "D": "100%"},
            "B",
            "0.999 × 0.999 ≈ 0.998 = 99.8%.",
        ),
        (
            "Bug reports: 70% UI, 20% API, 10% DB. You fix all DB bugs. New reports still show ~10% DB. Likely explanation?",
            {"A": "Fix failed", "B": "Reporting is categorical; proportion can stay if volume changed or mis-tagged",
             "C": "DB cannot have bugs", "D": "UI bugs became DB"},
            "B",
            "Percentages shift with denominator; misclassification and new bugs matter—read charts carefully.",
        ),
        (
            "Which schedule minimizes average wait if three jobs take 1, 3, 9 minutes (non-preemptive, one CPU)?",
            {"A": "Shortest job first: 1, 3, 9", "B": "Longest first", "C": "Random", "D": "9, 3, 1"},
            "A",
            "SJF minimizes average waiting time for known burst times.",
        ),
    ]
    return [q(s, o, a, w) for s, o, a, w in scenarios]
