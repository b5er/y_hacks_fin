import pandas as pd

reg1 = open("regions/region_1.csv", "w")
reg2 = open("regions/region_2.csv", "w")
reg3 = open("regions/region_3.csv", "w")
reg4 = open("regions/region_4.csv", "w")
reg5 = open("regions/region_5.csv", "w")
reg6 = open("regions/region_6.csv", "w")
reg7 = open("regions/region_7.csv", "w")
reg8 = open("regions/region_8.csv", "w")
reg9 = open("regions/region_9.csv", "w")
reg10 = open("regions/region_10.csv", "w")
reg11 = open("regions/region_11.csv", "w")
reg12 = open("regions/region_12.csv", "w")

r1 = False
r2 = False
r3 = False
r4 = False
r5 = False
r6 = False
r7 = False
r8 = False 
r9 = False
r10 = False
r11 = False
r12 = False

count1 = 0
count2 = 0
count3 = 0
count4 = 0
count5 = 0
count6 = 0
count7 = 0
count8 = 0
count9 = 0
count10 = 0
count11 = 0
count12 = 0

for i in range(1, 21):
	dataset = pd.read_csv('feeds/feed' + str(i) + '.csv')

	#iterate through states
	iterr = 0
	
	for state in dataset['emp_state']:

	# RegionNumber,ID,State,Address,Bankcrupt

	# Region 1 - CT, ME, MA, NH, RI, VT
		if state == "CT" or state == "ME" or state == "MA" or state == "NH" or state == "RI" or state == "VT":
			if r1 == False:
				reg1.write("1\n")
				r1 = True
			reg1.write(str(dataset.iloc[iterr, 1]) + ",")
			reg1.write(str(dataset.iloc[iterr, 2]) + ",")
			reg1.write(str(dataset.iloc[iterr, 5]) + ",")
			reg1.write(str(dataset.iloc[iterr, 0]) + ",")
			reg1.write(str(state) + ",")
			reg1.write(str(dataset.iloc[iterr, 6]) + ",")
			if i < 20:
				reg1.write(str(dataset.iloc[iterr, -1]) + "\n")
			else:
				reg1.write(str(dataset.iloc[iterr, -1]))

			if str(dataset.iloc[iterr, -1]) == "Y":
				count1 = count1 + 1

	# Region 2 - NJ, NY
		if state == "NJ" or state == "NY":
			if r2 == False:
				reg2.write("2\n")
				r2 = True
			reg2.write(str(dataset.iloc[iterr, 1]) + ",")
			reg2.write(str(dataset.iloc[iterr, 2]) + ",")
			reg2.write(str(dataset.iloc[iterr, 5]) + ",")
			reg2.write(str(dataset.iloc[iterr, 0]) + ",")
			reg2.write(str(state) + ",")
			reg2.write(str(dataset.iloc[iterr, 6]) + ",")
			if i < 20:
				reg2.write(str(dataset.iloc[iterr, -1]) + "\n")
			else:
				reg2.write(str(dataset.iloc[iterr, -1]))

			if str(dataset.iloc[iterr, -1]) == "Y":
				count2 = count2 + 1

	# Region 3 - DE, DC, MD, PA, VA, WV
		if state == "DE" or state == "DC" or state == "MD" or state == "PA" or state == "VA" or state == "WV":
			if r3 == False:
				reg3.write("3\n")
				r3 = True
			reg3.write(str(dataset.iloc[iterr, 1]) + ",")
			reg3.write(str(dataset.iloc[iterr, 2]) + ",")
			reg3.write(str(dataset.iloc[iterr, 5]) + ",")
			reg3.write(str(dataset.iloc[iterr, 0]) + ",")
			reg3.write(str(state) + ",")
			reg3.write(str(dataset.iloc[iterr, 6]) + ",")
			if i < 20:
				reg3.write(str(dataset.iloc[iterr, -1]) + "\n")
			else:
				reg3.write(str(dataset.iloc[iterr, -1]))
			if str(dataset.iloc[iterr, -1]) == "Y":
				count3 = count3 + 1

	# Region 4 - AL, FL, GA, KY, MS, NC, SC, TN
		if state == "AL" or state == "FL" or state == "GA" or state == "KY" or state == "MS" or state == "NC" or state == "SC" or state == "TN":
			if r4 == False:
				reg4.write("4\n")
				r4 = True
			reg4.write(str(dataset.iloc[iterr, 1]) + ",")
			reg4.write(str(dataset.iloc[iterr, 2]) + ",")
			reg4.write(str(dataset.iloc[iterr, 5]) + ",")
			reg4.write(str(dataset.iloc[iterr, 0]) + ",")
			reg4.write(str(state) + ",")
			reg4.write(str(dataset.iloc[iterr, 6]) + ",")
			if i < 20:
				reg4.write(str(dataset.iloc[iterr, -1]) + "\n")
			else:
				reg4.write(str(dataset.iloc[iterr, -1]))
			if str(dataset.iloc[iterr, -1]) == "Y":
				count4 = count4 + 1

	# Region 5 - IL, IN, MI, MN, OH, WI
		if state == "IL" or state == "IN" or state == "MI" or state == "MN" or state == "OH" or state == "WI":
			if r5 == False:
				reg5.write("5\n")
				r5 = True
			reg5.write(str(dataset.iloc[iterr, 1]) + ",")
			reg5.write(str(dataset.iloc[iterr, 2]) + ",")
			reg5.write(str(dataset.iloc[iterr, 5]) + ",")
			reg5.write(str(dataset.iloc[iterr, 0]) + ",")
			reg5.write(str(state) + ",")
			reg5.write(str(dataset.iloc[iterr, 6]) + ",")
			if i < 20:
				reg5.write(str(dataset.iloc[iterr, -1]) + "\n")
			else:
				reg5.write(str(dataset.iloc[iterr, -1]))
			if str(dataset.iloc[iterr, -1]) == "Y":
				count5 = count5 + 1

	# Region 6 - AR, LA, NM, OK, TX
		if state == "AR" or state == "LA" or state == "NM" or state == "OK" or state == "TX":
			if r6 == False:
				reg6.write("6\n")
				r6 = True
			reg6.write(str(dataset.iloc[iterr, 1]) + ",")
			reg6.write(str(dataset.iloc[iterr, 2]) + ",")
			reg6.write(str(dataset.iloc[iterr, 5]) + ",")
			reg6.write(str(dataset.iloc[iterr, 0]) + ",")
			reg6.write(str(state) + ",")
			reg6.write(str(dataset.iloc[iterr, 6]) + ",")
			if i < 20:
				reg6.write(str(dataset.iloc[iterr, -1]) + "\n")
			else:
				reg6.write(str(dataset.iloc[iterr, -1]))
			if str(dataset.iloc[iterr, -1]) == "Y":
				count6 = count6 + 1


	# Region 7 - IA, KS, MO, NE
		if state == "IA" or state == "KS" or state == "MO" or state == "NE":
			if r7 == False:
				reg7.write("7\n")
				r7 = True
			reg7.write(str(dataset.iloc[iterr, 1]) + ",")
			reg7.write(str(dataset.iloc[iterr, 2]) + ",")
			reg7.write(str(dataset.iloc[iterr, 5]) + ",")
			reg7.write(str(dataset.iloc[iterr, 0]) + ",")
			reg7.write(str(state) + ",")
			reg7.write(str(dataset.iloc[iterr, 6]) + ",")
			if i < 20:
				reg7.write(str(dataset.iloc[iterr, -1]) + "\n")
			else:
				reg7.write(str(dataset.iloc[iterr, -1]))
			if str(dataset.iloc[iterr, -1]) == "Y":
				count7 = count7 + 1


	# Region 8 - CO, MT, ND, SD, UT, WY
		if state == "CO" or state == "MT" or state == "ND" or state == "SD" or state == "UT" or state == "WY":
			if r8 == False:
				reg8.write("8\n")
				r8 = True
			reg8.write(str(dataset.iloc[iterr, 1]) + ",")
			reg8.write(str(dataset.iloc[iterr, 2]) + ",")
			reg8.write(str(dataset.iloc[iterr, 5]) + ",")
			reg8.write(str(dataset.iloc[iterr, 0]) + ",")
			reg8.write(str(state) + ",")
			reg8.write(str(dataset.iloc[iterr, 6]) + ",")
			if i < 20:
				reg8.write(str(dataset.iloc[iterr, -1]) + "\n")
			else:
				reg8.write(str(dataset.iloc[iterr, -1]))
			if str(dataset.iloc[iterr, -1]) == "Y":
				count8 = count8 + 1

	# Region 9 - AZ, CA, NV
		if state == "AZ" or state == "CA" or state == "NV":
			if r9 == False:
				reg9.write("9\n")
				r9 = True
			reg9.write(str(dataset.iloc[iterr, 1]) + ",")
			reg9.write(str(dataset.iloc[iterr, 2]) + ",")
			reg9.write(str(dataset.iloc[iterr, 5]) + ",")
			reg9.write(str(dataset.iloc[iterr, 0]) + ",")
			reg9.write(str(state) + ",")
			reg9.write(str(dataset.iloc[iterr, 6]) + ",")
			if i < 20:
				reg9.write(str(dataset.iloc[iterr, -1]) + "\n")
			else:
				reg9.write(str(dataset.iloc[iterr, -1]))
			if str(dataset.iloc[iterr, -1]) == "Y":
				count9 = count9 + 1

	# Region 10 - ID, OR, WA
		if state == "ID" or state == "OR" or state == "WA":
			if r10 == False:
				reg10.write("10\n")
				r10 = True
			reg10.write(str(dataset.iloc[iterr, 1]) + ",")
			reg10.write(str(dataset.iloc[iterr, 2]) + ",")
			reg10.write(str(dataset.iloc[iterr, 5]) + ",")
			reg10.write(str(dataset.iloc[iterr, 0]) + ",")
			reg10.write(str(state) + ",")
			reg10.write(str(dataset.iloc[iterr, 6]) + ",")
			if i < 20:
				reg10.write(str(dataset.iloc[iterr, -1]) + "\n")
			else:
				reg10.write(str(dataset.iloc[iterr, -1]))
			if str(dataset.iloc[iterr, -1]) == "Y":
				count10 = count10 + 1

	# Region 11 - AK
		if state == "AK":
			if r11 == False:
				reg11.write("11\n")
				r11 = True
			reg11.write(str(dataset.iloc[iterr, 1]) + ",")
			reg11.write(str(dataset.iloc[iterr, 2]) + ",")
			reg11.write(str(dataset.iloc[iterr, 5]) + ",")
			reg11.write(str(dataset.iloc[iterr, 0]) + ",")
			reg11.write(str(state) + ",")
			reg11.write(str(dataset.iloc[iterr, 6]) + ",")
			if i < 20:
				reg11.write(str(dataset.iloc[iterr, -1]) + "\n")
			else:
				reg11.write(str(dataset.iloc[iterr, -1]))
			if str(dataset.iloc[iterr, -1]) == "Y":
				count11 = count11 + 1

	# Region 12 - HI
		if state == "HI":
			if r12 == False:
				reg12.write("12\n")
				r12 = True
			reg12.write(str(dataset.iloc[iterr, 1]) + ",")
			reg12.write(str(dataset.iloc[iterr, 2]) + ",")
			reg12.write(str(dataset.iloc[iterr, 5]) + ",")
			reg12.write(str(dataset.iloc[iterr, 0]) + ",")
			reg12.write(str(state) + ",")
			reg12.write(str(dataset.iloc[iterr, 6]) + ",")
			if i < 20:
				reg12.write(str(dataset.iloc[iterr, -1]) + "\n")
			else:
				reg12.write(str(dataset.iloc[iterr, -1]))
			if str(dataset.iloc[iterr, -1]) == "Y":
				count12 = count12 + 1
		iterr = iterr + 1


print("count1" + str(count1))
print("count2" + str(count2))
print("count3" + str(count3))
print("count4" + str(count4))
print("count5" + str(count5))
print("count6" + str(count6))
print("count7" + str(count7))
print("count8" + str(count8))
print("count9" + str(count9))
print("count10" + str(count10))
print("count11" + str(count11))
print("count12" + str(count12))

reg1.close()
reg2.close()
reg3.close()
reg4.close()
reg5.close()
reg6.close()
reg7.close()
reg8.close()
reg9.close()
reg10.close()
reg11.close()
reg12.close()
