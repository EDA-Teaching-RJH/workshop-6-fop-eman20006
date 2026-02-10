sample_bay = ["Basalt", "Silica", "Iron", "Dust"]
# print(sample_bay[0]) prints basalt
# print(sample_bay[-1]) prints dust
#print(len(sample_bay)) #prints number of samples = 4 currently

for i in range(len(sample_bay)):
    print(f"Transmitting data for: {sample_bay[i]}")

new_findings = []
for i in range (3):
    finding = input(f"Please enter a new rock type:{i + 1}: ")
    new_findings.append(finding)
print("You entered: ", new_findings,)

answ = input("Would you like to remove an item from your previous list? ")

if answ == "yes":
   rem =  input(f"Which item would you like to get rid of? {sample_bay}")

if rem == "Basalt":
    sample_bay.remove("Basalt")
    print(sample_bay)

if rem == "Silica":
    sample_bay.remove("Silica")
    print(sample_bay)
if rem == "Iron":
    sample_bay.remove("Iron")
    print(sample_bay)

if rem == "Dust":
    sample_bay.remove("Dust")
    print(sample_bay) 

else:
    print(f"Ok, here is a list of your samples: {sample_bay}")
