with open("d4.txt", "r") as f:
    content = f.read().splitlines()
content.append('')

BYR_BIT = 1 << 0
IYR_BIT = 1 << 1
EYR_BIT = 1 << 2
HGT_BIT = 1 << 3
HCL_BIT = 1 << 4
ECL_BIT = 1 << 5
PID_BIT = 1 << 6
CID_BIT = 1 << 7
WRONG_BIT = 1 << 31
MANDATORY_MASK = BYR_BIT | IYR_BIT | EYR_BIT | HGT_BIT | HCL_BIT | ECL_BIT | PID_BIT
MANDATORY_MASK_AND_WRONG = MANDATORY_MASK | WRONG_BIT

valid_passeports_count = 0
current_passeport_fields = 0

def CheckBirthYear(str):
    if len(str) == 4:
        year = int(str)
        if 1920 <= year and year <= 2002:
            return BYR_BIT
    return WRONG_BIT

def CheckIssueYear(str):
    if len(str) == 4:
        year = int(str)
        if 2010 <= year and year <= 2020:
            return IYR_BIT
    return WRONG_BIT

def CheckExpYear(str):
    if len(str) == 4:
        year = int(str)
        if 2020 <= year and year <= 2030:
            return EYR_BIT
    return WRONG_BIT

def CheckHeight(str):
    l = len(str)
    if l == 4:
        inches = int(str[0:2])
        if 59 <= inches and inches <= 76:
            if str[2:4] == "in":
                return HGT_BIT
    elif l == 5:
        cm = int(str[0:3])
        if 150 <= cm and cm <= 193:
            if str[3:5] == "cm":
                return HGT_BIT
    return WRONG_BIT

def CheckHairColor(str):
    if len(str) == 7:
        if str[0] == '#':
            chars = "0123456789abcdefABCDEF"
            is_valid = True
            i = 1
            while is_valid and i < 7:
                is_valid = is_valid and (chars.find(str[i], 0, 22) != -1)
                i += 1
            if is_valid:
                return HCL_BIT
    return WRONG_BIT

def CheckEyeColor(str):
    valid_eyes = {
        "amb": True,
        "blu": True,
        "brn": True,
        "gry": True,
        "grn": True,
        "hzl": True,
        "oth": True,
    }
    if valid_eyes.get(str, False):
        return ECL_BIT
    return WRONG_BIT

def CheckPasseportId(str):
    if len(str) == 9:
        chars = "0123456789"
        is_valid = True
        i = 1
        while is_valid and i < 9:
            is_valid = is_valid and (chars.find(str[i], 0, 10) != -1)
            i += 1
        if is_valid:
            return PID_BIT
    return WRONG_BIT

def CheckCountryId(str):
    return CID_BIT

def Wrong(str):
    return WRONG_BIT

fields = {
    "byr": CheckBirthYear,
    "iyr": CheckIssueYear,
    "eyr": CheckExpYear,
    "hgt": CheckHeight,
    "hcl": CheckHairColor,
    "ecl": CheckEyeColor,
    "pid": CheckPasseportId,
    "cid": CheckCountryId
}

for line in content:
    if len(line) == 0:
        if (current_passeport_fields & MANDATORY_MASK_AND_WRONG) == MANDATORY_MASK:
            valid_passeports_count += 1
        current_passeport_fields = 0
    else:
        entries = line.split(" ")
        for entry in entries:
            bit = fields.get(entry[0:3], Wrong)(entry[4:])
            current_passeport_fields = current_passeport_fields | bit

print("Bons gaulois:", valid_passeports_count)
