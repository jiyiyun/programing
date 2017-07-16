branch={
    'spam':1.25,
    'ham':1.99,
    'eggs':0.99
}

print branch.get('spam','bad choice')
print branch.get('bacon','bad choice')