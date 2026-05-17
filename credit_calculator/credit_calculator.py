import math
import argparse
import sys

parser = argparse.ArgumentParser()
parser.add_argument("--type")
parser.add_argument("--principal", type=float)
parser.add_argument("--periods", type=int)
parser.add_argument("--interest", type=float)
parser.add_argument("--payment", type=float)

args = parser.parse_args()

params = [args.type, args.principal, args.periods, args.interest, args.payment]
neg_check = [p for p in params[1:] if p is not None and p < 0]

if len(sys.argv) < 5 or not args.interest or args.type not in ["annuity", "diff"] or neg_check:
    print("Incorrect parameters")
    sys.exit()

i = args.interest / (12 * 100)

if args.type == "diff":
    if args.payment:
        print("Incorrect parameters")
    else:
        total_repaid = 0
        for m in range(1, args.periods + 1):
            dm = math.ceil(
                args.principal / args.periods + i * (args.principal - (args.principal * (m - 1)) / args.periods))
            total_repaid += dm
            print(f"Month {m}: payment is {dm}")
        print(f"\nOverpayment = {int(total_repaid - args.principal)}")

elif args.type == "annuity":
    if not args.periods:
        n = math.ceil(math.log(args.payment / (args.payment - i * args.principal), 1 + i))
        years, months = n // 12, n % 12
        res = "It will take "
        if years > 0: res += f"{years} year" + ("s" if years > 1 else "")
        if years > 0 and months > 0: res += " and "
        if months > 0: res += f"{months} month" + ("s" if months > 1 else "")
        print(f"{res} to repay this loan!")
        print(f"Overpayment = {int(n * args.payment - args.principal)}")

    elif not args.payment:
        a = math.ceil(args.principal * (i * (1 + i) ** args.periods) / ((1 + i) ** args.periods - 1))
        print(f"Your annuity payment = {a}!")
        print(f"Overpayment = {int(a * args.periods - args.principal)}")

    elif not args.principal:
        p = math.floor(args.payment / ((i * (1 + i) ** args.periods) / ((1 + i) ** args.periods - 1)))
        print(f"Your loan principal = {p}!")
        print(f"Overpayment = {int(args.payment * args.periods - p)}")