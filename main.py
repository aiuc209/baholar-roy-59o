def baholarni_gpa_ga_aylantir(baholar):
    gpa_baholar = []
    for baho in baholar:
        if baho >= 90:
            gpa_baholar.append(4.0)
        elif baho >= 80:
            gpa_baholar.append(3.0)
        elif baho >= 70:
            gpa_baholar.append(2.0)
        elif baho >= 60:
            gpa_baholar.append(1.0)
        else:
            gpa_baholar.append(0.0)
    return gpa_baholar

baholar = [95, 85, 75, 65, 55]
gpa_baholar = baholarni_gpa_ga_aylantir(baholar)
print(gpa_baholar)
