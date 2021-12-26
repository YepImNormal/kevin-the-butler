import webbrowser
print('Rules')
print('1.Your Name Should Be In First Word Capital')

a = input('Who Are You: ')
if a == 'Krutarth':
  print('ACCESS GRANTED')
  print('Hey Boss, I Was Waiting For Ya')
  b = input('What Do You Want To Do: ')
  if b == 'i want information':
    print('Sure Sir, Wikipedia Will Open Any Second Now')
    Wikipedia = 'www.wikipedia.org'
    webbrowser.open(Wikipedia)
    c = input('Anythin else Sir: ')
    if c == 'i want to watch videos':
      print('Certainly')
      Youtube = 'www.youtube.com'
      webbrowser.open(Youtube)
    if c == 'i want to code':
      print('In A Few MicroSeconds')
      ReplIt = 'https://repl.it/~'
      webbrowser.open(ReplIt)
    if c == 'i want to binge on netflix':
      print('In A Few Microseconds ')
      Netflix = 'https://www.netflix.com/browse'
      webbrowser.open(Netflix)
  if b == 'i want to watch videos':
    print('Sure Sir, Youtube Will Open Any Second Now')
    Youtube = 'www.youtube.com'
    webbrowser.open(Youtube)
    d = input('Anything Else Sir:')
    if d == 'i want information':
      print('Certainly ')
      Wikipedia = 'www.wikipedia.org'
      webbrowser.open(Wikipedia)
    if d == 'i want to code':
      print('In A Few Microseconds')
      ReplIt = 'https://repl.it/~'
      webbrowser.open(ReplIt)
    if d == 'i want to binge on netflix':
      print('in a few seconds ')
      Netflix = 'https://www.netflix.com/browse'
      webbrowser.open(Netflix)
  if b == 'i want to code':
    print('Repl.it will open in 3 seconds...')
    ReplIt = 'https://repl.it/~'
    webbrowser.open(ReplIt)
    e = input('Anything Else Sir: ')
    if e == 'i want to watch videos':
      print('Youtube Is Ready')
      Youtube = 'www.youtube.com'
      webbrowser.open(Youtube)
    if e == 'i want information':
      print('Wikipedia is ready ')
      Wikipedia = 'www.wikipedia.org'
      webbrowser.open(Wikipedia)
    if e == 'i want to binge on netflix':
      print('Netflix is ready')
      Netflix = 'https://www.netflix.com/browse'
      webbrowser.open(Netflix)
      print('Repl.It Is Ready')
      ReplIt = 'https://repl.it/~'
      webbrowser.open(ReplIt)
      f = input('Anything Else Sir: ')
    if f == 'i want to information':
      print('Wikipedia Is Ready')
      Wikipedia = 'www.wikipedia.org'
      webbrowser.open(Wikipedia)
    if f == 'i want to watch videos':
      print('Youtube Is Ready')
      Youtube = 'www.youtube.com'
      webbrowser.open(Youtube)
    if f == 'i want to binge on netflix':
      print('Sure')
      Netflix = 'https://www.netflix.com/browse'
      webbrowser.open(Netflix)

  if b == 'i want to binge on netflix':
    print('Sure Netflix will open... ')
    Netflix = 'https://www.netflix.com/browse'
    webbrowser.open(Netflix)


