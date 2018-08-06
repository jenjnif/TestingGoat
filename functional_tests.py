from selenium import webdriver

browser = webdriver.Firefox()

# Adam Ondra has heard about a cool new climbing to-do app
# He goes to check out the homepage
browser.get('http://localhost:8000')
assert 'Django' in browser.title

# He notices the page title and header mention to-do lists
assert 'To-Do' in browser.title

# He is invited to enter a to-do item straight away

# He types "Climb a 9d" into a text box (Adam's speciallity is sport climbing)

# When he hits enter, the page updates, and now the page lists
# "1: Climb a 9d" as an item in a to-do list

# There is still a text box inviting him to add another item
# He enters "Hang out with Alex Megos in Frankenjura" (Adam is very social)

# The page udpates again, and now shows both items on his list

# Adam wonders if the site will remember his list
# Then he sees that the site has generated a unique URL for him -- there is
# some explanatory text to that effect

# He visits that URL - his to-do list is still there

# Satisfied, he goes back to training

browser.quit()
