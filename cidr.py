# Documentation

import sublime, sublime_plugin

class CidrOnCommand(sublime_plugin.TextCommand):
	def run(self, edit):

		masks = {
		"255.255.255.255": "/32",
		"255.255.255.254": "/31",
		"255.255.255.252": "/30",
		"255.255.255.248": "/29",
		"255.255.255.240": "/28",
		"255.255.255.224": "/27",
		"255.255.255.192": "/26",
		"255.255.255.128": "/25",
		"255.255.255.0": "/24",
		"255.255.254.0": "/23",
		"255.255.252.0": "/22",
		"255.255.248.0": "/21",
		"255.255.240.0": "/20",
		"255.255.224.0": "/19",
		"255.255.192.0": "/18",
		"255.255.128.0": "/17",
		"255.255.0.0": "/16",
		"255.254.0.0": "/15",
		"255.252.0.0": "/14",
		"255.248.0.0": "/13",
		"255.240.0.0": "/12",
		"255.224.0.0": "/11",
		"255.192.0.0": "/10",
		"255.128.0.0": "/9",
		"255.0.0.0": "/8"
		}

		for mask in masks:
			self.cidr_on(edit, mask, masks.get(mask))

	def cidr_on(self, edit, mask, cidr):
		ipmasks = self.view.find_all("\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3} " + mask)
		ipmasks.reverse()
		masks = []

		for region in ipmasks:
			regionstring = self.view.substr(region).split()
			regionstart = region.end() - len(regionstring[1]) - 1
			masks.append(sublime.Region(regionstart, region.end()))

		for region in masks:
			self.view.replace(edit, region, cidr)




		#debug:
#		for region in ipmasks:
#			self.view.insert(edit, self.view.size(), "\nIP: " + self.view.substr(region))
#
#		for region in masks:
#			self.view.insert(edit, self.view.size(), "\nIP: " + self.view.substr(region))



#		ipmasks = self.view.find_all("\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3} 255\.255\.255\.255")
#		regionstring = ""
#		masks = []
#
#		for region in ipmasks:
#			regionstring = self.view.substr(region)
#			regionstring = regionstring.split()
#			ip = regionstring[0]
#			mask = regionstring[1]
#			iplen = len(ip)
#			masklen = len(mask)
#			regionend = region.end()
#			regionstart = regionend - masklen - 1
#			region = sublime.Region(regionstart, regionend)
#			newregion = self.view.substr(region)
#
#			self.view.replace(edit, region, "/32")
#			#debug:
#			self.view.insert(edit, self.view.size(),
#				"\nDEBUG:"
#				 + "\nIP: " + ip
#				 + "\nMask: " + mask
#				 + "\niplen: " + str(iplen)
#				 + "\nmasklen: " + str(masklen)
#				 + "\nregionend: " + str(regionend)
#				 + "\nregionstart: " + str(regionstart)
#				 + "\nnewregion: " + newregion)