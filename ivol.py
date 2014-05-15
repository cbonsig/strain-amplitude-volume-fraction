# ivol.py
# =======

# a Python script for use with ABAQUS to sum the volume of elements
# exceeding a specified strain amplitude threshold

# original code by Payam Saffari

# The MIT License (MIT)

# Copyright (c) 2013-2014 Nitinol Devices & Components, Inc.

# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:

# The above copyright notice and this permission notice shall be included in all
# copies or substantial portions of the Software.

# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
# SOFTWARE.


from abaqus import*
from abaqusConstants import*
import visualization
from math import *
import displayGroupOdbToolset as dgo
user_inputs=getInputs(fields=(('Variable Name:','amp'),('Limit:','1.2e-3'),('Stent Instance Name (case sesnstive):','STENT')),label='Please Provide the Following Information',dialogTitle='Model Parameters')
vp = session.viewports[session.currentViewportName]
odb = vp.displayedObject
odb_name=odb.name
dle=session.scratchOdbs[odb_name].steps['Session Step'].frames[0].fieldOutputs[user_inputs[0]]
print 'finding critical elements'
critical_elements_positions_dict={}
critical_elements_positions=[]	
critical_elements=[]
i=0
for k in dle.values:
	if k.maxPrincipal>=float(user_inputs[1]):
		critical_elements.append(k.elementLabel)
		critical_elements_positions.append(i)
		critical_elements_positions_dict[k.elementLabel]=i
	i=i+1
print 'finding connected elements'
element=dle.values[0].instance.elements
connected_elements=[]	
for p in critical_elements_positions:
	a=[]
	a.append(element[p].label)
	element_connectivity=element[p].connectivity
	for j in critical_elements_positions:
		i=0
		for t in element_connectivity:
			if t in element[j].connectivity:
				i=i+1
		if i==4:
			a.append(element[j].label)
	connected_elements.append(a) 
connected_elements_dict={}
for i in range(len(connected_elements)):
	connected_elements_dict[connected_elements[i][0]]=connected_elements[i][1:]
##############################################################################################
print 'making final list'
final={}
for element in connected_elements_dict.keys():
	q=0
	for k in final.itervalues():
		if element in k:
			q=1
			break
	if q==0:
		i=0
		test=connected_elements_dict[element]
		while i<3*len(connected_elements):
			i=i+1
			for p in test:
				for t in connected_elements_dict[p]:
					if not t in test:
						test.append(t)
		final[element]=test
#############################################################################################
print 'modifying final list'
for m in critical_elements:
	if m in final.keys():
		for n in critical_elements:
			if n in final.keys():
				if not m==n:
					for i in final[n]:
						if i in final[m]:
							del final[n]
							break
#############################################################################################
print 'making batches'
critical_batches={}
for index in range(len(final.keys())):
	inter=final[final.keys()[index]]
	if not final.keys()[index] in inter:
		inter.append(final.keys()[index])
	inter.sort()
	critical_batches[index+1]=inter
print 'Number of Critical Batches:'+str(len(critical_batches))
############################################################################################
step_name=session.odbs[odb_name].steps.keys()[0]
ivol=session.odbs[odb_name].steps[step_name].frames[0].fieldOutputs['IVOL'].values
critical_batches_vol={}
leaf = dgo.LeafFromModelElemLabels(elementLabels=((user_inputs[2], (critical_elements)),))
dg = session.DisplayGroup(leaf=leaf, name='Critical_Elements')
for index in critical_batches.keys():
	vol=0
	for element in critical_batches[index]:
		position=critical_elements_positions_dict[element]
		vol=vol+ivol[element].data
	critical_batches_vol[index]=vol
	leaf = dgo.LeafFromModelElemLabels(elementLabels=((user_inputs[2], (critical_batches[index])),))
	dg = session.DisplayGroup(leaf=leaf, name='Batch-'+str(index)+',vol='+str(vol))
print critical_batches_vol
print 'Done!!!'	

	

