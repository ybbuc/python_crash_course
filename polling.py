favorite_languages = {
    'jen': 'python',
    'sarah': 'c',
    'edward': 'ruby',
    'phil': 'python',
}

possible_interviewees = ['jen', 'phil', 'jill']

for interviewee in possible_interviewees:
    if interviewee in favorite_languages:
        print(f"Thank you for participating already, {interviewee.title()}!")
    else:
        print(f"Please take the poll, {interviewee.title()}.")
