
def Resolve(do_print = False):

    with open('d04.txt', 'r') as f:
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
                if str[2:4] == 'in':
                    return HGT_BIT
        elif l == 5:
            cm = int(str[0:3])
            if 150 <= cm and cm <= 193:
                if str[3:5] == 'cm':
                    return HGT_BIT
        return WRONG_BIT

    HAIR_CHARS = '0123456789abcdefABCDEF'
    def CheckHairColor(str):
        if len(str) == 7:
            if str[0] == '#':
                for i in range(1, 7):
                    if HAIR_CHARS.find(str[i], 0, 22) == -1:
                        return WRONG_BIT
                return HCL_BIT
        return WRONG_BIT

    VALID_EYES = {
        'amb': True,
        'blu': True,
        'brn': True,
        'gry': True,
        'grn': True,
        'hzl': True,
        'oth': True,
    }
    def CheckEyeColor(str):
        return ECL_BIT if VALID_EYES.get(str, False) else WRONG_BIT

    PASSID_CHARS = '0123456789'
    def CheckPasseportId(str):
        if len(str) == 9:
            for i in range(1, 9):
                if PASSID_CHARS.find(str[i], 0, 10) == -1:
                    return WRONG_BIT
            return PID_BIT
        return WRONG_BIT

    def CheckCountryId(str):
        return CID_BIT

    def Wrong(str):
        return WRONG_BIT

    FIELDS = {
        'byr': (BYR_BIT, CheckBirthYear),
        'iyr': (IYR_BIT, CheckIssueYear),
        'eyr': (EYR_BIT, CheckExpYear),
        'hgt': (HGT_BIT, CheckHeight),
        'hcl': (HCL_BIT, CheckHairColor),
        'ecl': (ECL_BIT, CheckEyeColor),
        'pid': (PID_BIT, CheckPasseportId),
        'cid': (CID_BIT, CheckCountryId),
    }

    valid1 = 0
    fields1 = 0
    valid2 = 0
    fields2 = 0
    for line in content:
        if len(line) == 0:
            if (fields1 & MANDATORY_MASK_AND_WRONG) == MANDATORY_MASK:
                valid1 += 1
            if (fields2 & MANDATORY_MASK_AND_WRONG) == MANDATORY_MASK:
                valid2 += 1
            fields1 = 0
            fields2 = 0
        else:
            entries = line.split(' ')
            for entry in entries:
                field_bit, field_fn = FIELDS.get(entry[0:3], (WRONG_BIT, Wrong))
                fields1 = fields1 | field_bit
                fields2 = fields2 | field_fn(entry[4:])

    if do_print:
        print('Passeports gaulois 1:', valid1)
        print('Passeports gaulois 2:', valid2)


# #############################################################################
if __name__ == '__main__':
    Resolve(True)
    # Results with given input:
    #   1: 242
    #   2: 186
