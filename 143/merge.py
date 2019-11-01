from collections import defaultdict


NOT_FOUND = "Not found"

group1 = {'tim': 30, 'bob': 17, 'ana': 24}
group2 = {'ana': 26, 'thomas': 64, 'helen': 26}
group3 = {'brenda': 17, 'otto': 44, 'thomas': 46}


def get_person_age(name):
   if isinstance(name, str):
      name = name.lower()
      groups = [group3, group2, group1]
      d = defaultdict(list)
      for dic in groups:
         for k, v in dic.items():
            d[k].append(v)
      if name in d:
         return d[name][0]
   return NOT_FOUND



