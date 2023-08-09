"""A Prototype for learning about json serialization in Python"""

# accounts is a list of lists
# each inner list contains a string account name and an integer account balance

def main():
  accounts = [['bob', 0], ['josephine', 0], ['ryan', 0]]
  print(accounts)
  write_accounts_to_json(accounts)
  accounts_reloaded = read_accounts_from_json()
  print(accounts_reloaded)
  assert accounts_reloaded == accounts


def write_to_json(accounts):
  pass  # todo


def accounts_reloaded = read_accounts_from_json():
  pass  # todo


if __name__ == '__main__':
  main()

