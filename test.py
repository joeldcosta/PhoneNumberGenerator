import random
import sys

countrycode = sys.argv[1]
three_digits = sys.argv[2]


def random_sample(count, start, stop, step=1):

  def gen_random():
    while True:
      yield random.randrange(start, stop, step)

  def gen_n_unique(source, n):
    seen = set()
    seenadd = seen.add
    for i in (i for i in source() if i not in seen and not seenadd(i)):
      yield i
      if len(seen) == n:
        break

  return [
      i for i in gen_n_unique(gen_random,
                              min(count, int(abs(stop - start) / abs(step))))
  ]


def get_number_with_digits(number, desired_digits):
  str_number = str(number)
  return int(str_number[:desired_digits])


times = 100
total_digits_start = 8888888888
total_digits_end = 9999999999
desired_digits = 7

result_start = get_number_with_digits(total_digits_start, desired_digits)
result_end = get_number_with_digits(total_digits_end, desired_digits)

mobile = "New_mobile.txt"

def input_number(countrycode, three_digits):
  g = open(mobile, "a+")
  g.writelines(f'+{countrycode}{three_digits}')
  g.writelines(f'\n+{countrycode}{three_digits}'.join(
      map(str, random_sample(times, result_start, result_end))))
  g.close()


#input_number(91,123)
input_number(sys.argv[1], sys.argv[2])
##################################################
from time import gmtime, strftime
import os

name = "qwertx"
country_code = ""
starting_num = ""

# This will read the mobile numbers
mobile = "New_mobile.txt"
f = open(mobile, "r")

contact = name + "_contact_list.vcf"
g = open(contact, "w")

lines = f.readlines()

# Function to get total line number of a text file
def file_len(fname):
  with open(fname) as h:
    for i, l in enumerate(h):
      pass
  return i + 1


print("Total line number is:- ", file_len(mobile))

count_from = 1

# Generates output to contact_list
for i in range(file_len(mobile)):
  g.writelines("BEGIN:VCARD\n")
  g.writelines("VERSION:2.1\n")
  g.writelines("N:;" + name + "%d" % (i + count_from))
  g.writelines(";;;\n")
  g.writelines("FN:" + name + "%d" % (i + count_from))
  g.writelines("\n")
  g.writelines("TEL;CELL:")
  g.writelines("" + country_code + starting_num + lines[i] + "\n")
  g.writelines("END:VCARD\n")

#Closes the file after use.
#If not used it will show "File is still running
# even after you try to close it"
g.close()
f.close()
os.remove(mobile)
print("Raw File Removed!")
