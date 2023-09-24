# List/Array
name = []
npm = []
major = []
majorInput = []
yearClass = []
grade = []

# Variables
i = amountGrade = accumulationGrade = 0
necessaryGrade = 4
majorCorrect = True;

# Scholarship start
print("---------------------------------------------------------")
print("SELAMAT DATANG DI PENERIMAAN BEASISWA POLINES TAHUN 2023!")
print("---------------------------------------------------------")
print('')

onProcess = True    # Scholarship current status

# Scholarship process
while onProcess:
    # Input process
    name.append(input("Masukkan nama anda: "))
    npm.append(input("Masukkan NPM anda: "))
    yearClass.append(npm[i][3:5])
    majorInput.append(input("Masukkan jurusan anda: "))

    # Check if the npm is correct
    if len(npm[i]) != 8:
        print("NPM yang dimasukkan salah!")
        name.pop(i)
        npm.pop(i)
        majorInput.pop(i)
    else:
        print()

    # Check if the majorInput is correct
    if len(majorInput[i]) == 2:
        if majorInput[i] == "IA":
            major.append("Teknik Elektro")
            onProcess = False
        elif majorInput[i] == "IB":
            major.append("Teknik Sipil")
            onProcess = False
        elif majorInput[i] == "IC":
            major.append("Teknik Mesin")
            onProcess = False
        elif majorInput[i] == "ID":
            major.append("Akuntansi")
            onProcess = False
        elif majorInput[i] == "IE":
            major.append("Administrasi Bisnis")
            onProcess = False
        else:
            print("Jurusan yang anda masukan salah")
            print("Silahkan coba lagi!")
            name.pop(i)
            npm.pop(i)
            major.pop(i)
            majorInput.pop(i)
            majorCorrect = False
            print('')
    else:
        print("Jurusan yang anda masukan tidak terdaftar di POLINES")
        print("Silahkan coba lagi!")
        name.pop(i)
        npm.pop(i)
        major.pop(i)
        majorInput.pop(i)
        majorCorrect = False
        print('')

# Check if the identity input above is correct
if (len(npm[i]) == 8) & (len(majorInput[i]) == 2) & (majorCorrect == True):
    print("------------- IDENTITAS DIRI -------------")
    print("Nama: ", name[i])
    print("NPM: ", npm[i])
    print("Jurusan: ", major[i])
    print('')
    print("Masukkan nilai-nilai anda: ")

    # Grade input
    for j in range(1, necessaryGrade + 1, 1):
        print("Nilai [", j, "] = ")
        grade.append(int(input()))
        amountGrade += 1

    print('')

    # Check if the grade input is correspond to the scholarship requisite
    if len(grade) == necessaryGrade:
        for k in range(0, len(grade), 1):
            accumulationGrade += grade[k]

        if ((accumulationGrade / necessaryGrade) >= 90) & ((accumulationGrade / necessaryGrade) <= 100):
            print("Selamat! Untuk", name[i], "dengan", npm[i], "dari jurusan", major[i], "angkatan", yearClass[i])
            print("Anda Meraih Beasiswa dari POLINES")
            print("Jumlah rata-rata nilai:", accumulationGrade / necessaryGrade)
            onProcess = False
        else:
            print("Maaf, jumlah rata-rata nilai anda tidak memenenuhi syarat\n")
            onProcess = False

print("------------------------ PROGRAM SELEKSI BEASISWA SUKSES ------------------------")      # Scholarship end