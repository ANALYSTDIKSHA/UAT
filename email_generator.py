emails_generated = []
def generate_email(first_name, last_name, company_name):
    email = (first_name.lower() + "." + last_name.lower() + "@" + company_name + ".com")
    return email

user = "yes"
while user.lower() != "no":
    
    a = input("Enter your first name:")
    b = input("Enter your last name:")
    c = input("Enter your company name:")
    print(generate_email(a,b,c))
    emails_generated.append(email)
    user =input("Do you want to generate another emails (yes/no) : ")
    
print("generated emails are:- " , emails_generated)


