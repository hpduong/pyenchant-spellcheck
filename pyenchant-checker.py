import enchant
from enchant import DictWithPWL
from enchant.checker import SpellChecker



a = "backk huurts lymphama infurction angioadema corunary artury"

my_dict = DictWithPWL("en_US","479kwords.txt")
my_checker = SpellChecker(my_dict)

#this is the original built-in dict only
#chkr = enchant.checker.SpellChecker("en_US")
#chkr.set_text(a)

my_checker.set_text(a)

for err in my_checker:
    print err.word
    sug = err.suggest()[0]
    err.replace(sug)

c = my_checker.get_text()#returns corrected text

print "\n"
print a

print "\n"

print c
