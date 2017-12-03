from bs4 import BeautifulSoup
import better_exceptions

for i in range(1, 21):

	with open("../IAPD/IA_Indvl_Feeds" + str(i) + ".xml", 'rb') as f:
  		contents = f.read()

	soup = BeautifulSoup(contents, 'lxml')


	indiv_list = soup.find_all("indvl")

	data = open("feeds/feed" + str(i) + ".csv", "w")

	id = 0

	data.write("id,firstnm,lastnm,midnm,actv_agreg,orgnm,emp_str1,emp_city,emp_state,emp_cntry,emp_postlcd,regauth1,regcat1,reg_st1,regauth2,regcat2,reg_st2,b_str1,b_str2,b_city,b_state,b_cntry,b_postlcd,exmcd1,exmcd2,hasregaction,hascriminal,hasciviljudc,hasbond,hasjudgement,hasinvstgn,hascustcomp,hastermination,hasbankrupt\n")
	for person in indiv_list:

		data.write(str(id) + ",")
		try:
			#print(person.info["firstnm"])
			info = person.info["firstnm"].replace(',', '')
			info = info.replace('"', '')
			data.write(info + ",")
		except:
			data.write("NaN,")
		try:
			#print(person.info["lastnm"])
			info = person.info["lastnm"].replace(',', '')
			info = info.replace('"', '')
			data.write(info + ",")
		except:
			data.write("NaN,")
		try:	
			#print(person.info["midnm"])
			info = person.info["midnm"].replace(',', '')
			info = info.replace('"', '')
			data.write(info + ",")
		except:
			data.write("NaN,")
		try:
			# print(person.info["actvagreg"])
			info = person.info["actvagreg"].replace(',', '')
			info = info.replace('"', '')
			data.write(info + ",")
		except:
			data.write("NaN,")

#--------------------------------------------------------
		try:
			#print(person.crntemp["orgnm"])
			emp = person.crntemp["orgnm"].replace(',', '')
			emp = emp.replace('"', '')
			data.write(emp + ",")	
		except:
			data.write("NaN,")
		try:
			#print(person.crntemp["str1"])
			emp = person.crntemp["str1"].replace(',', '')
			emp = emp.replace('"', '')
			data.write(emp + ",")
		except:
			data.write("NaN,")
		try:
			#print(person.crntemp["city"])
			emp = person.crntemp["city"].replace(',', '')
			emp = emp.replace('"', '')
			data.write(emp + ",")
		except:
			data.write("NaN,")
		try:
			#print(person.crntemp["state"])
			emp = person.crntemp["state"].replace(',', '')
			emp = emp.replace('"', '')
			data.write(emp + ",")
		except:
			data.write("NaN,")
		try:
			#print(person.crntemp["cntry"])
			emp = person.crntemp["cntry"].replace(',', '')
			emp = emp.replace('"', '')
			data.write(emp + ",")
		except:
			data.write("NaN,")
		try:
			#print(person.crntemp["postlcd"])
			emp = person.crntemp["postlcd"].replace(',', '')
			emp = emp.replace('"', '')
			data.write(emp + ",")
		except:
			data.write("NaN,")

#----------------------------------------------
		try:
			# print(person.crntrgstn["regauth"])
			reg = person.crntrgstn["regauth"].replace(',', '')
			reg = reg.replace('"', '')
			data.write(reg + ",")
		except:
			data.write("NaN,")
		try:
			#print(person.crntrgstn["regcat"])
			reg = person.crntrgstn["regcat"].replace(',', '')
			reg = reg.replace('"', '')
			data.write(reg + ",")
		except:
			data.write("NaN,")
		try:
			# print(person.crntrgstn["st"]) STATUS
			reg = person.crntrgstn["st"].replace(',', '')
			reg = reg.replace('"', '')
			data.write(reg + ",")
		except:
			data.write("NaN,")
		try:
			# print(person.crntrgstn["regauth"])
			reg = person.crntrgstn["regauth"].replace(',', '')
			reg = reg.replace('"', '')
			data.write(reg + ",")
		except:
			data.write("NaN,")
		try:
			# print(person.crntrgstn["regcat"])
			reg = person.crntrgstn["regcat"].replace(',', '')
			reg = reg.replace('"', '')
			data.write(reg + ",")
		except:
			data.write("NaN,")
		try:
			# print(person.crntrgstn["st"])
			reg = person.crntrgstn["st"].replace(',', '')
			reg = reg.replace('"', '')
			data.write(reg + ",")
		except:
			data.write("NaN,")
#---------------------------------------------------

		try:
			#print(person.brnchofloc["str1"])
			branch = person.brnchofloc["str1"].replace(',', '')
			branch = branch.replace('"', '')
			data.write(branch + ",")
		except:
			data.write("NaN,")
		try:
			#print(person.brnchofloc["str2"])
			branch = person.brnchofloc["str2"].replace(',', '')
			branch = branch.replace('"', '')
			data.write(branch + ",")
		except:
			data.write("NaN,")
		try:
			#print(person.brnchofloc["city"])
			branch = person.brnchofloc["city"].replace(',', '')
			branch = branch.replace('"', '')
			data.write(branch + ",")
		except:
			data.write("NaN,")
		try:
			#print(person.brnchofloc["state"])
			branch = person.brnchofloc["state"].replace(',', '')
			branch = branch.replace('"', '')
			data.write(branch + ",")
		except:
			data.write("NaN,")
		try:
			#print(person.brnchofloc["cntry"])
			branch = person.brnchofloc["cntry"].replace(',', '')
			branch = branch.replace('"', '')
			data.write(branch + ",")
		except:
			data.write("NaN,")
		try:
			#print(person.brnchofloc["postlcd"])
			branch = person.brnchofloc["postlcd"].replace(',', '')
			branch = branch.replace('"', '')
			data.write(branch)
			data.write(",")
		except:
			data.write("NaN,")
#---------------------------------------------------

		try:
			#print(person.exm["exmcd"])
			exm = person.exm["exmcd"].repalce(',', '')
			exm = exm.replace('"', '')
			data.write(exm + ",")
		except:
			data.write("NaN,")
		try:
			#print(person.exm["exmcd"])
			exm = person.exm["exmcd"].replace(',', '')
			exm = exm.replace('"', '')
			data.write(exm)
			data.write(",")
		except:
			data.write("NaN,")

#---------------------------------------------------

		# print(person.drps["drp"])
		try:
			#print(person.drps.drp["hasregaction"])
			drp = person.drps.drp["hasregaction"].replace(',', '')
			drp = drp.replace('"', '')
			data.write(drp + ",")
		except:
			data.write("N,")
		try:
			#print(person.drps.drp["hascriminal"])
			drp = person.drps.drp["hascriminal"].replace(',', '')
			drp = drp.replace('"', '')
			data.write(drp + ",")
		except:
			data.write("N,")
		try:
			#print(person.drps.drp["hasciviljudc"])
			drp = person.drps.drp["hasciviljudc"].replace(',', '')
			drp = drp.replace('"', '')
			data.write(drp + ",")
		except:
			data.write("N,")
		try:
			#print(person.drps.drp["hasbond"])
			drp = person.drps.drp["hasbond"].replace(',', '')
			drp = drp.replace('"', '')
			data.write(drp + ",")
		except:
			data.write("N,")
		try:
			#print(person.drps.drp["hasjudgment"])
			drp = person.drps.drp["hasjudgment"].replace(',', '')
			drp = drp.replace('"', '')
			data.write(drp + ",")
		except:
			data.write("N,")
		try:
			#print(person.drps.drp["hasinvstgn"])
			drp = person.drps.drp["hasinvstgn"].replace(',', '')
			drp = drp.replace('"', '')
			data.write(drp + ",")
		except:
			data.write("N,")
		try:
			#print(person.drps.drp["hascustcomp"])
			drp = person.drps.drp["hascustcomp"].replace(',', '')
			drp = drp.replace('"', '')
			data.write(drp + ",")
		except:
			data.write("N,")
		try:
			#print(person.drps.drp["hastermination"])
			drp = person.drps.drp["hastermination"].replace(',', '')
			drp = drp.replace('"', '')
			data.write(drp + ",")
		except:
			data.write("N,")
		try:
			#print(person.drps.drp["hasbankrupt"])
			drp = person.drps.drp["hasbankrupt"].replace(',', '')
			drp = drp.replace('"', '')
			data.write(drp)
			data.write("\n")
		except:
			data.write("N")
			data.write("\n")

		id = id + 1
	data.close()
	f.close()
	#re-run because of close