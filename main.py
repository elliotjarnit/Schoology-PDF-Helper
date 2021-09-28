from functions import *
from login import *


init()
clear()

print(Fore.LIGHTBLUE_EX + "Schoology PDF Uploader\n\n" + Style.RESET_ALL)
if platform == "darwin":
    print("You will need to login to your Schoology account")
    input("Press " + Fore.RED + "enter" + Style.RESET_ALL + " to continue")
    clear()
elif platform == "win32":
    print("You will need to login to your Schoology account")
    input("Press " + Fore.RED + "enter" + Style.RESET_ALL + " to continue")
    clear()
else:
    print(Fore.RED + "Your platform is not supported")
    time.sleep(5)
    exit()

login = Login()

print("Pick your image")
while True:
    Tk().withdraw()
    filepath = askopenfilename()
    if filepath == "":
        printError("Please pick a valid image file", True)
    else:
        break

oauth = OAuth1(login.publicKey, client_secret=login.secretKey)

try:
    openedImage = Image.open(filepath)
except:
    printError("Invalid image file. Please choose another.", True)

try:
    pdf = img2pdf.convert(openedImage.filename)
except:
    openedImage = openedImage.convert("RGBA")
    imgData = openedImage.getdata()

url = str("https://api.schoology.com/v1/users/" + login.userID + "/sections")

headers = {"Accept": "application/json"}
getSections = makeRequest("get", url, oauth, headers)
SectionRemaining = str(json.loads(getSections.text)["section"])
clear()
Sections = {}

while True:
    Section1 = str(SectionRemaining).split("\'id\': \'", 1)
    ID = str(Section1[1].split("\'", 1)[0])
    Name = Section1[1].split("course_title\': \'", 1)[1].split("\'", 1)[0]
    SectionRemaining = Section1[1].split("course_title\': \'", 1)[1]
    Sections.update({Name: ID})
    if str(SectionRemaining.find("course_title\'")) == "-1":
        break

print("Courses:\n")

x = 0
for i in Sections.keys():
    print(str(x + 1) + ") " + i)
    x = x + 1

SecAnswer = ifStatementNum("\nPick a course: ")

fixedAnswer = Sections.get(str(list(Sections)[(int(SecAnswer) - 1)]))

getAssignments = makeRequest("get", "https://api.schoology.com/v1/sections/{}/assignments".format(fixedAnswer), oauth, headers)
print(getAssignments.status_code)
AssignmentsRemaining = str(json.loads(getAssignments.text)["assignment"])
Assignments = {}
clear()

while True:
    Section1 = str(AssignmentsRemaining).split("\'id\': ", 1)
    ID = str(Section1[1].split(", ", 1)[0])
    Name = Section1[1].split("title\': \'", 1)[1].split("\'", 1)[0]
    AssignmentsRemaining = Section1[1].split("title\': \'", 1)[1]
    Assignments.update({Name: ID})
    if str(AssignmentsRemaining.find("title\'")) == "-1":
       break

print("Assignments:\n")
x = 0
for i in Assignments.keys():
    print(str(x + 1) + ") " + i)
    x = x + 1

AssigAnswer = ifStatementNum("\nPick an assignment: ")

fixedAnswer2 = Sections.get(str(list(Assignments)[(int(AssigAnswer) - 1)]))


