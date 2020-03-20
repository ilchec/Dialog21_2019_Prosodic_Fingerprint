from __future__ import division
import sys, os, operator, statistics,re
import math
home_dir = "./Pitch/"

#defining the working range of frequencies
numbers = []
full_text = []
for d, dirs, files in os.walk(home_dir):
	for dr in dirs:
		current_dir = home_dir + dr
		for d, dirs, files in os.walk(current_dir):
			for f in files:
				print(str(f))
				if f == ".DS_Store": continue
				current_file = open(current_dir+"/"+f, "r")
				for line in current_file:
					full_text.append(line.strip("\n"))
					full_source_ds = {}
				for line in full_text:
					if "Time_s" in line or "undefined" in line: 
						continue
					ln = re.sub("   ",";",line)
					a = ln.split(";")
					numbers.append(float(a[1]))
			numbers_no_outliers = numbers[math.floor(0.025*len(numbers)):math.ceil(len(numbers)-0.025*len(numbers))]	
			current_mean = statistics.mean(numbers)
			current_max = max(numbers)
			current_min = min(numbers)
			current_range = current_max - current_min	
			max_no_outliers = max(numbers_no_outliers)
			min_no_outliers = min(numbers_no_outliers)	
			range_no_outliers = max_no_outliers - min_no_outliers	
			thr1 = current_min + 0.025*current_range
			thr2 = min_no_outliers + (0.025 + 0.31666)*range_no_outliers
			thr3 = min_no_outliers + (0.025 + 2*0.31666)*range_no_outliers
			thr4 = min_no_outliers + (0.025 + 3*0.31666)*range_no_outliers
############	
			for f in files:	
				source_ds = {}
				s = "Speaker_ID;Sex;Place;Age;Text;Sentence;Time_s;Abs_value;Unigram\n"
				s_counted = "Speaker_ID;Sex;Place;Age;Text;Sentence;-1;0;1;NA\n"
				table = []
				if f == ".DS_Store": continue
				dir = f.split("_")[1]
				place = f.split("_")[0]
				sex = f.split("_")[2]
				age = f.split("_")[3]
				text = f.split("_")[4]
				sentence = f.split("_")[5].strip(".csv")
			#place = f.split("_")[0]
				current_file = open(current_dir+"/"+f, "r")
				for line in current_file:
					table.append(line.strip("\n")) 
				converted_ds = {}
				counted_ds = {"-1":0,"0":0,"1":0,"NA":0}
				current_time = 0
				for line in table:
					if "Time_s" in line: 
						continue
					if "--" in line:
						current_time = str(round(float(current_time)+0.01,6))
						source_ds[current_time] = "NA"
					else:	
						ln = re.sub("   ",";",line)
						a = ln.split(";")
						source_ds[a[0]] = a[1]
						current_time = a[0]
				for element in source_ds:
					if source_ds[element] == "NA":
						converted_ds[element] = "NA"
					elif float(source_ds[element]) <= thr1:
						continue
					elif float(source_ds[element]) <= thr2:
						converted_ds[element] = -1
					elif float(source_ds[element]) <= thr3:
						converted_ds[element] = 0
					elif float(source_ds[element]) <= thr4:
						converted_ds[element] = 1
					elif float(source_ds[element]) > thr4:
						continue
					counted_ds[str(converted_ds[element])] += 1
				s_counted += (str(dir)+";"+str(sex)+";"+str(place)+";"+str(age)+";"+str(text)+";"+str(sentence)+";"+str(counted_ds["-1"])+";"+str(counted_ds["0"])+";"+str(counted_ds["1"])+";"+str(counted_ds["NA"])+"\n")
				for element in converted_ds:
					s += (dir+";"+sex+";"+place+";"+age+";"+text+";"+sentence+";"+str(element)+";"+str(source_ds[element])+";"+str(converted_ds[element])+"\n")
				f_write = open("Unigrams.csv","a")
				f_write.write(s)
				f_write.close()
	
				f_counted = open("Unigrams_counted.csv","a")
				f_counted.write(s_counted)
				f_counted.close()
