IC_PATTERNS = ["KAD", "PENGELANAN", "IDENTITY", "MYKAD"]
DRIVING_PATTERN = ["DRIVING", "LICENSE", "LESEN", "MEMANDU", "KELAS", "CLASS", "TEMPOH", "VALIDITY",
                   "ALAMAT", "ADDRESS"]
PASSPORT_PATTERNS = ["PASSPORT", "JENIS", "TYPE", "KOD", "NEGARA", "COUNTRY", "CODE", "JANTINA", "SEX",
                     "TEMPAT", "LAHIR", "PLACE", "OF", "BIRTH", "TINGGI", "HEIGHT", "ISSUE", "EXPIRY", "ISSUING", "OFFICE"]

IC_NUMBER_REGREX = "^(\\d\\d\\d\\d\\d\\d)-(\\d\\d)-\\d\\d\\d\\d$"
DRIVING_IC_NUMBER_REGREX = "^\\d\\d\\d\\d\\d\\d\\d\\d\\d\\d\\d\\d$"

PASSPORT_DATE_REGREX = "\\d\\d\\s(?:JAN|FEB|MAR|APR|MAY|JUN|JUL|AUG|SEP|OCT|NOV|DEC)\\s\\d{4}"
DRIVING_DATE_REGREX = "^(0?[1-9]|[12][0-9]|3[01])/(0?[1-9]|1[0-2])/\\d\\d\\d\\d$"
