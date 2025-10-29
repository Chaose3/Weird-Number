def find_weird_divisibility(divisor, limit=30):
	print(f"Checking divisibility patterns for {divisor}...\n")
	for n in range(1, limit + 1):
		num_minus = 10**n - 1
		num_plus = 10**n + 1

		if num_minus % divisor == 0:
			print(f"10^{n} - 1 = {num_minus:,}  ÷ {divisor} = {num_minus // divisor:,}")
		if num_plus % divisor == 0:
			print(f"10^{n} + 1 = {num_plus:,}  ÷ {divisor} = {num_plus // divisor:,}")
	print("\nDone.")

find_weird_divisibility(91)
