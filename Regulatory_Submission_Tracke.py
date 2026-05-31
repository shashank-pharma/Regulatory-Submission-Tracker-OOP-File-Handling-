from datetime import date

class Submission:
    def __init__(self,submission_id,drug_name,applicant,submission_type,status,date):
        self.submission_id = submission_id
        self.drug_name = drug_name
        self.applicant = applicant
        self.submission_type = submission_type
        self.status = status
        self.date = date

    def __str__(self):
        return (
            f"Submission ID: {self.submission_id}\n"
            f"Drug Name: {self.drug_name}\n"
            f"Applicant: {self.applicant}\n"
            f"Submission Type: {self.submission_type}\n"
            f"Status: {self.status}\n"
            f"Date: {self.date}"
        )

    def save_to_files(self):
        with open("submission.txt","a") as f:

            f.write(
                    f"{self.submission_id}, "
                    f"{self.drug_name}, "
                    f"{self.applicant}, "
                    f"{self.submission_type}, "
                    f"{self.status}, "
                    f"{self.date}\n"
                    )

    def is_approved(self):
        return self.status == "Approved"


s1 = Submission("S001",
"vit_c" ,
"XYX" ,
"FDA" ,
"Approved" ,
str(date.today()))

s2 = Submission(
"S002",
"Insulin Glargine",
"Novo Nordisk",
"NDA",
"Pending",
str(date.today())
)

s3 = Submission(
"S003",
"Paracetamol IV",
"Sun Pharma",
"IND",
"Rejected",
str(date.today())
)

s4 = Submission(
"S004",
"Atorvastatin",
"Torrent Pharma",
"ANDA",
"Approved",
str(date.today())
)

submissions = [s1, s2, s3, s4]

for submission in submissions:
    submission.save_to_files()

print("FILE SAVED\n")

print("APPROVED SUBMISSIONS\n")

with open("submission.txt","r") as f:
    lines = f.readlines()

    for line in lines:
        data = line.strip().split(", ")
        if data[4] == "Approved":
            print(line)






