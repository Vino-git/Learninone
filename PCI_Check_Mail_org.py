import os, sys
import win32com.client
import re

def cdo_iter (cdo_collection):
  item = cdo_collection.GetFirst ()
  while item:
    yield item
    item = cdo_collection.GetNext ()

def cdo_walk (folder):
  try:
    folders = cdo_iter (folder.Folders)
  except AttributeError:
    folders = []
  try:
    items = cdo_iter (folder.Messages)
  except AttributeError:
    items = []

  yield folder, folders, items

  for subfolder in folders:
    for r in cdo_walk (subfolder):
      yield r

def card_check_digit(card):
  card_even=[]
  card_odd=[]
  card_number = card
  card_list_var = list(card_number)
  card_list = map(lambda x:int(x),card_list_var)
  #print card_list
  card_to_test = card_list[0:15]
  card_last = card_list[-1]
  card_to_test.reverse()
  card_to_test.insert(0,0)
  map(lambda x,y:card_even.append(int(x)) if y % 2 == 0 else card_odd.append(int(x)),card_to_test, range(len(card_to_test)))
  card_odd_2 = map(lambda x: int(x)*2,card_odd)
  card_over_nine = map(lambda x: x if x < 9 else (x - 9), card_odd_2)
  tot_odd = sum(card_over_nine)
  tot_even = sum(map(lambda x: int(x),card_even))
  final = tot_odd+tot_even
  last_val = 10 - final % 10
  if last_val==card_last:
    return True
  else: 
    return False

class x_found (Exception):
  pass
  
if __name__ == '__main__':
  outlook = win32com.client.gencache.EnsureDispatch ("Outlook.Application")
  session= outlook.GetNamespace("MAPI")
  bins = raw_input("Enter the Bin with comma separated").split(',')
  try:
    for i in range (session.Folders.Count):
      info_store = session.Folders[i+1]
      #
      # Ignore Public Folders which is very big
      #
      if info_store.Name == "vinoth.durairaj@wirecard.com": 
      #print "Searching", info_store.Name
      
        for folder, folders, items in cdo_walk (info_store):
          #print str(folder.Name)
          for item in folder.Items:
            for jbin in bins:
              #print "i am inside"
              #print jbin
              if re.search(str(jbin)+'[0-9][0-9][0-9][0-9][0-9][0-9][0-9][0-9][0-9][0-9]',item.Body):
                ful_card = re.search(str(jbin)+'[0-9][0-9][0-9][0-9][0-9][0-9][0-9][0-9][0-9][0-9]',item.Body).group(0)
              #print ful_card.group(0)
                check_digit = card_check_digit(ful_card)
                if check_digit:
                  print ful_card
                  print item.Subject
                check_digit = False
            #break
          #if folder.Name == "SysAdmin":
            #print "am i inside"
            #for item in items:
              #print item.Subject
          #raise x_found
  
  except x_found:
    pass

