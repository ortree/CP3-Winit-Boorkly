import csv

with open('Exercise86_Winit_B.csv', 'w') as csvfile:
    filewriter = csv.writer(csvfile)
    filewriter.writerow(['FriendName','Movie','Pet'])
    filewriter.writerow(['Johny', 'Thor', 'Cat'])
    filewriter.writerow(['Winie', 'Ju-on', 'Dog'])
    filewriter.writerow(['Magalo', 'The Matrix', 'Bear'])
    filewriter.writerow(['Infinity', 'Avenger', 'Lizard'])