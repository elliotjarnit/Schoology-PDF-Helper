from functions import *

init()
clear()

print(Fore.LIGHTBLUE_EX + "Schoology PDF Uploader\n\n" + Style.RESET_ALL)
if platform == "darwin":
    print("You will need to login to your schoology account")
    input("Press " + Fore.RED + "enter" + Style.RESET_ALL + " to continue")
    clear()
elif platform == "win32":
    print("You will need to login to your schoology account")
    input("Press " + Fore.RED + "enter" + Style.RESET_ALL + " to continue")
    clear()
else:
    print(Fore.RED + "Your platform is not supported")
    time.sleep(5)
    exit()

ChromeDriver = os.getcwd() + "/Drivers/chromedriver"

try:
    driver = webdriver.Chrome(ChromeDriver)
except:
    clear()
    printError("Please update google chrome to latest version")
    time.sleep(5)
    exit()

driver.get("https://klschools.schoology.com/api")

try:
    WebDriverWait(driver, 120).until(EC.url_matches("https://klschools.schoology.com/api" or "https://klschools.schoology.com/api#"))
except:
    printError("Took too long")
    time.sleep(5)
    exit()

WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, "edit-current-key")))
publicKey = driver.find_element_by_id("edit-current-key").get_attribute("value")
secretKey = driver.find_element_by_id("edit-current-secret").get_attribute("value")
WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.XPATH, "//button[@class='_1SIMq _2kpZl _3OAXJ _13cCs _3_bfp _2M5aC _24avl _3v0y7 _2s0LQ _3ghFm _3LeCL _31GLY _9GDcm _1D8fw util-height-six-3PHnk util-pds-icon-default-2kZM7 Header-header-button-active-state-3AvBm Header-header-button-1EE8Y Z_KgC fjQuT uQOmx']")))
button1 = driver.find_element_by_xpath("//button[@class='_1SIMq _2kpZl _3OAXJ _13cCs _3_bfp _2M5aC _24avl _3v0y7 _2s0LQ _3ghFm _3LeCL _31GLY _9GDcm _1D8fw util-height-six-3PHnk util-pds-icon-default-2kZM7 Header-header-button-active-state-3AvBm Header-header-button-1EE8Y Z_KgC fjQuT uQOmx']")
button1.click()
WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.XPATH, "//a[normalize-space()='Your Profile']")))
profButton = driver.find_element_by_xpath("//a[normalize-space()='Your Profile']")
userID = profButton.get_attribute("href")
userID = str(userID).replace("https://klschools.schoology.com/user/", "").replace("/info", "")
driver.quit()

print()

print("Pick your image")
while True:
    Tk().withdraw()
    filepath = askopenfilename()
    if filepath == "":
        printError("Please pick a valid image file", True)
    else:
        break

oauth = OAuth1(publicKey, client_secret=secretKey)

try:
    openedImage = Image.open(filepath)
except:
    printError("Invalid image file. Please choose another.", True)

try:
    pdf = img2pdf.convert(openedImage.filename)
except:
    openedImage = openedImage.convert("RGBA")
    imgData = openedImage.getdata()

url = str("https://api.schoology.com/v1/users/" + userID + "/sections")

headers = {"Accept": "application/json", "Content-Type": "application/json"}
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

makeRequest("post", )


