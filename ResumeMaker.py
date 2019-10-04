Categories = ["AI", "CG", "SE", "DB", "EC", "PM", "PL", "API", "AL", "MC", "CC", "OS", "FT", "PT"]
Cat_Full = ["Artificial Intelligence", "Computer Graphics", "Software Engineering", "DataBases", "Error Correction",
			"Project Management", "Programming Languages", "APIs", "Algorithms", "Micro-Controllers", "Cloud Computing",
			"Operating Systems", "Full Time", "Part Time"]
class Education:
	def __init__(self,deg,field,sch,op,mon,yr,gpa=None):
		self.degree = deg;
		self.field = field;
		self.school = sch;
		self.option = op;
		self.graduation_month = mon;
		self.graduation_year = yr;
		self.GPA = gpa;

class Award:
	def __init__(self,title,awardee,date):
		self.title = title;
		self.awardee = awardee;
		self.date = date;

class Skill:
	def __init__(self,title, cat):
		self.title = title;
		self.category = cat;

class Concept:
	def __init__(self,title, cat):
		self.title = title;
		self.category = cat;

class Experience:
	def __init__(self, name, org, year, desc, cat, isActive = False):
		self.name = name;
		self.organization = org;
		self.year = year;
		self.description = desc;
		self.category = cat;
		self.isActive = isActive;

class Resume:
	def __init__(self):
		print("Resume was created");
		self.first_name = None;
		self.middle_name = None;
		self.last_name = None;
		self.phone = None;
		self.email = None;
		self.website = None;
		self.education = [];
		self.skills = [];
		self.concept = [];
		self.awards = [];
		self.experiences = [];
		
	def set_head(self,fn,mn,ln,pn,em,ws):
		self.first_name = fn;
		self.middle_name = mn;
		self.last_name = ln;
		self.phone = pn;
		self.email = em;
		self.website = ws;
		print("Head was set.");

	def add_education(self,edu):
		self.education.append(edu);
		print("Education was added.");

	def add_awards(self,award):
		self.awards.append(award);
		print("Award was added.");

	def add_skills(self,skill):
		self.skills.append(skill);
		print("Skill was added.");

	def add_experiences(self,experience):
		self.experiences.append(experience);
		print("Experience was added.");

	def add_concept(self,concept):
		self.concept.append(concept);
		print("Concept was added.");

	def print_resume(self,cat):
		print("Here is your resume for "+cat+":");

	def make_JSON(self,cat, path):
		print("Saving the JSON object for category "+cat+" at the path:",path);

	def save_resume(self,cat,path):
		print("Formatting and saving your Resume for "+cat+" in:",path);
		print("Saved.");

def main():
	myResume = Resume();
	myEducation = [];
	myAward = [];
	mySkills = [];
	myConcepts = [];
	myExperiences = [];

	myEducation.append(Education("BS","Computer Science","Oregon State University", "Systems", "Spring", 2017))
	myEducation.append(Education("MS","Computer Science","Oregon State University", "Machiene Learning", "Spring", 2019,3.79))

	myAward.append(Award("Ontario Scholar","Canadian Minister of Education Laurel Broten", "7th December 2012"));

	mySkills.append(Skill("C",["PL"]));
	mySkills.append(Skill("C++",["PL"]));
	mySkills.append(Skill("C#",["PL"]));
	mySkills.append(Skill("Java",["PL"]));
	mySkills.append(Skill("PHP",["PL"]));
	mySkills.append(Skill("ASM (6502, x86, ARM, AVR)",["PL"]));
	mySkills.append(Skill("Python",["PL"]));
	mySkills.append(Skill("Bash",["PL"]));
	mySkills.append(Skill("SQL",["PL"]));
	mySkills.append(Skill("Pytorch",["API"]));
	mySkills.append(Skill("OpenCV",["API"]));
	mySkills.append(Skill("Tensorflow",["API"]));
	mySkills.append(Skill("SKLearn",["API"]));
	mySkills.append(Skill("OpenGL",["API"]));
	mySkills.append(Skill("GLSL",["API"]));
	mySkills.append(Skill("GLM",["API"]));
	mySkills.append(Skill("OpenMP",["API"]));

	myConcepts.append(Concept("Machine Learning",["AI", "SE"]));
	myConcepts.append(Concept("Deep Learning",["AI", "SE"]));
	myConcepts.append(Concept("Computer Vision",["AI", "CG", "SE"]));
	myConcepts.append(Concept("Image Processing",["AI", "CG"]));
	myConcepts.append(Concept("Agile Scrum SEM",["SE"]));
	myConcepts.append(Concept("Graph Theory",["AL"]));
	myConcepts.append(Concept("Error Correction",["EC", "SE", "AI"]));
	myConcepts.append(Concept("Embedded Programming",["MC", "SE"]));
	myConcepts.append(Concept("Digital Logic",["MC", "SE"]));

	myExperiences.append(Experience("Senior software engineering GTA","Oregon State University", 2018, 
								 "Oregon State university’s Capstone program is a 9 month course during which over 250 students get involved in a professional software engineering process before they graduate. The projects which students work on are used in consumer level releases and  presented by many high ranking companies in industry such as Intel, HP, Nvidia  and more. GTAs for this course are the acting project managers for over 10 different groups with diverse range of skills from embedded level programming and IOT to high level deep learning applications.",
								["SE", "PM", "PT"]));
	myExperiences.append(Experience("Tensorflow WYSIWYG","Oregon State University", 2017, 
								 "Developed visual programming environment and interpreter for Google Tensorflow API. This compiler converts UML diagrams into working Tensorflow™ python scripts. This project was successfully produced and documented through a waterfall software engineering method within a span of 9 months. The project’s Client was Professor Fuxin Li under the oregon state university Capstone program. Find out more at my website.",
								["AI", "PL", "SE", "PM", "AL", "PT"]));
	myExperiences.append(Experience("NASA Life in Space challenge","Oregon State University", 2017, 
								 "With a team of engineers developed a tool capable of performing in microgravity. Selected by NASA, HP and Intel® Design Challenge: Life in Space program as a finalist. The challenge was to develop a tool in order to improve the quality of life in International Space Station (ISS). The design involved a tape dispenser with retractable blade, designed to ensure safety of ISS astronauts in microgravity environment. This tool was designed, developed, prototyped and tested within the course of 10 weeks. The tool does not need to be shipped to ISS since it was designed to be completely 3D printable using the ISS’s on-board 3D printer. On behalf of OSU the team became one of the finalists in the competition.",
								["PM", "PT"]));
	myExperiences.append(Experience("SandBox","Oregon State University", 2016, 
								 "Developed a computer vision program with OpenGL, OpenCV and RealSense™ technology in order to generate a topographical map of a sandbox and display a color pattern on the sand using a projector. Furthermore, this project uses machine learning algorithms in order to detect and remove noise from the camera output to enhance the appearance and reliability of the projection. The project is now being displayed at information office at Kelly engineering center in Oregon State University. ",
								["AI", "PL", "SE", "PM", "AL", "PT"]));
	myExperiences.append(Experience("TekFly","Oregon State University", 2015, 
								 "Worked on a UAV that takes advantage of intel® Edison™ Microprocessor to send commands to its flight control module. This UAV carries an Intel RealSense™ Camera. Furthermore, an ML and CV application was developed for stabilization and flight control. The drone is capable of autonomous navigation in a 3D environment.",
								["AI", "PL", "SE", "PM", "AL", "PT"]));
	myExperiences.append(Experience("Virtual Gimbal","Oregon State University", 2015, 
								 "Developed an Augmented Reality version of labyrinth game using F200 prototype camera and a small projector. The projector projects the game field and the ball and the camera calculates the angle of the plane held under the camera to animate the game. The game was developed using Unity engine and it was capable of simulation different friction coefficients and the acceleration due to gravity in different planets.",
								["AI", "PL", "SE", "PM", "AL", "PT"]));
	myExperiences.append(Experience("Virtual Tower Defense","Oregon State University", 2014, 
								 "Created a demo in form of a tower defense game as part of an Intel® research. The user participates in the game by placing physical square blocks of different colors and sizes on a whiteboard that has an overhead projector and camera. The camera picks the size, color and position of those blocks and turns them into towers required by the tower defense game by bringing them to life. This project was developed for Intel® Realsense™ and is currently in their toolkit.",
								["AI", "PL", "SE", "PM", "AL", "PT"]));
	myExperiences.append(Experience("Software Engineer","Microsoft", 2019, 
								 "Microsoft Core Services Engineering and Operations. Working closely with development on PowerBI, Azure Data Factory, Dat Bricks, Data Lake, Data Warehouse, and Analysis Services.",
								["SE", "PM", "DB", "PL", "CC", "FT"], True));
	myExperiences.append(Experience("JAI Tool-Chain","Oregon State University", 2019, 
								 "This was produced to streamline the process of setting up tools needed for Artificial Intelligence and Computer Graphic applications on Jetson SoC family of hardwares.",
								["AI", "PL", "SE", "PM","CG", "OS", "CC", "FT"]));
	myExperiences.append(Experience("Tank 2019","Oregon State University", 2019, 
								 "This project started as a fun experiment with OpenGL and turned into something much bigger. Everything from the models to the engine was developed from scratch. This program takes advantage of GLSL, GLM, OpenMP and OpenAL. Each revision introduced my features in an Agile fashion and it could be found online free to download.",
								["AI", "PL", "SE", "PM","CG", "FT"]));
	myExperiences.append(Experience("Capstone Senior Software Engineering Instructor","Oregon State University", 2019, 
								 "",
								["SE", "PM", "PT"]));
	myExperiences.append(Experience("OSU EECS Inventory and Databases","Oregon State University", 2014, 
								 "EECS department at OSU has a large inventory of electronic components that are available for use in various EECS cources. These components were previously stored in a localized spreadsheet accessed by several people. The inventory process was long, tedious and prone to many errors. Some of these errors often lead to re-inventorying the components. A tool was proposed that moved this inventory into an online database. Securtity procedures were set into place to ensure the safety of the system. Furthermore, barcodes and QRCodes were designed to improve the integrity of the inventory between different counting events. This system ended up being adopted and greatly improved the efficiency and performance of EECS instructors and students. This tool also saved hours of time for the EECS hardware store personel in inventory counting and tracking of the electronic components.",
								["PL", "SE", "PM", "DB", "PT"]));

	myResume.set_head("Behnam", "" , "Saeedi", 8186993803, "Behnam.Saeedi.m.sc@gmail.com", "None.com");
	
	for E in myEducation:
		myResume.add_education(E);
	
	for A in myAward:
		myResume.add_awards(A);
	
	for S in mySkills:
		myResume.add_skills(S);

	for C in myConcepts:
		myResume.add_concept(C)

	for E in myExperiences:
		myResume.add_experiences(E);

	myResume.print_resume("AI");
	myResume.save_resume("AI","PATH/TO/FILE");
	myResume.make_JSON("AI","PATH/TO/FILE");

	print("Done.")

if __name__== "__main__":
	main()