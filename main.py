import csv

# abrindo o arquivo .csv
lst = list(csv.DictReader(open('6 - June/SQDF_GCD_LATAM_VEHICLE_INFO_Jun.csv')))
print(lst[0])
