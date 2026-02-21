file=open('youtube.text','w')

try:
   file.write('chai aur code')
except:
    print('something went wrong') 
finally:
   file.close()




with open('youtube.text') as file:
   file.write('chai aur python')

