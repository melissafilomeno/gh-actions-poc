import argparse
import sys

def main() -> int:
  parser = argparse.ArgumentParser()
  parser.add_argument('--input1')
  args = parser.parse_args()

  print("input1 = {}".format(args.input1))
  print("""

	line1
	line2
	
	line3
	line4

  """)
  return 0

if __name__ == '__main__':
  sys.exit(main())
