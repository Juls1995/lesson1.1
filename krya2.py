kolichestvo_vipolnennih_DZ = 12
kolichestvo_zatrachennih_chasov = 1.5
nazvanie_kursa = 'Python'
vremya_na_odno_zadanie = float(kolichestvo_zatrachennih_chasov) / int(kolichestvo_vipolnennih_DZ)
print(nazvanie_kursa,", всего задач:",kolichestvo_vipolnennih_DZ,"; затрачено часов:",kolichestvo_zatrachennih_chasov, "; среднее время выполнения:",vremya_na_odno_zadanie, "часа")